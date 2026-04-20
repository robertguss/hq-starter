---
title: "The Folder Is the Agent"
source: "https://every.to/source-code/the-folder-is-the-agent"
author:
  - "[[Kieran Klaassen]]"
published: 2026-04-13
created: 2026-04-20
description: "I'm running 44 AI agents across multiple projects. Each one is just a model pointed at a folder."
tags:
  - "clippings"
---
*On Friday, April 17,* ***[Cora](https://cora.computer/)*** *general manager* ***[Kieran Klaassen](https://every.to/@kieran_1355)*** *will lead a camp for Every paid subscribers on compound engineering, the AI-native engineering philosophy that he built and that has more than 14,000 stars on GitHub. Since the last camp, Kieran and product leader* ***Trevin Chow*** *have built out product-focused workflows to make the methodology as valuable for product managers and founders as it is for engineers. In this camp, they’ll walk you through what’s new, go deeper on the brainstorm and ideate steps, and share examples of using compound engineering beyond engineering work. [Read the full compound engineering guide](https://every.to/guides/compound-engineering?source=post_button), [install the plugin](https://github.com/EveryInc/compound-engineering-plugin), and [join us for the camp](https://every.to/events/compound-engineering-camp-2).— [Kate Lee](https://every.to/@kate_1767)*

---

I spent three months trying to make [agent swarms](https://chatgpt.com/share/e/69dced68-f6bc-800e-b4c5-af6a134d4737) work.

The idea of multiplying myself by coordinating multiple agents at the same time was a compelling pitch as the sole engineer building Every’s AI email assistant, **[Cora](https://cora.computer/)**. If I could summon a fleet of [AI agents](https://every.to/guides/agent-native), let them coordinate, and watch them produce work no single agent could match, it would relieve some of my overwhelm.

I tried everything to make it work— [Claude Code](https://every.to/source-code/how-i-use-claude-code-to-ship-like-a-team-of-five) teams, agents dispatching tasks to other agents, [orchestration setups](https://every.to/source-code/the-three-ways-i-work-with-llms) where a lead agent managed a pool of workers. Many iterations, many burned tokens.

But more agents didn’t make me faster. I’ve [run parallel Claude Code sessions](https://every.to/source-code/how-i-use-claude-code-to-ship-like-a-team-of-five) for months, which works when each agent has a clear task, and I’m directing the work. The swarm experiment was different: agents coordinating with each other, deciding what to work on, producing output I hadn’t shaped. When 10 of them finished simultaneously, I had 10 [results to evaluate](https://every.to/source-code/i-stopped-reading-code-my-code-reviews-got-better) without enough context to know which ones I could trust. AI agents don’t have a speed limit, but the person managing them still does.

I kept looking for a smarter orchestration layer—a better protocol or a tighter framework that would filter the output and tell me which result to trust. Then I stopped and looked at what was really doing the work.

It was something I already had—a folder.

A project folder with a CLAUDE.md/AGENT.md (the file that tells an AI how to work in your project), some [skill](https://skills.every.to/) definitions, and context accumulated through months of [compound engineering](https://every.to/source-code/compound-engineering-the-definitive-guide) —that’s an agent. The context that this folder gives an AI model makes the generalized model a specialist in whatever task or field you want it to excel in.

I’m running 44 of these folders-as-agents across multiple projects now. Each one runs inside a specialized folder I’ve built and tested over months, and a dispatch layer I built on top does the routing between them. Here’s how it works.

[![Uploaded image](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/advertisements/1061/optimized_2f828539-b123-4add-8d1d-381bd4c44b72.png)](https://www.softr.io/build-with/every?utm_source=every&utm_medium=influencer&utm_campaign=ai_co-builder&utm_content=every_march_launch_post)

#### Build AI apps that actually work

Softr’s AI Co-Builder lets you describe the internal tool or portal your business needs and get back a real, working app in minutes—database, logic, logins, permissions, security, and all. No coding. Not a prototype. Ready for real users immediately. Switch between AI and visual editing whenever you want.

[Start building at softr.io](https://www.softr.io/build-with/every?utm_source=every&utm_medium=influencer&utm_campaign=ai_co-builder&utm_content=every_march_launch_post&source=post_button)

## The agents hiding on your hard drive

People hear “agent” and picture a [Rube Goldberg machine](https://en.wikipedia.org/wiki/Rube_Goldberg_machine) —dozens of comically complex moving parts, each one triggering the next. But an agent is much simpler: a model with enough context so you don’t have to re-explain everything each time you open the chat.

Here’s an example: All of Cora’s code lives in a project folder in the Every organization on GitHub. When I open that folder with Claude, Claude can see the code and the structure. But it doesn’t know my way of working or what I care about, which is why the folder also includes a [CLAUDE.md](http://claude.md/) file. The file tells Claude how I name things and how I structure tests. That’s an agent—not a fancy one, but an agent nonetheless. Just by pointing the model at this folder, which contains some of my personality, knowledge, and [taste](https://every.to/p/what-is-taste-really), the model can be a specialist in my codebase.

Claude Skills—files that give the model specific capabilities—are an example of this “folder as agent” structure. Before anyone called them “skills,” people were already writing markdown files full of instructions and dropping them into project directories.

My ~/cora/ folder goes further:

- **Conventions and standards:** The CLAUDE.md covers Rails conventions, deploy workflows, and database patterns.
- **Institutional knowledge:** The docs/developer-docs/ directory holds accumulated knowledge that any new agent inherits automatically, including architecture reports, the email processing pipeline, and the [assistant system design](https://every.to/source-code/from-every-studio-cora-assistant-spiral-goes-agentic-and-sparkle-de-dupes).
- **Operational memory:** The docs/runbooks/ and docs/investigations/ capture operational patterns built from real incidents.
- **Specialized agents:** .claude/agents/ holds specialists I’ve refined over months: reviewers, planners, and the assistant-component-creator.

When I point a model at this folder, it starts working with everything Cora knows about itself.

The reading order I give to every new agent that touches Cora is the following: Read CLAUDE.md first, then the architecture document, then the assistant system report, then the assistant’s prompt, then the component creator agent.

[![My Cora repository serves as a living memory system: conventions, runbooks, and specialized agents all layered so any new model instantly inherits how Cora thinks and operates. (All images courtesy of Kieran Klaassen.)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4108/optimized_46f0bce3-b65e-415b-a584-fc79624aa862.jpeg)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4108/optimized_46f0bce3-b65e-415b-a584-fc79624aa862.jpeg)

My Cora repository serves as a living memory system: conventions, runbooks, and specialized agents all layered so any new model instantly inherits how Cora thinks and operates. (All images courtesy of Kieran Klaassen.)

~/cora-agent/, another folder, is a completely different agent, though it runs on the same model. (I mostly use [Opus 4.6](https://every.to/vibe-check/opus-4-6), but also like [GPT 5.4](https://every.to/vibe-check/gpt-5-4-openai-is-back) and [Gemini Pro](https://every.to/vibe-check/vibe-check-gemini-3-pro-a-reliable-workhorse-with-surprising-flair) 3.1.)

Where ~/cora/ builds features, ~/cora-agent/ runs the operation. It has no app code, so it can’t accidentally modify production code while doing operations work. Instead, it has skills for:

- Querying AppSignal to check for errors and performance problems across Cora’s live system
- Tailing Render logs to watch server output in real time and catch issues as they happen
- Pulling from a Postgres read replica—a copy of Cora’s database—so it can query user data without affecting the live version
- Reading Intercom tickets so it can connect customer complaints to technical problems
- Correlating GitHub deploys to production incidents, tracing a break back to the specific code change that caused it

.claude/skills/ directory is a cockpit—a single place where the agent can see and interact with every system Cora depends on. Each external system Cora touches has a reference file telling the agent exactly how to talk to it. Its bin/ directory has Ruby daemons (background processes that stay running continuously) running continuously: a scheduler, an inbox processor that triages incoming issues automatically, and a health monitor that restarts stalled processes. Three postmortems live in docs/postmortems/. A dense deploy journal covers every Cora pull request from March through April.

Just by changing the folder and not the model, I have a different agent. Point Opus at ~/cora/ and it’s a Rails engineer. Point it at ~/cora-agent/ and it’s an ops engineer who knows our incident history, our service topology, and exactly which Slack channel to notify.

## A morning with 44 agents

Once you realize the folder is the agent, you can run as many as you want. I have a handful of specialized folders, but 44 agents running across them at any given time—several working inside ~/cora/ simultaneously on different tasks, others monitoring production from ~/cora-agent/, others handling orchestration. It’s the same folders, just different jobs happening in parallel.

The obvious question is: Who manages 44 of them?

For months, the answer was me, manually. I’d open a terminal tab, navigate to a project folder, start a Claude Code session, give it a task, open another tab, and do it again. I was the dispatch layer—keeping track of which agent was working on what, which tasks had finished, and which were stuck. It worked when I had five agents. At 10, I started forgetting what was running where. At 44, it was unsustainable. Bugs I knew were easy to fix sat untouched for days, and pull request reviews piled up.

So I built a dispatch layer: a system that sits above the folders and routes work between them. There’s a Ruby daemon that watches a directory for spawn requests. When I ask it to orchestrate a task, it creates a lead agent, the lead breaks the task into subtasks and writes each one as a file, and the daemon picks those files up and spawns worker agents in the right folders. Workers report back by writing files. The daemon checks status every 60 seconds. There’s no need for custom networking or agent-to-agent protocol.

As a result, I went from manually juggling terminal tabs to managing my entire engineering surface from one place. I interact with the dispatch layer through slash commands in Claude Code. Two do most of the work:

### Two commands that replace 20 terminal tabs

- **The morning briefing:** I type /hey into Claude Code to get a status report. For each project, the system checks what was completed, what errored, what’s blocked, and any new high-priority issues. This one command yields a complete picture of what needs my attention across Cora’s main codebase, the ops environment, and the orchestration system.
- **The kickoff:** I type /orchestrate to kick off a task—for example, /orchestrate “Fix GitHub issue #1765.” The system creates a lead agent, which breaks down the task and spawns workers in the right folders. Each worker inherits that folder’s full context—its CLAUDE.md, agents, and accumulated knowledge. Workers do the work. A pull request appears, and I review it.

[![With the /orchestrate command, a lead agent delegates to specialized workers across contexts, and you watch the entire system think in parallel.](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4108/optimized_2fdb920e-0dff-47b4-9653-b47961d8e09f.jpeg)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/4108/optimized_2fdb920e-0dff-47b4-9653-b47961d8e09f.jpeg)

With the /orchestrate command, a lead agent delegates to specialized workers across contexts, and you watch the entire system think in parallel.

Every agent gets a pane I can watch live in tmux (a terminal tool for running multiple sessions at once). A dashboard shows me a live map called an agent tree that shows every agent and its status—working, waiting, done, or error. Pull requests and GitHub issue comments arrive for asynchronous review. I process results when I’m ready, instead of when agents finish their tasks.

The whole thing runs on a Ruby daemon with file-based messaging. The dispatch layer is not sophisticated infrastructure. The sophistication lies in the folders underneath it—each one a specialist built through months of learning from work.

[Anthropic’s own research](https://www.anthropic.com/engineering/multi-agent-research-system) backs up why this pattern works: An [Opus](https://www.youtube.com/watch?app=desktop&v=Unzc731iCUY) lead agent with [Sonnet](https://every.to/vibe-check/vibe-check-claude-sonnet-4-5) sub-agents outperformed a single Opus agent by 90 percent on research tasks. But they also found that multi-agent systems burn 15 times more tokens than single-agent setups, and that most coding tasks have fewer parallelizable steps than research, which makes them harder to split across agents. The dispatch layer doesn’t replace me—it handles the tracking so that I still decide what work gets done and where it goes.

## What breaks at scale (and why you can’t vibe orchestrate)

That morning walkthrough makes it sound smooth, but it isn’t always.

The encoding bug was my favorite disaster. For weeks, agents would randomly crash mid-task, and the error message gave no helpful explanation. I dug through logs, checked API responses, and tested network configurations. The culprit turned out to be em dashes and curly quotes—characters from text I’d copy-pasted into prompts. My daemon was running US-ASCII encoding, which only recognizes plain English letters, so those special characters were crashing it. The frontier of AI-assisted development is full of problems like this: genuinely dumb, and shockingly hard to find.

The harder ongoing challenge is context drift. With dozens of agents, some end up running stale versions of tasks or duplicating work that another agent already finished. The list of active agents grows, but I have to do manual cleanup. I don’t have a good automated solution yet—I prune regularly and accept that some tokens get wasted.

This setup also entails a sneaky issue: agent stalls. An agent makes too many API calls too fast or gets stuck waiting for input, and its status stays on “working” indefinitely. You don’t notice until you check, and when you’re managing 44 agents, you don’t always check.

These failures point to the biggest lesson I’ve learned: You can’t vibe orchestrate.

Just like you can’t [vibe code](https://every.to/source-code/i-rebuilt-sparkle-in-14-days-with-ai) —you need [plans before you start building](https://every.to/source-code/stop-coding-and-start-planning) —and you can’t [vibe fix](https://every.to/chain-of-thought/when-your-vibe-coded-app-goes-viral-and-then-goes-down) when things break in production, you can’t hand a folder to the dispatch layer and hope for the best. When I start a new project, I don’t immediately hand it to the dispatch layer. I set up the folder, build the agent, establish the flows—the [compound engineering loop](https://every.to/chain-of-thought/compound-engineering-how-every-codes-with-agents) —and use them myself until they’re predictable. Only when I trust a flow do I hand it off to the dispatch layer and stop watching. If you skip this step, you’ll have agents opening pull requests for work you’ve already finished and filing duplicate issues. The order of work is key: Build it, use it, trust it, and then orchestrate it.

## Your folder is already an agent

I started this whole experiment trying to build a swarm. I ended up with 44 folders, each one with specialized context built through months of work, connected by a dispatch layer.

It’s not what I expected, but it works. You also have the building blocks to create the same thing.

If your project has a CLAUDE.md and some files in.claude/, you have an agent. You just haven’t been treating it like one.

Here’s an experiment for you: Look at your project folder. Is it a generic setup or a specialist? If it’s generic—if your CLAUDE.md is boilerplate you copied from someone’s blog post—spend 30 minutes making it yours. Add your conventions, your patterns, your opinions about how code should be written. Then try running two agents in separate git worktrees (separate copies of your codebase so they don’t interfere with each other) and notice where *you* slow things down. That’s where the dispatch layer needs to go.

I’m one step into that myself. I’ve moved from manually orchestrating—opening terminal tabs, navigating folders, and starting sessions—to having a dispatch layer do that routing for me.

The step after this is already arriving. Anthropic just launched [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) —a hosted service that handles sandboxing, state management, and tool execution so developers can focus on what their agents do rather than how to keep them running. The folder-as-agent pattern makes that kind of managed autonomy possible: a trusted, specialized environment the model can run inside without you holding its hand.

The industry is spending a lot of energy on autonomous swarms. I spent three months there too, and found that for now, the answer is still just a folder.

#### Go further

- Read Kieran’s [comprehensive guide to compound engineering](https://every.to/guides/compound-engineering?source=post_button)
- [Install the compound engineering plugin](https://github.com/EveryInc/compound-engineering-plugin)
- [Watch the recording](https://every.to/events/compound-engineering-camp) from Kieran’s last compound engineering camp

---

*Thank you to* ***[Katie Parrott](https://every.to/@katie.parrott12)*** *for editorial support.*

***[Kieran Klaassen](https://every.to/@kieran_1355)*** *is the general manager of* *[Cora](https://cora.computer/), Every’s email product. Follow him on X at* *[@kieranklaassen](https://x.com/kieranklaassen)* *or on* *[LinkedIn](https://www.linkedin.com/in/kieran-klaassen/).*

*To read more essays like this, subscribe to [Every](https://every.to/subscribe), and follow us on X at [@every](http://twitter.com/every) and on [LinkedIn](https://www.linkedin.com/company/everyinc/).*

*For sponsorship opportunities, reach out to sponsorships@every.to.*

[Subscribe](https://every.to/subscribe?source=post_button)