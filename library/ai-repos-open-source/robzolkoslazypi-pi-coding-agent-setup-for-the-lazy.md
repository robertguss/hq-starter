---
tags:
  - library
title: "robzolkos/LazyPi: Pi coding agent setup for the lazy"
url: "https://github.com/robzolkos/lazypi"
company: [personal]
topics: []
created: 2026-04-20
source_type: raindrop
raindrop_id: 1690570563
source_domain: "github.com"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: github-api
---
## Excerpt

Pi coding agent setup for the lazy

## Raw Content

<!-- Hydrated 2026-04-20 via github-api -->

# LazyPi

The [Pi](https://github.com/badlogic/pi-mono) coding agent is minimal by design. LazyPi is opinionated by design. Run one command and get a complete, curated Pi setup — everything selected by default, nothing to research, nothing to configure. Remove what you don't want later.

## Quick start

```bash
npx @robzolkos/lazypi
```

LazyPi will:

1. Install `pi` for you if it isn't installed yet.
2. Ask if you want to install all the packages or choose which to install.

That's it.  Once done - run `pi` and experience a feature rich coding agent experience.

Install is **idempotent** — LazyPi reads your Pi settings and skips any package that is already installed, so re-running is safe.

For theme packages, LazyPi also applies a small Pi package filter so duplicate theme IDs do not collide. It keeps both `pi-themes` and `@victor-software-house/pi-curated-themes` installed, but excludes `catppuccin-mocha` and `gruvbox-dark` from `pi-themes` so those two come from the curated themes package.

## Commands

| Command | What it does |
| --- | --- |
| `npx @robzolkos/lazypi` | Install all or selected catalog (interactive picker by default) |
| `npx @robzolkos/lazypi remove <id>` | Remove a catalog package by id (or pass a raw pi source) |
| `npx @robzolkos/lazypi status` | Show which catalog packages are installed, missing, or extra |
| `npx @robzolkos/lazypi update` | Reconcile the catalog and then run `pi update` |
| `npx @robzolkos/lazypi doctor` | Check your environment for common problems |

## Updating

```bash
npx @robzolkos/lazypi update
```

## Removing packages

```bash
npx @robzolkos/lazypi remove
```

Shows an interactive picker of installed packages. Or pass ids directly to skip the picker:

```bash
npx @robzolkos/lazypi remove subagents
npx @robzolkos/lazypi remove npm:pi-subagents@0.13.3   # raw pi source also works
```

There is nothing to "uninstall" for LazyPi itself — `npx` doesn't leave it around.

## Troubleshooting

Run the built-in health check (`npx @robzolkos/lazypi doctor`).

---

For the full list of included packages and themes, see [lazypi.org](https://lazypi.org).
