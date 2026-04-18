---
tags:
  - library
title: "fast.ai - How To Use AI for the Ancient Art of Close Reading"
url: "https://www.fast.ai/posts/2026-01-21-reading-LLMs/"
company: [personal]
topics: []
created: 2026-03-09
source_type: raindrop
raindrop_id: 1636076369
source_domain: "fast.ai"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Experiments in reading with LLMs

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: fast.ai - How To Use AI for the Ancient Art of Close Reading

URL Source: https://www.fast.ai/posts/2026-01-21-reading-LLMs/

Markdown Content:
## The Ancient Art of Close Reading[](https://www.fast.ai/posts/2026-01-21-reading-LLMs/#the-ancient-art-of-close-reading)

[Close reading](https://classicswrites.hsites.harvard.edu/close-reading-0) is a technique for careful analysis of a piece of writing, paying close attention to the exact language, structure, and content of the text. As [Eric Ries described it](https://www.youtube.com/watch?v=zIqLuuyxgE4),“_close reading is one of our civilization’s oldest and most powerful technologies for trying to communicate the gestalt of a thing, the overall holistic understanding of it more than just what can be communicated in language because language is so limited._” It was (and in some cases still is) practiced by many ancient cultures and major religions.

Some [scholars describe](https://classicswrites.hsites.harvard.edu/close-reading-0) close reading as “‘reading out of’ a text rather than ‘reading into’ it”, referring to the importance of making outward connections to broader context. LLMs can provide a useful tool for identifying these outward connections.

It might come as a surprise that a technique associated with such a long history could now see a revival with the use of Large Language Models (LLMs). With an LLM, you can pause after a paragraph to ask clarifying questions, such as ‘What does this term mean?’ or ‘How does this connect to what came before?’

## Two Examples of Reading with an LLM[](https://www.fast.ai/posts/2026-01-21-reading-LLMs/#two-examples-of-reading-with-an-llm)

Watching the videos below will give you the clearest examples of how reading with an LLM can work. However, I will do my best to summarize our findings below. The videos are excerpts from the most recent fast.ai course, [How to Solve It With Code](https://solve.it.com/).

Jeremy read an early version of Eric Ries’s new book, [Incorruptible](https://www.simonandschuster.com/books/Incorruptible/Eric-Ries/9798893311860). He discusses his approach to Eric, demonstrating how he managed context, sharing his discoveries, and they both reflect on the experience.

A second demo looks not at a book, but at a dense academic paper. Johno Whitaker used a cutting-edge paper from Yann LeCun ([LeJEPA](https://arxiv.org/abs/2511.08544)) as an example. He walks through how he prepares his workspace, investigates both math and code from the paper, and creates a simple visual interaction in order to build intuition.

## Benefits of Close Reading with an LLM[](https://www.fast.ai/posts/2026-01-21-reading-LLMs/#benefits-of-close-reading-with-an-llm)

Here are a few examples from Jeremy’s experiences that stood out to me as benefits of reading with an LLM: he was able to go down rabbit holes of interest, ask clarifying questions, and personalize the material.

One chapter of Eric’s book discusses a disastrous CEO who moved from 3M to Boeing, causing problems at both companies with his focus on cost-cutting. He won “CEO of the Year”, yet oversaw the development of the Boeing 737 MAX, which later experienced fatal crashes. Jeremy was intrigued and searched for more information, discovering that this CEO was one of 13 unsuccessful mentees of Jack Welch. In a series of follow-up questions with the LLM, he learned that 4 of these 13 mentees served as CEOs at Boeing during its period of safety scandals and decline!

When Jeremy was confused about a concept, he asked for more background explanation. At one point, he was skeptical of Eric’s thesis and sought out counterexamples. Jeremy asked the LLM to personalize principles from the book by applying them to the governing structure of Answer.ai. These are all questions LLMs can be well-suited for.

To retain new information you learn as you read, [spaced repetition](https://en.wikipedia.org/wiki/Spaced_repetition) is a useful technique, often implemented with [Anki flashcards](https://rachel.fast.ai/posts/2023-02-21-anki/). The [fastanki library](https://answerdotai.github.io/fastanki/) provides a way to create new Anki cards within a reading dialog. You can read, write, and sync to the same Anki deck you use on your phone and desktop computer, so you’ll be able to study the cards later at your convenience.

At the end of the chapter, Jeremy generated a summary of the dialog (including his own questions and rabbit holes) that would be useful context for the LLM when he started the next chapter. Reflecting on the experience, Jeremy was enthusiastic, “_This is one of the absolute best reading experiences I’ve ever had!_” Eric found it rewarding to see a reader so actively engaged with his book.

## The SolveIt Process[](https://www.fast.ai/posts/2026-01-21-reading-LLMs/#the-solveit-process)

We used the [SolveIt platform](https://solve.it.com/), which combines elements of ChatGPT, Jupyter, Claude Code, and Cursor. SolveIt is designed around the principle of encouraging people to work in small, incremental steps and receive immediate feedback. The goal is to not just figure out answers, but to develop a deeper understanding of the problem.

Here is an overview of the process that Jeremy followed for reading:

1.   Convert PDFs to Markdown (a simple text format that can be easily read by LLMs)
2.   Generate summaries of each chapter to use as context for the LLM
3.   Instruct the LLM not to give spoilers
4.   The reader asks questions as they read through the full text of the book
5.   At the end of each chapter, generate overviews of the conversation between the reader and the LLM to share as further context for the next chapter
6.   Optional: have the LLM ask questions to check the reader’s understanding
7.   Optional: create Anki cards within reading dialogs using [fastanki](https://answerdotai.github.io/fastanki/)

## Obstacles to Reading with an LLM[](https://www.fast.ai/posts/2026-01-21-reading-LLMs/#obstacles-to-reading-with-an-llm)

It is early days of building the tools for close reading with an LLM. The process for creating chapter summaries to provide as context to the LLM is somewhat clunky. The SolveIt PDF-to-markdown and Anki integration tools currently require coding ability to set up. We are working to further streamline this process to make it easier to use.

A concern when working with LLMs is that they generate plausible-sounding text that can be factually incorrect, a problem known as hallucination. Jeremy and Johno did not encounter this issue, most likely because their approach took advantage of grounding (when the answers to questions are present in the LLM’s context) and of having the LLM make use of external web searches.

## A Work in Progress[](https://www.fast.ai/posts/2026-01-21-reading-LLMs/#a-work-in-progress)

Hopefully, the above ideas and videos provide inspiration of how LLMs could be used in your reading. One key finding from both Jeremy and Johno was about the value of setting up the context of their environments beforehand. “_It’s like the architect sharpening his pencils or Jeremy like preparing his canvas. And then the next time you go there, your desk’s all set up. You know, you’ve got all those pieces. And that little investment up front makes it a very different tool to the vanilla case,_” Johno described this preparation.

The videos included above are excerpts from Lesson 9 of the fast.ai How to Solve It With Code course. The full course covered how to use AI **not** to outsource your thinking, but rather to deepen your understanding and problem solving skills. It covered a wide range of topics: building your own AI agent, web development, remote server management, classic algorithms, and more. You can find out more about the course and how to sign up [here](https://solve.it.com/).

_Thank you to Eric, Rens, and Jeremy for feedback on earlier drafts of this post._
