# Early decoder checkpoint —2026-10-28 12:00UTC

Source intake complete. QC.v1 gives actual all-genus connected decoder with at most3^(v-1) quotient states. Proposed implementation imports the hash-verified frozen decoder and replaces its memo/transition storage with explicit deterministic linear-scan maps. It prepares only polynomial unrestricted C/Z, samples full macro first, and discards every selected component counter after use. Thus no rare-component cost is hidden in preparation.

Base9 follows by squaring Q<=(ell+1)3^(v-1) under linear lookup scans. A loose P^12 per-component conditional expected bit-time envelope and P^8*3^v storage envelope are being pinned with full accounting. Exact fair-bit rejection does not have a deterministic time bound; deterministic table/structural work and conditional expected random cost will be distinguished. No mathematical job has run.
