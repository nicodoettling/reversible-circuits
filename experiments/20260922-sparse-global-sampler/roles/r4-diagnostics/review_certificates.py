#!/usr/bin/env python3
"""Fresh current-version count comparison against R4 active-support tables."""
from fractions import Fraction
import json
import diagnostics as d
import review_forward as review


def main():
    sampler,digest=review.load_snapshot()
    c=d.connected_counts(16)
    full=d.active_counts(c,16)
    z=d.evaluator(full)
    rows=[]
    for n,m in [(42,12),(82,14),(128,16),(8,12),(6,16)]:
        for policy in ['H0','H1']:
            prepared=sampler.PreparedSampler(n,m,policy=policy)
            k=d.cutoff(n,m)
            allowed=d.active_counts(c,16,lambda v,ell:d.h0_allowed(v,ell,k)
                                    and (policy=='H0' or v<=k))
            a=d.evaluator(allowed)(n,m)
            assert prepared.Z[n][m]==z(n,m) and prepared.A[n][m]==a
            rows.append({'N':n,'m':m,'policy':policy,'K':k,'Z':z(n,m),'A':a,
                         'TV':str(Fraction(z(n,m)-a,z(n,m)))})
    result={'version':'R4-CERT-REVIEW.v1','sampler_sha256':digest,'rows':rows,'passed':True}
    (review.HERE/'review-certificate-results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'passed':True,'rows':len(rows)}))


if __name__=='__main__':
    main()
