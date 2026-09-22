#!/usr/bin/env python3
"""Exact feasibility classification of the first finite H0 omission."""
import json,platform,sys,time
import boundary_diagnostics as bd
start=time.monotonic();tested=0;first=None
for n in range(2,129):
    for m in range(0,bd.star(n)+1,2):
        k=bd.d.cutoff(n,m);tested+=1
        excluded=(k<n and m>=2*k+4)
        if excluded and first is None:
            first={'N':n,'m':m,'K':k,'minimal_bad_component_v':k+1,'minimal_bad_component_ell':2*k+4}
result={'claim':'For even m, H0 excludes a word iff K<N and m>=2K+4. Necessity from v>K,g>=2; sufficiency connected support K+1 of length m plus isolates.',
        'domain':'2<=N<=128; all even0<=m<=m_star(N)','tested_pairs':tested,'first_omission':first,
        'seconds':time.monotonic()-start,'command':sys.argv,'python':platform.python_version(),
        'source_hashes':bd.MANIFEST['source_hashes'],'seeds':None}
(bd.HERE/'first-omission-classification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:result[key] for key in ['tested_pairs','first_omission','seconds']},indent=2))
