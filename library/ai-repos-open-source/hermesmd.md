---
tags:
  - library
title: "hermes.md"
url: "https://hermes-md.com/"
company: [personal]
topics: []
created: 2026-04-14
source_type: raindrop
raindrop_id: 1683867127
source_domain: "hermes-md.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Generate Hermes Agent context from any GitHub repo.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: any github repo, compressedinto a briefingfor hermes agents to clone.

URL Source: https://hermes-md.com/

Markdown Content:
# hermes.md

00%

hermes.md for hermes agents to clone

# a n y g i t h u b r e p o,c o m p r e s s e d i n t o a b r i e f i n g f o r h e r m e s a g e n t s t o c l o n e.

$brief run ↵

// public github repo · private needs GITHUB_TOKEN

fig. 02 · process walk → pack → brief 00%

walk 02.A

100 75 50 25 00

0 N

R02:C01

nodes · depth

traverse the tree

readmes, configs, entry points, and top source files selected by depth and weight. node_modules, dist, binaries dropped at the filter.

pack 02.B

100 75 50 25 00

0 N

R02:C02

tok · f(rank)

pack into 100k

each file capped at 8k tokens. the lowest-priority files truncate first until the context envelope fits.

brief 02.C

100 75 50 25 00

0 N

R02:C03

ln · stream

emit as markdown

streaming, seven sections, imperative voice. stack · architecture · key files · conventions · gotchas · agent instructions.

sample · vercel/next.js

01

02

03

04

05

06

07

08

09

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

32

33

34

35

# next.js

## Stack

- TypeScript · React Server Components · Turbopack

- webpack 5 fallback for production

- swc compiler · rust binaries shipped as @next/swc-*

## Architecture

Monorepo split into packages/. User-facing entry is packages/next/. App Router

lives under packages/next/src/server/app-render/ and reuses React Flight for

streaming SSR. Routing config is generated at build-time from the on-disk

app/ tree.

## Key Files

- packages/next/src/server/next-server.ts — request entry

- packages/next/src/build/index.ts — build orchestration

- packages/next/src/server/app-render/app-render.tsx — RSC pipeline

## Conventions

- Public APIs re-exported from packages/next/index.ts

- Internal modules use relative imports, no path aliases

- Errors throw NextError subclasses, never plain strings

## Gotchas

- TURBOPACK env var swaps bundler at runtime

- pnpm workspace; npm install will not work

- vendored rust binaries land in node_modules/@next/swc-*

## Agent Instructions

Always read packages/next/src/server/next-server.ts before modifying request

handling. Never edit files in packages/next/dist — generated. To add a new

config option, add the type to packages/next/src/server/config-shared.ts and

the runtime parsing to packages/next/src/server/config.ts. Run

`pnpm dev --filter next` from repo root to test changes against the example

apps in test/. Do not bump React versions manually; use scripts/sync-react.js.

streaming 00 / 35

hermes.md · for hermes agents to clone[github ↗](https://github.com/ElizenDevVini/hermes-md)
