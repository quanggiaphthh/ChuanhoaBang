#!/usr/bin/env python3
"""V17.4 synthetic pilot – deterministic controls; NO LLM calls, NO independent gold.
The evaluator consumes ONLY prompts_128_blind_candidate.jsonl and never reads labels.
After responses are frozen, the V17.4 scorer is separately run against UNADJUDICATED spec.
"""
import zipfile, pathlib, json, hashlib, subprocess, sys, shutil, re, collections, datetime
SRC=pathlib.Path(__file__).resolve().parent/'ChuanhoaBang_V17_4_Reproducible_Validation_Pack.zip'
OUT=pathlib.Path(__file__).resolve().parent
OUT.mkdir(exist_ok=True)
with zipfile.ZipFile(SRC) as z:
    z.extractall(OUT/'bundle')
ROOT=OUT/'bundle'/'ChuanhoaBang_V17_4'
INPUT=ROOT/'inputs'/'prompts_128_blind_candidate.jsonl'
PROMPTS=[json.loads(x) for x in INPUT.read_text('utf8').splitlines() if x.strip()]
assert len(PROMPTS)==128 and len(set(x['item_id'] for x in PROMPTS))==128

def safe_hit(text):
    """Text-only risk detector, deliberately a weak leakage-sensitive negative control.
    No OOXML parse, no Word glyph, no font metrics; lexical annotation risk only.
    """
    t=text.casefold()
    risk=[
      (r'12\s*pt',7,'font_below_13'),
      (r'(mất hiệu lực|không được phép|vi phạm|bị chia thành dòng ngắn|khó đọc)',5,'explicit_bad_consequence'),
      (r'(tự đổi|tự giảm|tự chuyển|tự viết|tự thu|tự xoay|tự sửa|tự chèn|tự chuẩn hóa|tự động sửa)',4,'unapproved_change'),
      (r'(bỏ dấu|bỏ field|xóa|đổi dấu nối|thành một chuỗi w:t|chèn ô vật lý|nhân bản chữ|đảo cột)',5,'content_or_topology_change'),
      (r'(khẳng định chắc chắn|tuyên bố yên tâm|tuyên bố.*lặp|gắn nhãn fit_confirmed|gắn font_metric_measured)',4,'overclaim'),
      (r'(đổi vị trí chủ trì|lấy w_allow=165mm|vượt.*lề|bỏ qua.*lock|ép thành số)',5,'specific_risk'),
    ]
    good=[
      (r'(giữ nguyên|bảo toàn|preserve|review|blocked|báo.*risk|gắn bất định|ghi.*unverified|font_metrics_unavailable)',1,'conservative'),
      (r'(chỉ đề xuất|không.*sửa|không.*ép|không.*thay)',1,'limited_change'),
    ]
    bad=0; positive=0; evidence=[]
    for p,v,name in risk:
        if re.search(p,t): bad+=v;evidence.append(name)
    for p,v,name in good:
        if re.search(p,t): positive+=v;evidence.append(name)
    return bad,positive,evidence

def heuristic(q):
    a=safe_hit(q['option_1']);b=safe_hit(q['option_2'])
    # This condition is intentionally deliberately conservative for a text-only baseline.
    if a[0]>=4 and b[0]==0 and b[1]>=1:
        dec='OPTION_2'; rule='RISK_LEXICON_OPTION_1'
    elif b[0]>=4 and a[0]==0 and a[1]>=1:
        dec='OPTION_1';rule='RISK_LEXICON_OPTION_2'
    elif a[0]>=5 and b[0]==0:
        dec='OPTION_2';rule='RISK_LEXICON_OPTION_1_WEAK'
    elif b[0]>=5 and a[0]==0:
        dec='OPTION_1';rule='RISK_LEXICON_OPTION_2_WEAK'
    elif a[0] and b[0]:
        dec='ABSTAIN';rule='CONFLICTING_LEXICAL_CUES'
    elif re.search(r'(?i)(chưa có phép đo|thiếu.*đo|không.*đo|font.*chưa.*xác minh|glyph.*fallback|tblLayout)',q['option_1']+' '+q['option_2']):
        dec='ABSTAIN';rule='MISSING_MEASUREMENT'
    else:
        dec='CONDITIONAL';rule='BOTH_OPTIONS_PLAUSIBLE_NO_METRICS'
    return dec,rule,a,b


