# Group-Gated Codex `bwrap`: Administrator Instructions

## Design

Ubuntu's packaged AppArmor profile grants user-namespace access specifically
to `/usr/bin/bwrap` and strips capabilities from programs launched through
it. A Unix group then controls who may execute that exact binary.

The global setting `kernel.apparmor_restrict_unprivileged_userns=1` remains
enabled. Membership in `codex-bwrap` should therefore be treated as a
security privilege and kept small.

## Install

```bash
sudo apt update
sudo apt install bubblewrap apparmor-profiles apparmor-utils

sudo groupadd --system codex-bwrap
sudo usermod -aG codex-bwrap nico

sudo dpkg-statoverride --update --add \
  root codex-bwrap 0750 /usr/bin/bwrap

sudo install -o root -g root -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict

sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict
```

`dpkg-statoverride` makes the group ownership and `0750` mode survive
package upgrades.

## Verify

```bash
stat -c '%A %U %G %n' /usr/bin/bwrap
sudo dpkg-statoverride --list /usr/bin/bwrap
sudo aa-status | grep bwrap
```

The first command should report approximately:

```text
-rwxr-x--- root codex-bwrap /usr/bin/bwrap
```

That completes the administrator's part. Nico will establish a fresh login
session and run `notes/codex-bwrap-apparmor-user.md`.

References:

- https://learn.chatgpt.com/docs/sandboxing
- https://manpages.debian.org/dpkg-statoverride
