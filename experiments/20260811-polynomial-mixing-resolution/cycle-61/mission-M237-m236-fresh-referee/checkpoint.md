# Mission M237 checkpoint

Date: 2026-08-13 (UTC)

Status: initialized before inspecting M236 artifacts.

The project skill has been read.  The mission is locked to a clean-room,
finite `d=7 -> 8` reconstruction.  No M236 code or data will be imported or
executed, and no route/descriptor search or endpoint-derived adaptation will
be performed.  M236 and all predecessors remain immutable.

## Substantive clean-room checkpoint

Fixed before any compatibility-normalization inspection:

```text
M236 SHA256SUMS entries verified                 10 / 10
M236 top inventory digest
  0a1d8fd747051b32ee99a3600fc0b87d9a8b7fa47a08706b6eca032f9e26350a
independent tree constructions equal            yes
root-leaf trees                                  1296
source-extension identities                     1296 / 1296
formal carrier substitutions                     1680 / 1680
initial-run sign cases                             28 / 28
primary rows / passes / failures                 6480 / 6480 / 0
secondary rows / passes / failures               7776 / 7776 / 0
full rows / passes / failures                   14256 / 14256 / 0
Z2 classes by primary edit                       9,6,4,3,2
global Z2 classes                                20
closed rows by primary edit                      864,756,624,463,267
open rows by primary edit                        432,540,672,833,1029
closed / open rows                               2974 / 3506
primary / full distinct formula words            20 / 22
maximum finite primary length                    21
```

The primary length histogram is
`{0:2974,5:1029,9:833,13:672,17:540,21:432}`.  The complete-table
histogram is
`{0:8158,1:1296,2:1296,5:1029,9:833,13:672,17:540,21:432}`.
Both first-failure fields and the first same-Z2 behavior-collision field are
null.

The native clean-room certificate digests fixed at this checkpoint are:

```text
tree universe   6fc1701517198e0121d8100947a43c572bb23448d43915d9c36504596dd8b49c
primary rows    ef5bbc2e29e552bab0734f1ab8383123c2524a77eaa3b08c1281f868f6dcd714
Z2 classes      8efe553652daa54170615ad101633af35e24238d9227a579e3372e6657826905
primary words   64b1027f55b3252a4f41773b6ef450793c21f960c77e6debbbce589672776191
secondary rows  037a2783f128876f09ee4d31c1e5671359f7ceb2ca3d652416b5dbeb3078fa9e
full rows       98ccb3348ca315ab143ba6e3cb932089854516afb43e685b1089c379f2f72204
full words      66f69d75e579754182c0dc5e5c19ed4dad5fea633b7a62131c2a83b7c09edaa1
```

These native hashes intentionally use an independently selected schema; the
mathematical replay and all counts above do not depend on M236 serialization.

## Post-checkpoint compatibility audit

Only after fixing the substantive table and native hashes above, the frozen
M236 serialization block was inspected statically and transcribed into an
isolated compatibility function.  The checker still reads and imports no
M236 file at runtime.  All seven published normalized digests match exactly:

```text
tree universe   4bedab1e9da7ba6dc4c657b1da435da53dc0e3d5114d5678209579774a476ed9
primary rows    f1256098c2b86bf85504979ddb04a9f2c5afb0008c36233051a7e0a0859fdf53
Z2 classes      30adb20d0458fae1829670233e6c0cdfdf599e76b5f39bf4a8f8b71c987bfaa1
primary words   3bca6bd6407aa38e3cdc82c16f527f91fa5bda9ce6c75008bcdf89c3bb810608
secondary rows  f7efdc9be6321543b784c71bffd18af2c2d7ec79adbcf7150867c5cbed5d1868
full rows       114a70ed4fb006b25658a0cf7d49675b20b223b2504b8cca9ec462c31c05acf4
full words      d6fdf8d908fee98bc866ab6201f585f187f3fee8771512ba2e2aa9cf208a821c
```

Two consecutive final runs produced byte-identical `referee_results.json`
with SHA-256
`f2f36b7ba75d9bdf978dd07d0b132183f914551df832a3fd528bd5d7342da037`.