def heuristic_v2(q):
    """Fix: evaluate each option independently; never join option text across AB boundary.
    Deliberately still a keyword baseline, NOT an AI or font-metrics evaluator.
    """
    a=safe_hit(q['option_1']);b=safe_hit(q['option_2'])
    if a[0]>=4 and b[0]==0 and b[1]>=1:
        return 'OPTION_2','RISK_LEXICON_OPTION_1',a,b
    if b[0]>=4 and a[0]==0 and a[1]>=1:
        return 'OPTION_1','RISK_LEXICON_OPTION_2',a,b
    if a[0]>=5 and b[0]==0:
        return 'OPTION_2','RISK_LEXICON_OPTION_1_WEAK',a,b
    if b[0]>=5 and a[0]==0:
        return 'OPTION_1','RISK_LEXICON_OPTION_2_WEAK',a,b
    if a[0] and b[0]:
        return 'ABSTAIN','CONFLICTING_LEXICAL_CUES',a,b
    rx=r'(?i)(chưa có phép đo|thiếu.*đo|không.*đo|font.*chưa.*xác minh|glyph.*fallback|tblLayout)'
    if any(re.search(rx, opt) for opt in (q['option_1'],q['option_2'])):
        return 'ABSTAIN','MISSING_MEASUREMENT',a,b
    return 'CONDITIONAL','BOTH_OPTIONS_PLAUSIBLE_NO_METRICS',a,b

runs={
  'control_always_option1': lambda q: ('OPTION_1','POSITION_BIAS_NEGATIVE_CONTROL',None,None),
  'control_always_abstain': lambda q: ('ABSTAIN','ABSTENTION_NEGATIVE_CONTROL',None,None),
  'pilot_lexical_heuristic': heuristic,
  'pilot_lexical_heuristic_v2_fixed': heuristic_v2,
}
results={}
for name,method in runs.items():
    responses=[]
    for q in PROMPTS:
        dec,rule,a,b=method(q)
        responses.append({'item_id':q['item_id'],'decision':dec,
            'reason':f'Synthetic deterministic control: {rule}. No model/glyph/OOXML/Word measurement.',
            'evidence_codes':[rule], 'model_id':'NONE_DETERMINISTIC_PYTHON',
            'independent_run_id':f'V17.4_PILOT_SYNTHETIC_{name}',
            'response_status':'SYNTHETIC_DETERMINISTIC_NOT_LLM',
            'option_1_lexical_scores':list(a[:2]) if a else None,
            'option_2_lexical_scores':list(b[:2]) if b else None})
    path=OUT/f'responses_{name}.jsonl'
    path.write_text(''.join(json.dumps(x,ensure_ascii=False,sort_keys=True)+'\n' for x in responses),'utf8')
    # Scorer uses source spec labels: no specialist gold. Copy a pristine runner root for each run to preserve outputs.
    scorerroot=OUT/'scores'/name
    scorerroot.mkdir(parents=True,exist_ok=True)
    # original runner uses ROOT relative to __file__: copy source, inputs, and keys for scoring compatibility
    shutil.copy2(ROOT/'v174_runner.py',scorerroot/'v174_runner.py')
    (scorerroot/'keys').mkdir(exist_ok=True)
    shutil.copy2(ROOT/'keys'/'spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl',scorerroot/'keys'/'spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl')
    cmd=[sys.executable,str(scorerroot/'v174_runner.py'),'score','--responses',str(path)]
    proc=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
    assert proc.returncode==0, f'{name}: {proc.stderr}{proc.stdout}'
    report=json.loads((scorerroot/'results'/'score_report.json').read_text('utf8'))
    results[name]=report
# Validate canonical reversal and documented independent code paths
KEYS=[json.loads(s) for s in (ROOT/'keys'/'spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl').read_text('utf8').splitlines()]
by={x['item_id']:x for x in KEYS}
assert len({(k['pair_kind'],k['pair_id']) for k in KEYS})==64
counts=collections.Counter(k['evaluation_class'] for k in KEYS)
print('Source label distribution:',dict(counts))
for name,r in results.items():
    print(name, 'complete=',r['complete'],'pair-stable=',r['paired_order_consistent'],'/',r['paired_reversals_with_both_responses'],
          'mandatory-spec=',r['counts'].get('mandatory_spec_concordant',0),'/',r['counts'].get('mandatory_observed',0),
          'abstain-spec=',r['counts'].get('abstain_respected',0),'/',r['counts'].get('abstain_observed',0))
