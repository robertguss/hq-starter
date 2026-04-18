---
tags:
  - library
title: "Hatchet | The orchestration engine for teams who ship"
url: "https://hatchet.run/"
company: [personal]
topics: []
created: 2026-04-16
source_type: raindrop
raindrop_id: 1686604949
source_domain: "hatchet.run"
source_type_raindrop: link
collection: "unsorted"
collection_id: -1
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Hatchet is a single platform for orchestrating AI agents, scheduling background tasks, and running mission-critical workflows.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Hatchet | The orchestration engine for teams who ship

URL Source: https://hatchet.run/

Markdown Content:
A single platform for orchestrating AI agents, scheduling background tasks, and running mission-critical workflows

![Image 1: Hatchet dashboard showing workflow runs, task details, and activity navigation](https://hatchet.run/assets/ui-CVenXwgc.svg)

## How it works

There are two components to running Hatchet: the orchestration engine and your workers. Workers run on your own infrastructure, while the Hatchet orchestration engine is available as a managed service or can be self-hosted.

![Image 2: Diagram of Hatchet orchestration engine connecting to customer-managed workers in the cloud](https://hatchet.run/assets/how-BuPEv6aN.svg)

Step 1

Write tasks and workflows as code

![Image 3: Illustration: defining tasks and workflows as code with retries and step dependencies](https://hatchet.run/assets/step1-CJUnStdm.svg)

Tasks are simple functions. They can be composed into workflows to represent more complex logic. Your tasks automatically retry on failure and handle complex dependencies between steps.

Step 1

Write tasks and workflows as code

![Image 4: Illustration: defining tasks and workflows as code with retries and step dependencies](https://hatchet.run/assets/step1-CJUnStdm.svg)

Tasks are simple functions. They can be composed into workflows to represent more complex logic. Your tasks automatically retry on failure and handle complex dependencies between steps.

Step 2

Invoke your tasks and workflows

![Image 5: Illustration: starting workflows from APIs, schedules, and events](https://hatchet.run/assets/step2-Dpmd8atN.svg)

Start workflows from your API, schedule them to run at specific times, or trigger them when events happen. Tasks run immediately or queue up for later.

Step 2

Invoke your tasks and workflows

![Image 6: Illustration: starting workflows from APIs, schedules, and events](https://hatchet.run/assets/step2-Dpmd8atN.svg)

Start workflows from your API, schedule them to run at specific times, or trigger them when events happen. Tasks run immediately or queue up for later.

Step 3

Run workers in your own cloud

![Image 7: Illustration: running Hatchet workers on your infrastructure and connecting to the orchestrator](blob:http://localhost/ac59514e90f10548c6c737d57805f5ac)

Deploy workers on Kubernetes, Porter, Railway, Render, ECS, or any container platform. They automatically connect to Hatchet and can scale up or down based on workload.

Step 3

Run workers in your own cloud

![Image 8: Illustration: running Hatchet workers on your infrastructure and connecting to the orchestrator](blob:http://localhost/ac59514e90f10548c6c737d57805f5ac)

Deploy workers on Kubernetes, Porter, Railway, Render, ECS, or any container platform. They automatically connect to Hatchet and can scale up or down based on workload.

Step 4

Monitor and replay

![Image 9: Illustration: monitoring workflows, failures, and metrics in the Hatchet dashboard](https://hatchet.run/assets/step4-D3IXkVFQ.svg)

See all your worksflows in the dashboard, get alerts when tasks fail, and export metrics to your monitoring tools. Full visibility (and control) without extra setup.

Step 4

Monitor and replay

![Image 10: Illustration: monitoring workflows, failures, and metrics in the Hatchet dashboard](https://hatchet.run/assets/step4-D3IXkVFQ.svg)

See all your worksflows in the dashboard, get alerts when tasks fail, and export metrics to your monitoring tools. Full visibility (and control) without extra setup.

Use Case

## Ingestion & Indexing Pipelines

Agents and AI workflows need continuous, fast access to your data to construct context on-demand. With Hatchet, your vector databases and knowledge graphs will always be up-to-date.

![Image 11: Illustration of ingestion and indexing pipelines updating vector databases and knowledge bases](https://hatchet.run/assets/ingestion-BCOFTpWq.svg)

Learn more

##### Scale with Hatchet

Build resilient pipelines that handle real-world complexity. Automatic retries, intelligent rate limiting, and checkpoint recovery mean your data stays fresh without constant firefighting.

*   Build RAG, document processing, and indexing pipelines with ease

*   Easily replay failed pipelines from the Hatchet UI

*   Update vector databases in real-time with exactly-once semantics

With Hatchet, we've scaled our indexing workflows effortlessly, reducing failed runs by 50% and doubling our user base in just two weeks!

```
# Build resilient indexing pipelines with automatic retries and checkpoint recovery
indexing_workflow = hatchet.workflow(name="document-indexing", input_validator=DocumentInput)

@indexing_workflow.task()
async def chunk_document(input: DocumentInput, ctx: Context) -> dict:
    chunks = await split_into_chunks(input.document_url)
    return {'chunks': chunks, 'doc_id': input.doc_id}

@indexing_workflow.task(parents=[chunk_document])
async def parse_chunks(input: DocumentInput, ctx: Context) -> dict:
    chunk_output = ctx.task_output(chunk_document)
    parsed = await extract_content(chunk_output['chunks'])
    return {'embeddings': parsed, 'doc_id': chunk_output['doc_id']}

@indexing_workflow.task(parents=[parse_chunks])
async def store_vectors(input: DocumentInput, ctx: Context) -> dict:
    parse_output = ctx.task_output(parse_chunks)
    await vector_db.insert(parse_output['embeddings'])
    return {'status': 'indexed', 'doc_id': parse_output['doc_id']}
```

Use Case

## AI Requests & Agents

AI agents need complex orchestration — managing tool calls, handling timeouts, maintaining conversation state, and enforcing safety constraints. Most teams end up building fragile in-process systems that are difficult to scale and maintain.

![Image 12: Illustration of AI agents with tool orchestration, guardrails, and durable execution](https://hatchet.run/assets/AIAgents-CNu8oChg.svg)

Learn more

##### Reliability with Hatchet

Define agents as simple, durable functions with built-in orchestration primitives. Set guardrails, manage state, and handle failures gracefully.

*   Write your agent's tools as simple functions, integrated tightly with your business logic

*   Designed to be long-running with safety and security constraints

*   Built-in eventing for human-in-the-loop signaling and streaming responses

Implementing Hatchet has revolutionized our task management system, enabling us to handle a growing number of background tasks efficiently.

```
# Define agents as durable functions with built-in state management and event signaling
@hatchet.durable_task(input_validator=AgentInput)
async def ai_agent(input: AgentInput, ctx: DurableContext) -> dict:
    # Call LLM to determine which tool to use
    tool_decision = await call_llm(input.prompt)

    # Execute the tool
    tool_result = await execute_tool(tool_decision.tool_name)

    # Wait for user approval before proceeding
    approval = await ctx.aio_wait_for(
        "approval",
        UserEventCondition(
            event_key=f"agent:approval:{ctx.workflow_run_id()}",
            expression="input.approved == true"
        )
    )

    return {
        'tool_used': tool_decision.tool_name,
        'result': tool_result,
        'approved': True
    }
```

Use Case

## Massive Parallelization

Processing thousands of documents, enriching large datasets, running agent swarms, or scheduling GPU workloads requires complex coordination. Most solutions either can't scale or become impossibly complex to manage.

![Image 13: Illustration of fan-out parallel work across many Hatchet workers and coordinated steps](https://hatchet.run/assets/parallelization-Cl2cPhUi.svg)

Learn more

##### Parallelize with Hatchet

Fan out to thousands of workers with a single function call. Built-in fairness algorithms and resource management ensure efficient utilization without manual tuning.

*   Process entire document repositories in parallel

*   Enrich millions of leads without rate limit headaches

*   Schedule GPU jobs with intelligent batching

*   Scrape web data with automatic retry and deduplication

Hatchet enables Aevy to process up to 50,000 documents in under an hour through optimized parallel execution, compared to nearly a week with our previous setup.

```
# Fan out to thousands of parallel workers with built-in fairness and resource management
@hatchet.task(input_validator=SwarmInput)
async def agent_swarm(input: SwarmInput, ctx: Context) -> dict:
    # Coordinate multiple AI agents to process tasks in parallel
    promises = []
    for task in input.tasks:
        promises.append(
            subagent.run({'task': task, 'context': input.context})
        )

    # Wait for all subagents to complete
    results = await asyncio.gather(*promises)

    # Aggregate results from all subagents
    total_completed = sum(r['completed'] for r in results)

    return {
        'total_completed': total_completed,
        'agents_used': len(results)
    }
```

## Core Principles

![Image 14: Graphic highlighting performance, durability, and code-first SDKs as Hatchet core principles](https://hatchet.run/assets/corePrinciples-DztF54Pg.svg)

* * *

##### Performance

Built for low-latency, high-throughput workloads with task start times of less than 20ms. Smart assignment rules handle rate limits, fairness, and priorities without complex configuration.

##### Durability

Every task invocation is durably logged to a data store. When jobs fail, resume exactly where you left off — no lost work, no duplicate LLM calls, no engineering headaches.

##### Code-First

Hatchet SDKs are language-native so developers can write business logic as versionable, reusable, testable atomic functions.

![Image 15: Stylized illustration of workflow steps and orchestration connecting tasks](blob:http://localhost/6b0e17dea533cb5f8492a45285d760f4)

### Build AI that scales.Consolidate your legacy orchestration into one reliable, scalable, & secure solution.

*   Enterprise-grade security, compliance, and SSO

*   Processing over 100 million tasks/day for AI-first companies

*   Custom deployment options & bring-your-own-cloud available
