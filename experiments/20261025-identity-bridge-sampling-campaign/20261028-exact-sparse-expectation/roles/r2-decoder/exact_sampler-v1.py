"""I2-D.v1: unrestricted exact identity bridges, selected-component QC decoding.

The global law is exact for every feasible N,m. Expected polynomial time is a
SEPARATE sparse-regime theorem; rare draws may take exponential time/space.
All nontrivial component tables are built only after the complete macro draw.
Rightmost-first products, canonical labels1..N, explicit words, fair-bit model.
"""
from dataclasses import dataclass
from math import comb
from pathlib import Path
from types import ModuleType
import hashlib
import random
import sys

ROOT=Path(__file__).resolve().parents[5]
QC_SOURCE='experiments/20260922-sparse-boundary/roles/r4-construction/quotient_sampler.py'
QC_HASH='7cfd9bcaed9cc08d57d2e50564b829d8a54cbc40e89aa5fe445a2a5c2149ee7c'


def load_checked_qc():
    path=ROOT/QC_SOURCE
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=QC_HASH:
        raise RuntimeError('frozen quotient dependency hash mismatch')
    module=ModuleType('i2_checked_qc_dependency')
    module.__file__=str(path)
    sys.modules[module.__name__]=module
    exec(compile(raw,str(path),'exec'),module.__dict__)
    return module


qc=load_checked_qc()


class LinearMemo:
    """Deterministic key scans; no expected hash-table performance premise.

    The inherited QC evaluator needs only membership/getitem/setitem. Metrics
    are integer operation counts and do not alter the mathematical recurrence.
    """
    def __init__(self):
        self.keys=[]
        self.values=[]
        self.key_comparisons=0
        self.operations=0

    def _index(self,key):
        self.operations+=1
        for i,old in enumerate(self.keys):
            self.key_comparisons+=1
            if old==key:
                return i
        return -1

    def __contains__(self,key):
        return self._index(key)>=0

    def __getitem__(self,key):
        i=self._index(key)
        if i<0:
            raise KeyError(key)
        return self.values[i]

    def __setitem__(self,key,value):
        i=self._index(key)
        if i<0:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[i]=value

    def __len__(self):
        return len(self.keys)


class SelectedCounter(qc.QuotientCounter):
    def __init__(self,v):
        super().__init__(v)
        self.cache=LinearMemo()
        self.transitions=LinearMemo()

    def metrics(self,length):
        return {
            'degree':self.v,'length':length,
            'count_keys':len(self.cache),'transition_states':len(self.transitions),
            'memo_operations':self.cache.operations+self.transitions.operations,
            'key_comparisons':self.cache.key_comparisons+self.transitions.key_comparisons,
            'maximum_count_bits':max((value.bit_length() for value in self.cache.values),default=0),
            'state_bound':3**(self.v-1),
            'remaining_length_key_bound':(length+1)*3**(self.v-1),
        }


@dataclass(frozen=True)
class MacroComponent:
    labels:tuple
    positions:tuple

    @property
    def degree(self):
        return len(self.labels)

    @property
    def length(self):
        return len(self.positions)


class PreparedExact:
    """Polynomial C/Z preparation only, with no component decoder cache.

    Repeated calls draw independent words when supplied independent fair bits.
    Every call samples all labeled components/position sets first. A local
    quotient counter is then created and released for each selected component.
    """
    def __init__(self,n,m):
        if (not isinstance(n,int) or not isinstance(m,int)
                or n<0 or m<0 or m%2 or (n<2 and m)):
            raise ValueError('requires a feasible nonnegative identity-bridge input')
        self.n,self.m=n,m
        self.C=qc.counts.connected_counts(n,m)
        self.Z=qc.counts.assembly_counts(n,m,self.C)
        if self.Z[n][m]<=0:
            raise ValueError('empty identity bridge')

    def branches(self,n,m):
        choices,weights=[],[]
        for v in range(1,min(n,m//2+1)+1):
            for ell in range(0,m+1,2):
                if self.C[v][ell]:
                    weight=(comb(n-1,v-1)*comb(m,ell)*self.C[v][ell]
                            *self.Z[n-v][m-ell])
                    if weight:
                        choices.append((v,ell));weights.append(weight)
        assert sum(weights)==self.Z[n][m]
        return choices,weights

    def sample_macro(self,rng):
        """Draw the full macro before any exponential component preparation."""
        labels=list(range(1,self.n+1));positions=list(range(self.m));macro=[]
        while labels:
            n,m=len(labels),len(positions)
            choices,weights=self.branches(n,m)
            v,ell=choices[qc.weighted_index(rng,weights)]
            other=qc.unrank_subset(n-1,v-1,qc.randbelow(rng,comb(n-1,v-1)))
            selected_labels=(labels[0],)+tuple(labels[i+1] for i in other)
            selected_indices=qc.unrank_subset(m,ell,qc.randbelow(rng,comb(m,ell)))
            selected_positions=tuple(positions[i] for i in selected_indices)
            macro.append(MacroComponent(selected_labels,selected_positions))
            chosen_labels,chosen_indices=set(selected_labels),set(selected_indices)
            labels=[x for x in labels if x not in chosen_labels]
            positions=[x for i,x in enumerate(positions) if i not in chosen_indices]
        assert not positions
        return tuple(macro)

    def decode_macro(self,macro,rng,collect_metrics=False):
        """Exact independent connected words conditional on a sampled macro.

        No counter survives a component iteration. Optional scalar metrics keep
        no table or counter reference and may be used by exact finite audits.
        """
        result=[None]*self.m;metrics=[]
        for component in macro:
            v,ell=component.degree,component.length
            if v==1:
                if ell:
                    raise ValueError('positive-length singleton in macro')
                continue
            # This is the first creation point for an exponential table.
            counter=SelectedCounter(v)
            if counter.connected_count(ell)!=self.C[v][ell]:
                raise AssertionError('quotient and imported scalar counts disagree')
            local=counter.sample(ell,rng)
            for position,(a,b) in zip(component.positions,local):
                result[position]=(component.labels[a],component.labels[b])
            if collect_metrics:
                metrics.append(counter.metrics(ell))
            del counter
        assert all(edge is not None for edge in result)
        word=tuple(result)
        return (word,tuple(metrics)) if collect_metrics else word

    def sample(self,rng=None):
        rng=random.SystemRandom() if rng is None else rng
        macro=self.sample_macro(rng)
        return self.decode_macro(macro,rng)

    def sample_with_metrics(self,rng=None):
        rng=random.SystemRandom() if rng is None else rng
        macro=self.sample_macro(rng)
        word,metrics=self.decode_macro(macro,rng,True)
        return word,macro,metrics


def sample_identity(n,m,rng=None):
    """One exact unrestricted sample; sparse expected-cost claim is separate."""
    return PreparedExact(n,m).sample(rng)