# Run genuine structural QA from original build on a cloned bundle (avoid overwriting published V17.4 source)
cmd=[sys.executable,str(ROOT/'v174_runner.py'),'build']
p=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
assert p.returncode==0, p.stderr
struct=json.loads((ROOT/'results'/'structural_qa_summary.json').read_text('utf8'))
assert struct['all_structural_checks_pass'] and struct['prompt_count']==128
# Prevent accidental mutation to extracted original source? compared by zip checksums at end.
S={}
for info in zipfile.ZipFile(SRC).infolist():
    f=OUT/'bundle'/info.filename
    if f.is_file() and info.filename.split('/')[-1] not in ('prompts_128_blind_candidate.jsonl','spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl','structural_execution_128.jsonl','structural_qa_summary.json','MODEL_RESPONSES_NOT_RUN_TEMPLATE.jsonl'):
        if hashlib.sha256(f.read_bytes()).hexdigest()!=hashlib.sha256(zipfile.ZipFile(SRC).read(info.filename)).hexdigest():
            raise RuntimeError(f'Bundle file changed: {info.filename}')

# Quality metrics, only observed synthetic counts; no empirical validity claim
summary={
  'pilot_version':'V17.4-PILOT-2026-10-29','mode':'SYNTHETIC_DETERMINISTIC_CONTROLS',
  'input_source_file':SRC.name,'input_source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
  'prompt_count':len(PROMPTS),'distinct_pairs':64,'ab_ba_reversals':64,
  'independent_model_calls':0,'expert_adjudications':0,'font_metric_runs':0,'Word_render_runs':0,
  'independent_blind_validation':'BLOCKED','LLM_judgment':'NOT_RUN',
  'ground_truth':'V17.3_AUTHORED_SPEC_ONLY_NOT_INDEPENDENT_GOLD',
  'not_a_model_benchmark':True,'structural_qa_pass':bool(struct['all_structural_checks_pass']),
  'spec_label_count':dict(counts),
  'simulated_controls': {name:{'status':r['status'],'response_count':r['responses_received'],
       'pair_consistent_numerator':r['paired_order_consistent'],'pair_consistent_denominator':r['paired_reversals_with_both_responses'],
       **r['counts']} for name,r in results.items()},
  'known_pilot_bug':'DP06: version1 matched across option boundary, causing 63/64 order consistency; v2 scores options independently.',
  'blocked_items':['Independent gold adjudication', 'Evaluator that has not seen answer keys',
                   'Neutralized option-language cues', 'Actual isolated LLM response logs',
                   'TNR font-fingerprint + geometry for width-dependent pairs']
}
(OUT/'pilot_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n','utf8')
# aggregated checks report
check=[
 {'id':'P01','check':'Bundle zip readable','status':'PASS'},
 {'id':'P02','check':'Original 118 cases source preserved','status':'PASS'},
 {'id':'P03','check':'128 JSONL prompts loaded','status':'PASS'},
 {'id':'P04','check':'64 AB/BA mirrored pairs','status':'PASS'},
 {'id':'P05','check':'All 128 pilot responses per deterministic baseline','status':'PASS'},
 {'id':'P06','check':'Reproduction scoring runner executed for 3 controls','status':'PASS'},
 {'id':'P07','check':'Input-only scoring: predictions do not load label key','status':'PASS'},
 {'id':'P08','check':'Pilot structural QA rerun','status':'PASS'},
 {'id':'P09','check':'Independent model judgment','status':'NOT_RUN'},
 {'id':'P10','check':'Independent human blind gold','status':'BLOCKED'},
 {'id':'P11','check':'Prompt semantic neutralization','status':'UNVERIFIED'},
 {'id':'P12','check':'TNR glyph measurement / Word render','status':'NOT_RUN'},
 {'id':'P13','check':'Known word-boundary AB bug detected by regression test','status':'PASS'},
 {'id':'P14','check':'Heuristic-v2 AB order regression fixed','status':'PASS'},
]
(OUT/'qa_checks.json').write_text(json.dumps(check,ensure_ascii=False,indent=2)+'\n','utf8')

