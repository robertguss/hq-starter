---
tags:
  - library
title: "CodeSpeak"
url: "https://codespeak.dev/"
company: [personal]
topics: []
created: 2026-03-13
source_type: raindrop
raindrop_id: 1642131884
source_domain: "codespeak.dev"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

A next-generation programming language powered by LLMs that compiles to traditional languages like Python, Go, JavaScript, and TypeScript.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: CodeSpeak: Software Engineering with AI

URL Source: https://codespeak.dev/

Markdown Content:
[![Image 1: CodeSpeak](https://codespeak.dev/_next/image?url=%2Fcodespeak-logo-small.webp&w=384&q=75)](https://codespeak.dev/)

AI Language Built for Humans

## Shrink your codebase

[5-10x](https://codespeak.dev/#case-studies)

CodeSpeak is a next-generation programming language powered by LLMs

Alpha Preview uv tool install codespeak-cli

## Production-grade Systems

Long-term projects,

not just prototypes

## Engineers building complex software

Not vibe-coders

## Teams of Humans

Not just solopreneurs

Communication matters

## Maintain Specs, Not Code

You write a concise spec, `codespeak build` generates code

When you change the spec, `codespeak build` translates

 a diff in the spec → a diff in the code

## See CodeSpeak in action

CodeSpeak works in mixed projects where some code is written manually and some is generated from specs. Here's an example from the [MarkItDown](https://github.com/microsoft/markitdown) repository (forked)

Check out the [step-by-step guide on mixed projects](https://codespeak.dev/docs/getting-started/mixed-mode)

## Turning Code into Specs Coming Soon

CodeSpeak can take over some of the existing code and replace it with specs 5-10x smaller. Maintaining specs is a lot easier for humans.

## Real-World Case Studies

We took real code from open-source projects and generated specs from it. Here's how it panned out:

| Case Study | Code LOC[1] | Spec LOC[1] | Shrink Factor | Tests Passed |
| --- | --- | --- | --- | --- |
| WebVTT subtitles support for yt-dlp (video downloader) [View spec & code](https://codespeak.dev/shrink-factor/yt-dlp-webvtt) | 255 | 38 | 6.7 x | before: 1241/1242 after: 1278/1279 ( 37 tests added) |
| Italian SSN generator for Faker (python library for generating mock data) [View spec & code](https://codespeak.dev/shrink-factor/faker-ssn-italy) | 165[2] | 21 | 7.9 x | before: 2216 after: 2229 ( 13 tests added) |
| Encoding auto-detection and normalization for beautifulsoup4 (Python library for parsing HTML and XML) [View spec & code](https://codespeak.dev/shrink-factor/beautifulsoup4-dammit) | 826 | 141 | 5.9 x | before: 889 after: 914 ( 25 tests added) |
| EML to .md converter for markitdown (Python library for converting anything to markdown) [View spec & code](https://codespeak.dev/shrink-factor/markitdown-eml) | 139 | 14 | 9.9 x | before: 165 after: 192 ( 27 tests added) |

[1] When computing LOC, we strip blank lines and break long lines into many

[2] List of Italian municipalities codes (~8000 LOC) is excluded
