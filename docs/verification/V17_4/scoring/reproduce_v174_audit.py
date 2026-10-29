#!/usr/bin/env python3
"""Offline post-lock V17.4 scoring, using only Python stdlib.
NO legal/visual or independent-expert validation claims.
Usage: python reproduce_v174_audit.py --results Evaluation_Report_Results.zip \
         --private PRIVATE_Scoring_After_Lock.zip --public Antigravity_Attach_Only.zip
"""
import argparse, collections, hashlib, json, zipfile
from datetime import datetime
from pathlib import Path

def load_jsonl(z, name):
    return [json.loads(s) for s in z.read(name).decode('utf-8').splitlines() if s.strip()]
def sha(data): return hashlib.sha256(data).hexdigest()
def run(results_path,private_path,public_path):
    with zipfile.ZipFile(results_path) as zres,zipfile.ZipFile(private_path) as zkey,zipfile.ZipFile(public_path) as zpub:
        responses=load_jsonl(zres,'responses_128.jsonl')
        logs=load_jsonl(zres,'raw_requests_responses.jsonl')
        keys=load_jsonl(zkey,'keys/spec_answer_key_UNADJUDICATED_KEEP_SEPARATE.jsonl')
        inp=load_jsonl(zpub,'01_EVALUATOR_ONLY/prompts_128_blind_candidate.jsonl')
        manifest=json.loads(zres.read('run_manifest.json'))
        ri={x['item_id']:x for x in responses};li={x['item_id']:x for x in logs};ki={x['item_id']:x for x in keys};pi={x['item_id']:x for x in inp}
        checks={}
        checks['all_four_collections_128']=all(len(x)==128 for x in [responses,logs,keys,inp])
        checks['matching_unique_item_ids']=len(ri)==len(li)==len(ki)==len(pi)==128 and set(ri)==set(li)==set(ki)==set(pi)=={f'TQ{j:04d}' for j in range(1,129)}
        checks['raw_result_and_prompt_matching']=True
        for item in li.values():
            try:
                raw=json.loads(item['raw_response']);body=json.loads(item['raw_request']);prompt=json.loads(body['prompt'].split('Item to evaluate:\n',1)[1]);iid=item['item_id'];r=ri[iid]
                fields=['item_id','decision','reason','evidence_codes','unknown_measurements','uncertainty','response_status']
                if not all(raw.get(f)==item['parsed_result'].get(f)==r.get(f) for f in fields):raise AssertionError('Response mismatch')
                if prompt!=pi[iid]:raise AssertionError('Prompt mismatch')
                start=datetime.fromisoformat(item['timestamp_start']);end=datetime.fromisoformat(item['timestamp_end'])
                if abs((end-start).total_seconds()*1000-item['latency_ms'])>2:raise AssertionError('Latency mismatch')
            except Exception:
                checks['raw_result_and_prompt_matching']=False
                break
        checks['sealed_files_sha256_match']=all(sha(zres.read(x['path']))==x['sha256'] for x in manifest['sealed_artifacts'])
        checks['input_jsonl_sha256_match']=sha(zpub.read('01_EVALUATOR_ONLY/prompts_128_blind_candidate.jsonl'))==manifest['input_sha256']
        checks['public_zip_sha256_match']=sha(Path(public_path).read_bytes())==manifest['source_package_sha256']
        verdicts=collections.defaultdict(collections.Counter);groups=collections.defaultdict(list)
        for k in keys:
            d=ri[k['item_id']]['decision'];c=k['evaluation_class'];p=k.get('preferred_option_if_directional')
            if c in ('MANDATORY','RECOMMENDED'):v=d==p
            elif c=='ABSTAIN':v=d=='ABSTAIN'
            elif c=='CONDITIONAL':v=d in ('CONDITIONAL','ABSTAIN')
            else:raise ValueError('Unexpected class')
            verdicts[c]['total']+=1;verdicts[c]['spec_concordant']+=int(v)
            canonical=('A' if (d=='OPTION_1' and k['orientation']=='AB') or (d=='OPTION_2' and k['orientation']=='BA') else 'B') if d.startswith('OPTION_') else d
            groups[(k['pair_kind'],k['pair_id'])].append((k['orientation'],canonical,k['item_id']))
        consistent=[g for g in groups.values() if len(g)==2 and g[0][1]==g[1][1]]
        inconsistent=[{'pair_kind':kind,'pair_id':pair,'items':g} for (kind,pair),g in groups.items() if len(g)!=2 or g[0][1]!=g[1][1]]
        return {'status':'SPEC_CONCORDANCE_ONLY_NOT_VALIDATED_ACCURACY','checks':checks,'score_by_class':dict(verdicts),
            'reversed_pairs':len(groups),'order_consistent':len(consistent),'order_inconsistent':inconsistent,
            'responses':len(responses),'uncertainty_distribution':dict(collections.Counter(x['uncertainty'] for x in responses)),
            'low_uncertainty_but_measurements_missing':sum(x['uncertainty']=='LOW' and bool(x.get('unknown_measurements')) for x in responses),
            'abstain_class_decisions':dict(collections.Counter(ri[k['item_id']]['decision'] for k in keys if k['evaluation_class']=='ABSTAIN')),
            'classifications':['EXPLORATORY_MODEL_BASED_PILOT','INDEPENDENT_EXPERT_GOLD_NOT_OBTAINED','PROMPT_NEUTRALITY_UNVERIFIED','MODEL_PROVIDER_ID_NOT_EXTERNALLY_ATTESTED']}

if __name__=='__main__':
    a=argparse.ArgumentParser()
    a.add_argument('--results',required=True);a.add_argument('--private',required=True);a.add_argument('--public',required=True);a.add_argument('--output')
    b=a.parse_args();v=run(b.results,b.private,b.public)
    doc=json.dumps(v,ensure_ascii=False,indent=2)+'\n'
    if b.output:Path(b.output).write_text(doc,encoding='utf-8')
    print(doc)