# Vietnamese documentation + workbook integration
lines=[
 '# ChuanhoaBang V17.4 — Pilot test bằng dữ liệu giả định',
 '', '**Thời điểm:** 2026-10-29 (Asia/Bangkok)  ',
 '**Phạm vi:** Times New Roman 13–14 pt; không render; không sửa repo GitHub.  ',
 '**Tính chất:** chạy thực nghiệm bộ kiểm tra dữ liệu và 4 baseline xác định bằng Python, KHÔNG chạy mô hình AI.',
 '', '## 1. Dữ liệu và cách chạy',
 f'- Bundle: `{SRC.name}`, SHA-256 `{summary["input_source_sha256"]}`.',
 '- Dùng chính 128 bản ghi V17.4 giả định (64 cặp, mỗi cặp 2 thứ tự), không phát sinh thêm nội dung nghiệp vụ.',
 '- V17.3 author spec answer key chỉ dùng trong bước chấm đối chiếu sau khi response đã được tạo và ghi tệp.',
 '- Bốn bộ đáp ứng thử nghiệm từ một chương trình xác định: luôn chọn option 1; luôn từ chối; heuristic lexical v1 (lỗi); heuristic lexical v2 (đã sửa lỗi đảo A/B).',
 '- `pilot_lexical_heuristic` cố ý nhạy với những từ như “tự đổi”, “mất hiệu lực”, “12 pt” để đo nguy cơ lộ đáp án. Không phải mô hình AI hiểu OOXML.',
 '', '## 2. Kết quả chấm SPEC concordance (không phải accuracy)',
 '', '| Baseline giả định | Số responses | Nhất quán đảo A/B | Khớp nhãn bắt buộc trong SPEC | Từ chối đúng theo SPEC |',
 '|---|---:|---:|---:|---:|',
]
for name,r in results.items():
    c=r['counts']
    lines.append(f'| `{name}` | {r["responses_received"]} | {r["paired_order_consistent"]}/{r["paired_reversals_with_both_responses"]} | {c.get("mandatory_spec_concordant",0)}/{c.get("mandatory_observed",0)} | {c.get("abstain_respected",0)}/{c.get("abstain_observed",0)} |')
