# Worker A bounded sandbox smoke report

## Scope

This was an infrastructure smoke test, not a research goal run. All created
artifacts are confined to this assigned worker directory. No elevated access,
network access, external service, installation, machine change, commit, or
push was requested or performed.

## Environment

The recorded sandbox environment reports groups `nico nogroup`, bubblewrap at
`/usr/bin/bwrap`, bubblewrap version `0.9.0`, and Python `3.12.3`. The complete
command/output transcript is in `environment.txt`.

## Workspace and boundary checks

- **Directly verified:** writing `workspace-write-ok.txt` in the assigned
  workspace directory succeeded.
- **Directly verified:** the single required attempt to run
  `touch /home/nico/.codex-bwrap-smoke-forbidden-a` returned exit code `1`
  with a read-only-filesystem error.
- **Directly verified:** after that denial, the outside file did not exist.
  The exit code and stderr are preserved separately in
  `denial-exit-code.txt` and `denial-stderr.txt`.

## Exact finite enumeration

`direct_enumeration.py` represents a permutation as a tuple whose entry at
index `i` is the image of `i`. It uses the right-action product convention:
in `t_1 ... t_m`, apply `t_1` first and proceed left to right, so
`compose(p, q)[i] = q[p[i]]`.

The script constructs every transposition and exhaustively visits every
length-four word with `itertools.product`. It then evaluates each word and
counts those equal to the identity.

- **Exact finite computational result:** `S_3, m=4` has `27` identity words.
- **Exact finite computational result:** `S_4, m=4` has `120` identity words.

Both match the supplied smoke-test pass criteria. These finite counts make no
claim about irreducibility, spectral gaps, asymptotic mixing, or sampler
quality.

## Verdict

**PASS.** Workspace writing worked, the forbidden outside write was denied
and left no file, and both direct-enumeration counts matched the supplied
criteria.
