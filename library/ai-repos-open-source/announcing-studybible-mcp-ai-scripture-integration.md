---
tags:
  - library
title: "Announcing StudyBible MCP: AI + Scripture Integration"
url: "https://viz.bible/announcing-study-bible-mcp-ai-scripture-integration/"
company: [personal]
topics: []
created: 2026-03-27
source_type: raindrop
raindrop_id: 1660789080
source_domain: "viz.bible"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

A new AI integration serves data-oriented answers to biblical questions trained on solid hermeneutical methods. Unlike other solutions, this one aims to reach people where they are instead of building a stand-alone “walled garden.”

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Announcing StudyBible MCP: AI + Scripture Integration

URL Source: https://viz.bible/announcing-study-bible-mcp-ai-scripture-integration/

Markdown Content:
imageTitle

imageCaption

date

Mar 25, 2026

description

A new AI integration serves data-oriented answers to biblical questions trained on solid hermeneutical methods. Unlike other solutions, this one aims to reach people where they are instead of building a stand-alone “walled garden.”

publish

publish

imageLink

image

[![Image 1: e839a42c-83b9-4213-8a92-7052d714af6b.jpg](https://www.notion.so/image/attachment%3A06bd2d5c-660d-4b84-8424-537756222b27%3Ae839a42c-83b9-4213-8a92-7052d714af6b.jpg?table=block&id=32e4a2f0-3514-8028-a8b8-f5093c3f6c49&cache=v2)](https://www.notion.so/image/attachment%3A06bd2d5c-660d-4b84-8424-537756222b27%3Ae839a42c-83b9-4213-8a92-7052d714af6b.jpg?table=block&id=32e4a2f0-3514-8028-a8b8-f5093c3f6c49&cache=v2)

_Editor’s note: This is a guest post by a professional acquaintance who is an entrepreneurial leader in AI and data analytics. The solution he describes below is an exciting innovation for injecting trustworthy biblical data within the tools people increasingly use to answer deep personal and spiritual questions._

### [](https://viz.bible/announcing-study-bible-mcp-ai-scripture-integration/#32e4a2f0351480b2b917e6910b8dddcd "Meet people where they are")**Meet people where they are**

Hi! My name is David Jayatillake, I'm a Christian and co-founder at a startup called [Quarri.ai](https://quarri.ai/).

I believe that tools like ChatGPT and Claude will be the future of how people will interact with computers (including smartphones and tablets). Rather than making a new app or website for people to go to, why not meet them where they are? It's the same principle we have had with Quarri: if Claude is the operating system of the future for enterprise, let's not fight them to go elsewhere, let's give them all the tools they need right here.

Using Claude Code, I have architected a free and open-source Study Bible MCP that plugs into any agent that supports MCP, including Claude, ChatGPT, Mistral, and others. It requires no installation, just entering the URL for the MCP server as a custom connector in settings. See the video below for how to do that in Claude Desktop. It centres around a 600MB SQLite database that is free to take (see the link in the code repository README below). The Bible is the biggest literary work of all time in stature but isn't that large in file size!

For the longest time since I became established in my career, I have asked God in prayer what I could or should do with my talents for his kingdom. For reference, my skillset lies in software and data engineering and architecture; I am CTO at Quarri. It wasn't clear to me for many years.

I started working on Quarri last summer and, using the power of tools like Claude Code, managed to build a full-stack SaaS application that did everything I wanted in my previous startups and more. I even built my own agent within it to perform complex data analysis.

Then the world changed overnight. With the release of Claude Opus 4.5 and Claude Desktop with MCP apps, the world realised that standalone SaaS applications were the past and empowering a frontier agent with the right tools to do any task was the future. Instead of having many small walled gardens of SaaS apps, you give a very powerful agent tools to use all of those SaaS apps alone and in combination. The ramifications of this have been felt broadly with SaaS stock valuations largely plummeting as a result. I followed suit and have largely abandoned the SaaS app for Quarri in favour of a set of tools for use via MCP, and the results were excellent; it provided a much improved and more powerful customer experience.

It was also about this time that I started to use agents more in my Bible study. Initially I started using ChatGPT to look up and research passages from the Bible, but soon after Opus 4.5 came out I switched to using Claude and it was even better. My concern with using Claude or ChatGPT, raw, for Bible study was the lack of constraint. My lessons from using an agent to query data were to give it rich sources of context to consume at will and constraint to tell it how to do something the right way. This was when I had the idea to build an MCP server for agents that provided them with method and content to perform rich Bible study. Initially I didn't know exactly what to include, but I have had help from Robert (who runs this site), and others at the Missional AI and FaithTech communities to find new resources to include. Claude Code was incredibly useful here too and found the STEPBible resources from Tyndale House, Cambridge that I started with.

Today the server includes the full[Liddell-Scott-Jones Greek lexicon](https://github.com/STEPBible/STEPBible-Data)(10,846 entries — the standard reference used by classical scholars for over 150 years); the full unabridged[Brown-Driver-Briggs Hebrew lexicon](https://github.com/eliranwong/unabridged-BDB-Hebrew-lexicon)(8,090 entries — the standard since 1906);[Abbott-Smith's Manual Greek Lexicon of the New Testament](https://github.com/translatable-exegetical-tools/Abbott-Smith)(5,896 entries with LXX cross-references and synonym discussions); morphologically tagged texts for every word in the Greek New Testament and Hebrew Old Testament from[Tyndale House](https://github.com/STEPBible/STEPBible-Data); the[Aquifer Open Study Notes](https://github.com/BibleAquifer/AquiferOpenStudyNotes)providing verse-level scholarly commentary across all 66 books; the[Tyndale Bible Dictionary](https://github.com/BibleAquifer/AquiferOpenBibleDictionary)with 500+ topical articles;[unfoldingWord](https://github.com/BibleAquifer/UWTranslationNotes)and[SIL](https://github.com/BibleAquifer/SILOpenTranslatorsNotes)translation notes; 200+[key theological term definitions](https://github.com/BibleAquifer/FIAKeyTerms); the[ACAI entity annotations](https://github.com/BibleAquifer/ACAI)covering 3,175 people, places, groups, and key terms with their relationships; the[Theographic Bible](https://github.com/robertrouse/theographic-bible-metadata)genealogy and event graph data; 87 structured Ancient Near East cultural context entries across 12 dimensions of life and 9 historical periods sourced from Walton, Hallo, Pritchard, and other standard ANE reference works; and semantic vector embeddings for all 31,280 verses enabling discovery of thematic connections across the entire canon. In all, the database contains over 200,000 rows of scholarly content.

The server exposes 18 tools to the agent. Verse lookup with the original Greek and Hebrew text and word-by-word analysis. Deep word studies pulling from the full LSJ, BDB, and Abbott-Smith lexicons — not brief glosses, but the complete scholarly entries. Cross-references and thematic searches. A full genealogy graph that can trace family trees, find the shortest relationship path between any two biblical people, and render Mermaid diagrams. Study notes combining three independent commentary sources. A Bible dictionary with 500+ articles. Ancient Near East cultural context that covers everything from cosmology and religious practices to legal conventions and daily life, mapped to specific biblical books and time periods. And semantic search using vector embeddings to discover passages that share themes and concepts beyond simple keyword matching.

**But the part I'm most proud of is not the data. It's the method.**

A raw agent with access to the Bible will happily proof-text, allegorise, flatten poetry into doctrine, and ignore genre entirely. The same problems that plague human interpretation. So I embedded a hermeneutical framework based on Gordon Fee and Douglas Stuart's "How to Read the Bible for All Its Worth" - the standard textbook for biblical hermeneutics used in seminaries worldwide. The server teaches the agent to identify genre, consider historical and literary context, respect authorial intent, and acknowledge uncertainty. It has specific guidance for epistles, narratives, gospels, parables, prophets, psalms, wisdom literature, and apocalyptic. The agent follows a seven-step reasoning pattern: identify the text, determine genre, establish context, examine content in the original languages, check cross-references, derive application, and practice humility where honest scholars disagree.

The constraint is the product. Without it, you just have a very fast concordance. With it, you have a study companion that reasons about Scripture the way a well-trained seminary student would.

I have so enjoyed using it for my personal study and use it multiple times a day. Folks I have shared it with have told me they feel the same, and I want this to be available to all Christians.

One day soon, we will have an agent as powerful as Claude is today, running locally on a device in our pockets. Perhaps even within a year. These agents will be how people interact with the online world now and in the future. StudyBible MCP brings rich scholarly content for Bible study to any agent.

Here are some example conversations I have had with Claude for my own personal bible study using StudyBible MCP:

*   [Azazel and the devil compared](https://claude.ai/share/95cb0be3-7c60-4438-bb96-e4803663b23a)

*   [Studying the book of Jude](https://claude.ai/share/b2b161a0-747f-498f-9458-75fbed177871)

*   [Jesus' words to Mary from the cross](https://claude.ai/share/5b3236f8-cf20-49c1-8f31-259ecb2a7a6b)

### [](https://viz.bible/announcing-study-bible-mcp-ai-scripture-integration/#32e4a2f0351480ce9eecf2da1c0603a3 "Get Started")**Get Started**

**Claude Desktop**: Settings → Connectors → Add Custom Connector → paste`https://studybible-mcp.fly.dev/sse`

**Claude Code**:`claude mcp add study-bible https://studybible-mcp.fly.dev/sse`

No signup. No API keys. No downloads.

* * *

1.   The STEPBible data from Tyndale House, Cambridge is licensed CC BY 4.0. The BibleAquifer and ACAI data is CC BY-SA 4.0. The BDB and Abbott-Smith lexicons are public domain. The code itself is MIT licensed. All of this is genuinely free and open.

1.   MCP stands for Model Context Protocol. It's an open standard for connecting AI agents to external tools and data sources. Think of it as USB for AI - any agent that speaks the protocol can use any server that implements it.

1.   Fee and Stuart's book was first published in 1981 and is now in its 4th edition. It has sold over a million copies. Gordon Fee (1934-2022) was a New Testament scholar at Regent College and one of the translators of the NIV. Douglas Stuart is an Old Testament scholar at Gordon-Conwell Theological Seminary. Their approach teaches readers to interpret Scripture according to its literary genre, historical context, and authorial intent - avoiding both wooden literalism and uncontrolled allegorising.

1.   If you're a developer and want to contribute, the project is open source. I'd especially welcome additional thematic cross-references, improved genre detection, and new translation support. If you're a biblical scholar who thinks I've got something wrong, I'd welcome that even more.
