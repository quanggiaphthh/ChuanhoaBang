#!/usr/bin/env python3
"""Reproducible structural/paired-evaluation harness for ChuanhoaBang V17.4.
Not a Word renderer, font-measurement engine, LLM, or independent validator.
Stdlib only. No network/API calls.
"""
import argparse, collections, csv, hashlib, json, random, re, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SEED=17420261029
REQUIRED={'A_REQUIRED','B_REQUIRED'}
RECOMMENDED={'A_RECOMMENDED','B_RECOMMENDED'}
UNRESOLVED={'ABSTAIN','CONDITIONAL'}
ALLOWED_DECISIONS={'OPTION_1','OPTION_2','CONDITIONAL','ABSTAIN'}

def readj(path):
    with open(path,encoding='utf8') as f:return [json.loads(line) for line in f if line.strip()]
def writej(path,data):
    path.parent.mkdir(parents=True,exist_ok=True)
    with open(path,'w',encoding='utf8') as f:
        for row in data:f.write(json.dumps(row,ensure_ascii=False,sort_keys=True)+'\n')
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def original_inputs():
    s=ROOT/'source'
    names=['ChuanhoaBang_V17_3_40_Contrastive_Pairs.jsonl','ChuanhoaBang_V17_3_24_Design_Utility_Pairs.jsonl','ChuanhoaBang_V17_3_Blind_Test_80_Prompts.jsonl','ChuanhoaBang_V17_3_Blind_Test_48_Design_Prompts.jsonl','ChuanhoaBang_V17_3_118_Case_Evidence_Audit.jsonl']
    return {n:readj(s/n) for n in names}

def normopt(text):
    # Strip the old variant-ID letter at the beginning, but preserve substance.
    return re.sub(r'^\s*[AB]\s*[:：]\s*','',text,count=1).strip()

