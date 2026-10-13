# Force & Initiative — development journal

## Agreed design

KOTOR II remains primary. BG3 is a required companion supplying real spell
definitions from the player's copy. Solo, protagonist and companions under
player control, individual movement/action/bonus-action/reaction turns.
Original code MIT, remix allowed. No assets, definitions or community mod
content copied out of either game. Existing window arrangement must remain.

## Research and current evidence

- Melty API reachable after adding melty.gg to the environment network draft.
- list_my_mods initially empty; search_games confirms both catalog slugs.
- game_info: no KOTOR II automatic loader; plain native resources or a genuine
  own-copy engine replacement are possible publication routes. BG3SE v32 is
  automatic for BG3, but is not a KOTOR II loader.
- search_mashups found no exact pair. Read wizardcraft's live recipe as an
  example of passing BG3's installed directory through an environment variable.
  Its Minecraft host is not substituted for our KOTOR II host.
- Universal Modder cloned to /workspace/universal-modder. Its mod-any-game
  skill read. Run with UV_CACHE_DIR=/workspace/.cache/uv. No paid tools used.
- `um scan --list`: no Steam/Epic/Xbox installations found. `um win ps` confirms
  this machine is Linux without the Windows/WSL automation route.
- xoreos-tools cloned to /workspace/tools/xoreos-tools for public NWScript
  interface research. src/nwscript/game_kotor2.h names PauseGame,
  SetCommandable, ActionMoveToLocation and SetPartyAIStyle. These names are
  research leads, not verified runtime hooks or signatures.
- Official reone README describes an Odyssey engine rewrite accepting
  `reone --game GAME_DIR`, but game mechanics are still in development.
  Not adopted as a working or compatible replacement.
- Official Norbyte/lslib README confirms PAK tooling. No reader runtime is
  bundled, no archive extracted, no game code inspected without game access.

## Route and validation

Investigate native NWScript scripts/event integration first. Do not claim
global pause supports active-actor-only simulation. Reactions and movement
require runtime verification. If native integration cannot meet the design,
explain the concrete obstacle and obtain agreement before altering it.

Four JSON sheets record games, hooks, systems and powers. Every cell includes
value, verified state and evidence. All unresolved game-dependent cells remain
explicit. Preflight reports 35 findings; no unresolved foreign keys.
Generator refuses to produce any release code until preflight is clean.
Six tooling tests passed. No game, install or release test has run.

## Melty draft

modId: 3bf37660-7652-4868-a4e4-7205c42d1708

Studio: https://melty.gg/studio/3bf37660-7652-4868-a4e4-7205c42d1708

Linked repo: farinhaque10-max/Melty. Remix explicitly enabled. No uploads,
release, media, recipe, commit, push or publication performed.

## Resume on the game PC

Use this checkout directly; no new worktree. Reuse the above modId.
Connect an agent session on the PC with both installed games and Melty open.
Discover Steam/GOG libraries and inspect installed versions automatically.
Read only selected source spell entries in place. Verify script events, camera,
key bindings and actor simulation. Back up saves/config before modded launch.
Update sheet evidence before generating or building. All final runtime
dependencies must be redistributable and bundled unless Melty installs them.
Test the real encounter, obtain game-only media, validate a complete recipe
and one-click behavior, then test two Melty install/play runs. Ask to publish
only after those checks pass. Never put the agent token in project files.