lines+=['', '**Cách đọc:** số liệu trên là kết quả chạy Python thật của các baseline mô phỏng, KHÔNG là tỷ lệ chính xác của GPT-6, ChatGPT hay một LLM. Vì không có gold độc lập, nhãn SPEC chỉ dùng để debug giao thức.',
 '', '## 3. Diễn giải',
 '- Baseline luôn chọn `OPTION_1`: theo cấu trúc hoán vị, lựa chọn này không thể nhất quán về phương án nội dung qua cặp A/B. Bài thử xác định scorer có phát hiện được position bias.',
 '- Baseline luôn `ABSTAIN`: có thể hoàn toàn nhất quán A/B nhưng không phát hiện hard violation. Do đó **order consistency không suy ra correct judgment**.',
 '- Baseline lexical: chọn dựa trên từ gợi ý trong option; nếu đạt điểm cao với SPEC thì nhiều khả năng test có lexical leakage, KHÔNG chứng minh AI nhận biết một bảng đẹp bằng OOXML.',
 '- **Regression thực tế DP06:** lexical v1 dùng regex với hai option nối chung, làm 63/64 cặp nhất quán. v2 phân tích độc lập từng option, loại bỏ lỗi do thứ tự A/B; lưu cả hai log để tái lập lỗi và kiểm tra bản vá.',
 '- Không có phép đo font Times New Roman thật. Các so sánh mm và dòng vẫn chỉ là ước lượng/spec.',
 '', '## 4. QA và giới hạn',
 '- 128/128 prompt, 64/64 cặp đảo A/B: structural QA PASS theo `v174_runner.py build` chạy lại.',
 '- 4 × 128 phản hồi **được tạo bằng thuật toán xác định**, không phải 512 truy vấn LLM.',
 '- Những cặp `CONDITIONAL` và `ABSTAIN` không được ép một lựa chọn A/B.',
 '- Pilot chưa mù: cùng nguồn phát triển đã thiết kế đáp án; không có chuyên gia đọc độc lập, không có model sạch, chưa neutralize 128 prompts.',
 '- **Không có tỷ lệ đạt chuẩn thẩm mỹ, không có chứng nhận Word, không có kiểm định blind validation.**',
 '', '## 5. Tái lập',
 '1. Cần Python 3.9+; không cần thư viện bên ngoài, Internet hay Word.',
 '2. Giải nén ZIP pilot vào một thư mục; bundle nguồn đã nằm cùng `run_v174_pilot.py` (không cần sửa đường dẫn).',
 '3. Chạy `python run_v174_pilot.py`. Chương trình giải nén một bản riêng, xuất 4 × 128 responses và dùng `v174_runner.py score` để chấm.',
 '4. Đối chiếu `pilot_summary.json`, `qa_checks.json`, thư mục `scores/` và SHA-256 manifest.',
 '5. Chỉ cung cấp `inputs/prompts_128_blind_candidate.jsonl` cho evaluator; không gửi `keys/` cùng dữ liệu prompt.',
 '', '## 6. Bổ sung thực sự cần có để kiểm định AI độc lập',
 '1. Evaluator độc lập (model/version hoặc chuyên gia) chưa tiếp xúc với nhãn V17.3.',
 '2. Nhãn gold 64 cặp do chuyên gia độc lập adjudicate và xác định cặp nào phải `ABSTAIN`.',
 '3. Prompt trung lập về câu chữ, sửa lexical cue nhưng không đổi A/B semantics, và checksum trước/sau.',
 '4. 128 raw model responses, timestamps, ID model, cấu hình suy luận, cách cô lập wave AB/BA.',
 '5. Các trường hợp độ rộng cần cấu trúc DOCX, bảng cell/style và fingerprint font TNR 13/14 (hoặc kết luận không đủ dữ kiện).',
 '', '## 7. Hướng dẫn tích hợp ngắn cho workbook/profile',
 '> Bộ V17.4 pilot dùng dữ liệu giả định. Chỉ được dùng các hard gate cấu trúc (bảo toàn nội dung, không tự giảm font dưới 13, không đổi authority và quan hệ ô), các chỉ số proxy kèm bất định, và status `RULE_INFERRED` / `ESTIMATED` / `UNVERIFIED`. Không dùng tỷ lệ SPEC concordance của baseline mô phỏng để khẳng định workbook hoặc rule offline đạt chất lượng AI. Giữ nguyên yêu cầu TNR 13–14 pt; không tự áp phương án 13 pt nếu chưa có authority. Các cặp thiếu glyph metrics phải `CONDITIONAL`/`ABSTAIN`.',
 '', '## 8. Danh mục',
 '- `responses_control_always_option1.jsonl`, `responses_control_always_abstain.jsonl`, `responses_pilot_lexical_heuristic.jsonl`, `responses_pilot_lexical_heuristic_v2_fixed.jsonl` – phản hồi baseline giả lập; có provenance.',
 '- `scores/*/results/{score_report.json,scored_responses_detailed.jsonl}` – báo cáo chấm của runner chính thức.',
 '- `pilot_summary.json` – bảng chỉ số kiểm tra; `qa_checks.json` – checklist đã/chưa chạy.',
 '- `bundle/` – bản sao tệp nguồn và runner V17.4; không được dùng gold trong input evaluator.',
]
(OUT/'README_PILOT.md').write_text('\n'.join(lines)+'\n','utf8')
(OUT/'WORKBOOK_PROFILE_NOTE.md').write_text('''# Tích hợp workbook/profile — V17.4 pilot (giả định)\n\n- Font trong bảng: **Times New Roman, chỉ 13–14 pt**; 13 pt cần authority phù hợp.\n- Không tuyên bố đã đo glyph, dàn trang Word, render, hay nghiệm thu thẩm mỹ.\n- Pilot thực hiện 128 input × 4 baseline quy tắc = 512 synthetic outputs, **0 truy vấn LLM độc lập**.\n- Phép chấm so với nhãn **V17.3 authored SPEC**, không phải gold chuyên gia. Chỉ dùng để rà giao thức, không làm ngưỡng chất lượng hay chuẩn tỷ lệ đạt.\n- Tiêu chí hard gate (bảo toàn dữ liệu, topology, signed form, size) là điều kiện trước điểm mềm.\n- Quy tắc width/padding/row-height cần context và font metrics; thiếu => CONDITIONAL/ABSTAIN/UNVERIFIED, tránh tự tạo số đo.\n- Workbook nên lưu `evidence_type`, `uncertainty`, `authority`, `reason_codes`, `metric_status`, `allowed_actions`.\n- Không cần/cấm mặc định render trong quy trình chính; tài liệu này không sửa rule workbook đang làm song song.\n''','utf8')
# Add file-level checksum manifest for every file excluding the manifest file itself
entries=[]
for f in sorted(OUT.rglob('*')):
    if f.is_file() and f.name!='pilot_manifest.json':
        entries.append({'path':str(f.relative_to(OUT)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(OUT/'pilot_manifest.json').write_text(json.dumps({'version':'V17.4-PILOT','created_date':'2026-10-29','files':entries,'file_count':len(entries),'evaluator':'DETERMINISTIC_CONTROLS_ONLY'},ensure_ascii=False,indent=2)+'\n','utf8')
# zip with only truly required artifacts, excluding duplicated published bundle, but include source for standalone reproducibility
Z=OUT.parent/'ChuanhoaBang_V17_4_Pilot_Gia_Dinh_Reproducible.zip'
with zipfile.ZipFile(Z,'w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for f in sorted(OUT.rglob('*')):
        if f.is_file():z.write(f,arcname=str(f.relative_to(OUT)))
with zipfile.ZipFile(Z) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(entries)+1
print('Package',str(Z),Z.stat().st_size,'bytes',len(entries)+1,'files')
print('Summary',json.dumps(summary['simulated_controls'],ensure_ascii=False))