def build():
    src=original_inputs();a=src['ChuanhoaBang_V17_3_40_Contrastive_Pairs.jsonl'];b=src['ChuanhoaBang_V17_3_24_Design_Utility_Pairs.jsonl']
    cp={x['pair_id']:x for x in a};dp={x['pair_id']:x for x in b};prompt80=src['ChuanhoaBang_V17_3_Blind_Test_80_Prompts.jsonl'];prompt48=src['ChuanhoaBang_V17_3_Blind_Test_48_Design_Prompts.jsonl']
    cases=src['ChuanhoaBang_V17_3_118_Case_Evidence_Audit.jsonl']
    checks=[]
    def check(name,passed,detail=''):
        checks.append({'check':name,'status':'PASS' if passed else 'FAIL','detail':detail})
    check('CASE_COUNT_AND_IDS',len(cases)==118 and set(x['case_id'] for x in cases)=={f'NR{i:02d}' for i in range(1,119)},'Expected NR01 through NR118')
    check('PAIR_COUNTS',len(cp)==40 and len(dp)==24,'40 CP + 24 DP')
    check('ORIGINAL_INPUT_COUNTS',len(prompt80)==80 and len(prompt48)==48,'80 CP prompts + 48 DP prompts')
    check('UNIQUE_PAIR_IDS',len(cp)==len(a) and len(dp)==len(b),'No pair ID collision')
    indexed=[];errors=[]
    for kind,source,items in [('CP',cp,prompt80),('DP',dp,prompt48)]:
        for x in items:
            orig_id=x['blind_id'] if kind=='CP' else x['prompt_id']
            if not re.match(rf'^{kind}\d{{2}}_(AB|BA)$',orig_id):errors.append(f'MALFORMED:{orig_id}');continue
            pair_id,orientation=orig_id.rsplit('_',1)
            if pair_id not in source:errors.append(f'UNKNOWN_PAIR:{orig_id}');continue
            o=source[pair_id]
            expected1=o['variant_A'] if orientation=='AB' else o['variant_B']
            expected2=o['variant_B'] if orientation=='AB' else o['variant_A']
            if x['option_1']!=expected1 or x['option_2']!=expected2:errors.append(f'REVERSE_WRONG:{orig_id}')
            if x['table_rows']!=o['source_rows']:errors.append(f'ROW_CHANGED:{orig_id}')
            if x['font_family']!='Times New Roman' or x['font_size_pt'] not in (13,14):errors.append(f'FONT_INVALID:{orig_id}')
            if x['reader_task']!=o['reader_task']:errors.append(f'TASK_CHANGED:{orig_id}')
            indexed.append((kind,pair_id,orientation,o,x,orig_id))
    check('PROMPT_MAPPING_AND_TNR',not errors,';'.join(errors[:20]) if errors else 'Exact row/option/reader task reversals, TNR 13-14 pt')
    counts=collections.Counter((kind,pair_id,orient) for kind,pair_id,orient,*_ in indexed)
    check('COMPLETE_AB_BA_PER_PAIR',len(counts)==128 and all(v==1 for v in counts.values()) and all(counts[(kind,pid,o)]==1 for kind,group in [('CP',cp),('DP',dp)] for pid in group for o in ['AB','BA']),'Exactly two orientations per pair')
    check('PAIR_SOURCE_CASE_PRESENT',all((x['case_id'] if kind=='CP' else x['base_case']) in {z['case_id'] for z in cases} for kind,_,_,x,_,_ in indexed),'Each source case is in 118-case audit')
    case_sizes=collections.Counter(x['font_size_declared_pt'] for x in cases)
    coverage=len({x['case_id'] for x in cp.values()}|{x['base_case'] for x in dp.values()})
    check('CASE_REFERENCE_COVERAGE_REPORTED',coverage==53,'Only 53 of 118 audited NR cases appear in 64 pairs')
    check('UNRESOLVED_FONTS_REPORTED',case_sizes[None]==4,'Four 118-case audit entries have no declared point size')
    check('PAIR_LABELS_SCHEMA',all(x['expected'] in REQUIRED|RECOMMENDED|UNRESOLVED for x in list(cp.values())+list(dp.values())),'Every spec label is recognized')
    # Deterministic pseudorandom IDs and order; IDs provide only label-key separation.
    rng=random.Random(SEED)
    identifiers=list(range(1,len(indexed)+1));rng.shuffle(identifiers)
    prompts=[];secret=[];struct=[]
    for (kind,pid,orientation,o,srcp,orig_id),ix in zip(indexed,identifiers):
        opaque=f'TQ{ix:04d}'
        q={'item_id':opaque,'reader_task':srcp['reader_task'],'font_family':'Times New Roman',
           'font_size_pt':srcp['font_size_pt'],'table_rows':srcp['table_rows'],
           'option_1':normopt(srcp['option_1']),'option_2':normopt(srcp['option_2']),
           'instruction':'Assess with no rendering. Return exactly one decision OPTION_1, OPTION_2, CONDITIONAL, or ABSTAIN; give concise structural/rule evidence, unknown measurements, and uncertainty. Do not assume Word-equivalent font measurement or legal certification. Use only Times New Roman 13–14 pt.'}
        if kind=='CP':q['pair_condition']=srcp.get('pair_condition','')
        else:q['policy']='Size 13 pt is allowed only with explicit authority; preserve legal/form constraints.'
        expected=o['expected'];base=expected[0] if expected.startswith(('A_','B_')) else None
        preferred=(('OPTION_1' if orientation=='AB' else 'OPTION_2') if base=='A' else ('OPTION_2' if orientation=='AB' else 'OPTION_1')) if base else None
        key={'item_id':opaque,'original_prompt_id':orig_id,'pair_id':pid,'pair_kind':kind,'orientation':orientation,
             'case_id':o.get('case_id',o.get('base_case')),'source_label':'V17.3_SPEC_EXPECTED_UNADJUDICATED',
             'spec_expected':expected,'preferred_option_if_directional':preferred,
             'evaluation_class':('MANDATORY' if expected in REQUIRED else 'RECOMMENDED' if expected in RECOMMENDED else expected)}
        # all read-only structural pass results for each prompt, zero model inferences
        status='PASS' if (q['table_rows']==o['source_rows'] and q['option_1']==normopt(srcp['option_1']) and q['option_2']==normopt(srcp['option_2'])) else 'FAIL'
        cues=['dù ','bị ','sai ','không được','cấm ','trái ','tự ý ','mất ','che ','khó đọc','đọc tốt','không phù hợp','vi phạm','tối ưu','quá ']
        normtext=(q['option_1']+' '+q['option_2']).lower()
        cue_hits=sorted({c.strip() for c in cues if c in normtext})
        # descriptive cues can make answer guessable without a real measurement.
        struct.append({'item_id':opaque,'source_prompt_id':orig_id,'operation':'STRUCTURAL_ONLY_NO_MODEL_CALL',
                       'table_content_preserved':q['table_rows']==o['source_rows'],
                       'option_mapping_correct':status=='PASS',
                       'font_in_range':q['font_family']=='Times New Roman' and q['font_size_pt'] in (13,14),
                       'answer_key_not_in_prompt':all(s not in q for s in ('expected','spec_expected','pair_id','orientation')),
                       'semantic_cue_risk_flag':bool(cue_hits),'cue_terms':cue_hits,
                       'status':status,'model_response':'NOT_RUN','independent_blind_adjudication':'NOT_OBTAINED'})
        prompts.append(q);secret.append(key)
    prompts.sort(key=lambda v:v['item_id']);secret.sort(key=lambda v:v['item_id']);struct.sort(key=lambda v:v['item_id'])
    check('PUBLIC_PROMPT_NO_ANSWER_KEY',all('spec_expected' not in x and 'orientation' not in x and 'pair_id' not in x and 'case_id' not in x and not re.match(r'^[AB]\s*:',x['option_1']) for x in prompts),'Opaque IDs, no case identity or old A/B prefix')
    check('ALL_128_STRUCTURAL_EXECUTED',len(struct)==128 and all(x['status']=='PASS' for x in struct),'Not model inference')
    check('A_B_SWAP_PRESERVES_WORDING', True, 'Deferred until comparison of paired public prompts')
    # prove swap symmetry using pair key not input IDs
    pm={x['item_id']:x for x in prompts}
    groups=collections.defaultdict(list)
    for k in secret:groups[(k['pair_kind'],k['pair_id'])].append(pm[k['item_id']])
    swap_correct=all(len(v)==2 and v[0]['option_1']==v[1]['option_2'] and v[0]['option_2']==v[1]['option_1'] and v[0]['table_rows']==v[1]['table_rows'] for v in groups.values())
    checks[-1]['status']='PASS' if swap_correct else 'FAIL';checks[-1]['detail']='128 options, 64 paired reverse checks'
    # Verifiable explicit outcome: 128 processed by structural harness, 0 model outputs.
    out=ROOT/'inputs';out.mkdir(exist_ok=True)
    writej(out/'prompts_128_blind_candidate.jsonl',prompts)
    writej(ROOT/'keys'/'spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl',secret)
    writej(ROOT/'results'/'structural_execution_128.jsonl',struct)
    schema=[{'item_id':x['item_id'],'decision':None,'reason':None,'evidence_codes':[],
             'model_id':None,'independent_run_id':None,'response_status':'NOT_RUN'} for x in prompts]
    writej(ROOT/'results'/'MODEL_RESPONSES_NOT_RUN_TEMPLATE.jsonl',schema)
    counts_src=collections.Counter(x['evaluation_class'] for x in secret)
    report={'protocol_version':'V17.4','seed':SEED,'source':'V17.3 local bundle files',
            'structural_checks':checks,'all_structural_checks_pass':all(x['status']=='PASS' for x in checks),
            'source_cases':len(cases),'source_case_font_sizes':{str(k):v for k,v in case_sizes.items()},
            'original_pairs':len(cp)+len(dp),'distinct_case_ids_in_pairs':coverage,
            'prompt_count':len(prompts),'reversed_pairs_checked':len(groups),
            'required_prompt_count':counts_src['MANDATORY'],'recommended_prompt_count':counts_src['RECOMMENDED'],
            'conditional_prompt_count':counts_src['CONDITIONAL'],'abstain_prompt_count':counts_src['ABSTAIN'],
            'model_calls_executed':0,'independent_human_adjudications':0,
            'model_response_status':'BLOCKED_NO_INDEPENDENT_EVALUATOR',
            'valid_blind_validation':'BLOCKED',
            'word_render_run':False,'font_metric_measurement_run':False,
            'cue_risk_prompts':sum(x['semantic_cue_risk_flag'] for x in struct),
            'notes':['Only deterministic structural checks have run on 128; not scored model judgment.',
                     'Opaque ID and removing A/B prefixes do not eliminate evaluative wording inside options.',
                     'Gold labels are V17.3 authored specifications, not independently adjudicated human gold.']}
    (ROOT/'results'/'structural_qa_summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:report[k] for k in ('all_structural_checks_pass','source_cases','original_pairs','prompt_count','required_prompt_count','recommended_prompt_count','conditional_prompt_count','abstain_prompt_count','cue_risk_prompts','model_calls_executed','valid_blind_validation')},ensure_ascii=False,indent=2))
    return 0 if report['all_structural_checks_pass'] else 1

def score(path):
    keys=readj(ROOT/'keys'/'spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl');key_by_id={k['item_id']:k for k in keys}
    rows=readj(Path(path));errors=[];seen=set();indexed={}
    for r in rows:
        i=r.get('item_id');v=r.get('decision')
        if i not in key_by_id:errors.append(f'UNKNOWN_ITEM:{i}');continue
        if i in seen:errors.append(f'DUPLICATE_ITEM:{i}');continue
        seen.add(i)
        if v not in ALLOWED_DECISIONS:errors.append(f'INVALID_DECISION:{i}:{v}');continue
        indexed[i]=r
    counts=collections.Counter()
    detail=[];pair_groups=collections.defaultdict(list)
    for k in keys:
        i=k['item_id'];r=indexed.get(i);cls=k['evaluation_class']
        if not r:continue
        v=r['decision'];flag=None
        if cls=='MANDATORY':flag=(v==k['preferred_option_if_directional']);counts['mandatory_observed']+=1;counts['mandatory_spec_concordant']+=int(flag)
        elif cls=='RECOMMENDED':flag=(v==k['preferred_option_if_directional']);counts['recommended_observed']+=1;counts['recommended_spec_preferred']+=int(flag)
        elif cls=='ABSTAIN':flag=(v=='ABSTAIN');counts['abstain_observed']+=1;counts['abstain_respected']+=int(flag)
        elif cls=='CONDITIONAL':flag=(v in ('CONDITIONAL','ABSTAIN'));counts['conditional_observed']+=1;counts['conditional_caution']+=int(flag)
        canonical=('A' if (v=='OPTION_1' and k['orientation']=='AB') or (v=='OPTION_2' and k['orientation']=='BA') else 'B') if v in ('OPTION_1','OPTION_2') else v
        pair_groups[(k['pair_kind'],k['pair_id'])].append(canonical)
        detail.append({'item_id':i,'pair_id':k['pair_id'],'orientation':k['orientation'],
                       'spec_label':k['spec_expected'],'decision':v,'canonical_choice':canonical,'spec_concordant_or_cautious':flag,
                       'answer_status':'V17.3_SPEC_NOT_INDEPENDENT_GOLD'})
    n_pairs=sum(len(v)==2 for v in pair_groups.values());n_stable=sum(len(v)==2 and v[0]==v[1] for v in pair_groups.values())
    complete=(len(indexed)==128 and n_pairs==64 and not errors)
    report={'status':'SPEC_CONCORDANCE_ONLY_NOT_VALIDATED_ACCURACY' if indexed else 'NOT_RUN',
            'responses_received':len(indexed),'expected_responses':128,'complete':complete,
            'paired_reversals_with_both_responses':n_pairs,'paired_order_consistent':n_stable,
            'counts':dict(counts),'scoring_errors':errors,
            'warnings':['The score is against V17.3 authored SPEC labels, not independent adjudicated gold.',
                        'Order consistency is not correctness. Two repeated ABSTAIN responses can be stable but miss a mandatory violation.',
                        'Original option descriptions leak quality cues; a human blind rewrite/adjudication is required.',
                        'No pass threshold is claimed; compute and report denominators.']}
    writej(ROOT/'results'/'scored_responses_detailed.jsonl',detail)
    (ROOT/'results'/'score_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if not errors else 2

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('command',choices=['build','score']);ap.add_argument('--responses',help='JSONL from independently executed model responses')
    args=ap.parse_args()
    if args.command=='score' and not args.responses:ap.error('score requires --responses')
    sys.exit(build() if args.command=='build' else score(args.responses))
