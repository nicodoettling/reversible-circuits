"""Nonauthor targeted production-bit/memo/one-counter checks for I2-D.v1."""
from collections import Counter
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
import argparse,gc,hashlib,importlib.util,json,linecache,os,platform,random,sys,time,weakref
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'r2-decoder/exact_sampler-v1.py'
HASH='93d38c75d25446dc7287cd65ea0ec4f05c5f3855fe96b3ee26fe6a9444bb33a0'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==HASH
spec=importlib.util.spec_from_file_location('r6_i2_frozen',SOURCE)
s=importlib.util.module_from_spec(spec);sys.modules[spec.name]=s;spec.loader.exec_module(s)

class Bits:
    # Deliberately NO exact_index: every tested call takes production branches.
    def __init__(self,items):self.items=list(items);self.calls=[]
    def getrandbits(self,bits):
        want,value=self.items.pop(0)
        assert bits==want and 0<=value<(1<<bits)
        self.calls.append((bits,value))
        return value

def bit_checks():
    cases=[];calls=0
    for bound in range(1,66):
        bits=(bound-1).bit_length();total=1<<bits
        rejects=list(range(bound,total))
        for accepted in range(bound):
            supplied=[] if bound==1 else [(bits,x) for x in rejects]+[(bits,accepted)]
            rng=Bits(supplied)
            assert s.qc.randbelow(rng,bound)==accepted and not rng.items
            assert len(rng.calls)==(0 if bound==1 else len(rejects)+1)
            calls+=len(rng.calls)
        # Exact finite geometric partial laws, with the remainder explicit.
        rejection=F(total-bound,total)
        truncated=sum(rejection**j/F(total) for j in range(8))
        assert truncated==F(1,bound)*(1-rejection**8)
        assert rejection<F(1,2)
        cases.append({'bound':bound,'width':bits,'rejected_candidates':len(rejects),
                      'truncated_mass_per_output_8_trials':str(truncated),
                      'remaining_mass':str(rejection**8)})
    patterns=[(1,),(0,1,0),(1,2),(0,3,0,2,0),(2,0,5,1),(0,0,4)]
    tickets=0
    for weights in patterns:
        total=sum(weights);bits=(total-1).bit_length()
        for ticket in range(total):
            expected=next(i for i in range(len(weights)) if ticket<sum(weights[:i+1]))
            supplied=[] if total==1 else [(bits,ticket)]
            rng=Bits(supplied)
            assert s.qc.weighted_index(rng,weights)==expected and not rng.items
            tickets+=1
    for weights in ((),(0,0),(-1,2)):
        try:s.qc.weighted_index(Bits([]),weights)
        except ValueError:pass
        else:raise AssertionError('invalid categorical weights accepted')
    for bound in (0,-1):
        try:s.qc.randbelow(Bits([]),bound)
        except ValueError:pass
        else:raise AssertionError('nonpositive bound accepted')
    return {'integer_cases':cases,'actual_getrandbits_calls':calls,
            'categorical_patterns':[list(x) for x in patterns],'categorical_tickets':tickets,
            'nonpositive_and_negative_rejected':True,'audit_exact_index_used':False}

def memo_checks():
    memo=s.LinearMemo();q=(3,((1,),(2,)))
    memo[q]=0;memo[tuple([3,tuple([(1,),(2,)])])]=7
    assert len(memo)==1 and q in memo and memo[q]==7
    assert (0,((3,),)) not in memo
    try:memo[(0,((3,),))]
    except KeyError:pass
    else:raise AssertionError('missing key accepted')
    rows=[];code=s.qc.QuotientCounter.count.__code__
    for v in range(2,7):
        for g in range(3):
            ell=2*v-2+2*g;counter=s.SelectedCounter(v);expansions=Counter()
            def trace(frame,event,arg):
                if frame.f_code is code and event=='line':
                    if linecache.getline(frame.f_code.co_filename,frame.f_lineno).strip()=='tasks.append((key, True))':
                        expansions[frame.f_locals['key']]+=1
                return trace
            previous=sys.gettrace();sys.settrace(trace)
            try:
                value=counter.connected_count(ell)
                word=counter.sample(ell,random.Random(1729))
            finally:sys.settrace(previous)
            assert expansions and max(expansions.values())==1
            assert all(key in counter.cache for key in expansions)
            assert value==s.qc.counts.connected_counts(v,ell)[v][ell]
            p=list(range(v))
            for a,b in word:p[a],p[b]=p[b],p[a]
            assert p==list(range(v)) and len(word)==ell
            metric=counter.metrics(ell)
            assert metric['count_keys']<=metric['remaining_length_key_bound']
            assert metric['transition_states']<=metric['state_bound']
            rows.append({'v':v,'ell':ell,'genus':g,'count':value,'distinct_expansions':len(expansions),
                         'max_expansions_per_key':max(expansions.values()),'metrics':metric})
    return {'replacement_preserves_single_key':True,'missing_getitem_rejects':True,
            'trace_changes_no_recurrence_or_branches':True,'validity_seed':1729,'rows':rows}

def disposal_checks():
    prepared=s.PreparedExact(5,4)
    macro=(s.MacroComponent((1,2),(0,2)),s.MacroComponent((3,4),(1,3)),s.MacroComponent((5,),()))
    refs=[];events=[];original=s.SelectedCounter
    def factory(v):
        gc.collect();assert all(ref() is None for ref in refs)
        obj=original(v);refs.append(weakref.ref(obj));events.append(v);return obj
    s.SelectedCounter=factory
    try:word=prepared.decode_macro(macro,Bits([]))
    finally:s.SelectedCounter=original
    gc.collect();assert all(ref() is None for ref in refs)
    assert events==[2,2] and word==((1,2),(3,4),(1,2),(3,4))
    assert set(prepared.__dict__)=={'n','m','C','Z'}
    return {'N':5,'m':4,'nontrivial_selected_degrees':events,'isolate_degree':1,
            'counter_absent_before_next_creation':True,'all_counters_released':True,
            'interleaved_output':[list(edge) for edge in word],'production_fair_bits_required':0}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);args=ap.parse_args()
    started=time.perf_counter()
    result={'status':'complete','claim':'I2-D.v1 targeted production-bit, DFS and counter-disposal checks',
            'python':platform.python_version(),'nonstandard_dependencies':[],
            'sampler_sha256':HASH,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'bit_checks':bit_checks(),'memo_checks':memo_checks(),'disposal_checks':disposal_checks()}
    result['elapsed_seconds']=time.perf_counter()-started
    result['generated_utc']=datetime.now(timezone.utc).isoformat()
    temp=args.output.with_name(args.output.name+'.tmp');temp.write_text(json.dumps(result,indent=2)+'\n');os.replace(temp,args.output)
    print(json.dumps({'status':'complete','integer_bounds':65,'memo_cases':15,
                      'repeated_component_disposal':True,'seconds':result['elapsed_seconds']}))
if __name__=='__main__':main()
