# Force & Initiative

**Design and tooling only. No playable release exists yet.**

Solo tactical combat in Star Wars: Knights of the Old Republic II, controlling
the protagonist and companions. Individual turns provide movement, an action,
a bonus action and a reaction. Selected real BG3 spell definitions are to be
read from the player's BG3 installation and adapted as Force powers.

KOTOR II is the required primary game; BG3 is the required companion. No game
content, including community mods, is redistributed or copied between games.
Star Wars 5e is a design reference only; its text and data are not bundled.

The initial slice is one isolated combat encounter using the player's existing
KOTOR II scene and party. In its first minute the player sees initiative, moves
one party member, casts a Force power and ends that character's turn. Planned
powers: a ranged Force strike, a short reposition and a defensive reaction.
Exact BG3 spell identities and numerical rules await inspection of installed
data; do not substitute invented BG3 definitions.

## Development

Python 3.10+; no third-party Python dependencies.

```
python -m unittest discover -s tests -v
python tools/preflight.py
python tools/generate.py
```

Preflight reports every missing or unverified sheet cell and unresolved link.
Generation is blocked until all cells have evidence. Successful tooling tests
do not validate gameplay. Generated output consists of one immutable record
per sheet row, never manually edited.

## Integration status

KOTOR II uses the native Odyssey engine and NWScript. Investigating native
script/event integration first: Melty installs no KOTOR II loader. Public
NWScript function names alone do not prove control of movement, enemy turns,
camera or reactions. No hook addresses or game versions have been guessed.

BG3 uses Larian's engine and PAK data; LSLib is a candidate read-only archive
reader. The final program must read selected entries in place, without
extracting game content into KOTOR II or uploading it.

This cloud machine has neither installed game nor a Windows/WSL connection
to the player's PC. Engine hooks, PAK reads, combat, installation and gameplay
capture remain unverified. No install recipe or release archive is ready.

## License and credits

Original project code: MIT, remix permitted. Game content remains under its
respective owners' rights. Built with AI assistance. Research tools: Universal
Modder by rehan-remade and contributors; xoreos-tools by its contributors.
Neither tool nor a third-party runtime is bundled. Full third-party licensing
must be reviewed before packaging any runtime.
