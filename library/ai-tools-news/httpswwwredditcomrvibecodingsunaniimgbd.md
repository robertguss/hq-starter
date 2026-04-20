---
tags:
  - library
title: "PSA: Google's Jules is being slept on... it just one-shotted my 900 line prompt to recreate Tumblr"
url: "https://www.reddit.com/r/vibecoding/s/uNanIiMgbD"
company: [personal]
topics: []
created: 2025-05-28
source_type: raindrop
raindrop_id: 1107588609
source_domain: "reddit.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: browser-harness
---

## Raw Content

<!-- Hydrated 2026-04-20 via browser-harness -->

# PSA: Google's Jules is being slept on... it just one-shotted my 900 line prompt to recreate Tumblr

> **r/vibecoding** · posted by u/scragz
> [Link to post](https://www.reddit.com/r/vibecoding/s/uNanIiMgbD)

I've been using it for focused features with great results. But since you only get five tasks a day, I wanted to see just how far you could stretch a single task. a friend asked for help porting their blog off tumblr so I thought this would be a perfect test.

here's my codegen prompt for reference. This is the plan that Jules generated:

1. Init mono-repo
2. Configure TypeScript & linting
3. Wrangler config
4. Hello World Worker
5. Initial schema migration
6. DB utility layer
7. Create Vite React app
8. Routing & Layout
9. zustand stores & fetch client
10. GET endpoints
11. Fetch hooks & PostCard
12. react-virtuoso index
13. Tag pages
14. SSR HTML for single post
15. CSR hydration
16. Utility functions
17. Access JWT middleware
18. Route guard on front-end
19. POST/PUT/DELETE endpoints
20. Wartime DataTable
21. CRUD models & Dropzone
22. Multi-delete & tag ops
23. scripts/imports
24. XML generators
25. Plausible script & hook
26. Logpush + Sentry
27. Vitest setup
28. Playwright scenarios
29. Lighthouse CI budget
30. GitHub Actions
31. Secrets & Pages project
32. Accessibility sweep
33. Final docs & governance
34. Submit the changes

the code is as good as any of these tools is spitting out right now. one cool thing is you can give it corrections mid-loop and it will pick them up and adapt. another is it can spin up a browser session, Manually review key frontend pages (Index, Post, Tag) using browser dev tools accessibility inspectors (e.g., Lighthouse tab, Axe DevTools extension).

I'm super impressed with its instruction-adherence to stick with such a long plan so well. biggest downside is it took almost two hours.

edit:the prompt came from my vibe coding extension kornelius. check it out.

## Top comments

### u/braiker · score 7

Look, not saying OP isn’t being authentic, but this kornelius.dev app (which OP admitted developing) only has 24 installs. Just be cautious yall.

### u/why_is_not_real · score 5

This is very cool. And after 2 hours what had it built? Would love to see the output, both code/repo and a working version

Btw, does Jules provide something of a hosting platform? or does it just work directly on the repo, like connecting to GitHub and just consuming/outputting code?

Thank you

### u/paul_h · score 4

Meanwhile for a seven (or so) sourcefile change to a repo with only some 88 files and 1581 lines of code total, it is now 25 hours into it. It is sure it has not stalled - I've asked a couple of times. I've asked to just stop on the plan, do a commit/push suggesting I'll finish it myself. My ask was to change two tiny source files from Java to Kotlin, and duly work on build scripts to accomodate.

### u/[deleted] · score 2

Commenting to have a gander later. Thanks for this resource.

### u/Bebexy · score 2

How does Jules compare to other code assistants out there like Cursor and Windsurf?

### u/headset38 · score 1

Cool project! Would be super interested in your process to create such a detailed prompt!

### u/MaxAtCheepcode_com · score 1

Would you mind throwing that prompt into CheepCode? You get 5 free tasks with no CC and I’d be very curious to see your results.

### u/ThaisaGuilford · score 1

It's still in beta

### u/telars · score 1

Cool to see so much detail on using cloudflare workers and related projects. As jules can't really spin up a cloudflare workers / pages project or create a D1 database, did you run these steps manually afterwards? How'd it do?

A video walkthrough or some screenshots of the app would be helpful.

### u/samuelalake · score 1

Hi OP, your site has black text on dark background in non dark mode which makes the text hard to read. Kindly fix.

Also, to understand how this works, do users give kornelius a base prompt and it returns a much larger prompt that can be used in Jules? Is it a conversational AI extension for prompt refinement?
