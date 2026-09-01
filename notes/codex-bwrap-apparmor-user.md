# Group-Gated Codex `bwrap`: User Test

The administrator adds `nico` to the `codex-bwrap` group. Group membership
does not propagate into processes that are already running.

After the administrator finishes:

1. Log out of SSH and reconnect.
2. Start a new tmux server; an old tmux server retains the old group list.
3. Run:

```bash
id -nG
command -v bwrap
bwrap --version
codex sandbox /bin/true
echo $?
```

Expected results:

- `id -nG` includes `codex-bwrap`;
- `command -v bwrap` prints `/usr/bin/bwrap`;
- the Codex sandbox command shows no `RTM_NEWADDR` error;
- the final exit status is `0`.

No launcher modification or `aa-exec` wrapper is required.
