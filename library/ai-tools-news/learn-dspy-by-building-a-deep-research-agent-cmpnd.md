---
tags:
  - library
title: "Learn DSPy by Building a Deep Research Agent — cmpnd"
url: "https://www.cmpnd.ai/blog/learn-dspy-deep-research.html"
company: [personal]
topics: []
created: 2026-03-11
source_type: raindrop
raindrop_id: 1638523862
source_domain: "cmpnd.ai"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Build several deep research agents with increasing complexity to learn DSPy's core concepts: Signatures, Modules, and composable programs.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Learn DSPy by Building a Deep Research Agent — cmpnd

URL Source: https://www.cmpnd.ai/blog/learn-dspy-deep-research.html

Markdown Content:
Build several deep research agents of increasing complexity to learn DSPy's core concepts: Signatures, Modules, and composable programs

Deep research agents are amazing tools. Given a research task or question, they scour the web, synthesizing data from numerous sources to prepare a nicely packaged report.

There are many deep research agents, each with their own quirks and design decisions. [ChatGPT](https://openai.com/index/introducing-deep-research/) sports one, as does [Claude](https://claude.com/blog/research). Google [has](https://notebooklm.google/app)[a couple](https://gemini.google/overview/deep-research/). Each is unique in how they plan, explore, clarify, and synthesize.

Today we're going to build several deep research agents, increasing their complexity as we go. By the end of this article you'll have a better idea how these agents work and how to build them. More importantly, you'll also learn _plenty_ about DSPy. You'll understand how it helps devs prototype quickly, iterate easily, and build reliable software.

All the code for these examples is accessible in a [GitHub repo](https://github.com/cmpnd-ai/dspy-tutorial-deep-research).

* * *

## Introducing Signatures & Modules as We Build Our First Agent

At a high level, our researcher does one thing: it accepts a research request and returns a research report. It's easy to imagine additional requests or constraints (include at least 3 sources, make it at least 500 words), but to begin we'll start with the minimum viable task description.

Today, we're using [DSPy](https://dspy.ai/) to implement our agent.

DSPy is an open-source software framework that lets us _declaratively_ describe the goals of our program, rather than _how_ it should accomplish the task. Think of DSPy as a higher-level language for AI programming, similar to Python compared to assembly. In Python we don't have to manage our memory, track our pointers, or handle register allocation. In DSPy we don't have to hand-craft our prompts, use weird context hacks, manually parse outputs, or manage the details of our test time strategy.

So let's focus on _what_ we want: we want a program that takes in a research request (as text) and outputs a research report (also as text). In DSPy, we can express this as a [Signature](https://dspy.ai/learn/programming/signatures/), like so:

`researcher_signature = "research_request: str -> report: str"`
A Signature can be a string or a class (more on that later). Here we're giving our input a name (`research_request`) and specifying its type (`str`). Our output, delineated by the `->`, is also named and typed (`report` and `str`, respectively).

When I first read about DSPy Signatures, I immediately began looking through the documents for a list of "terms" I could use to describe my inputs and outputs. I thought there was a preset list! But this was old software thinking: we can name our inputs and outputs _whatever we want_, and the LLM will _infer_ our goals from them. This means it's important that we give our Signature attributes descriptive names; ones that give the LLM a clue to what we want.

Amazingly, `research_request` and `report` turn out to be sufficiently detailed for our goals! No further instruction is needed.

On its own, a Signature does nothing other than express what you want. It's intentionally very simple. If we send it to an LLM as-is, we'll be rather disappointed. DSPy provides functions that use our signature to perform operations with an LLM, the most essential of which is _Module_.

A DSPy [Module](https://dspy.ai/learn/programming/modules/)_executes_ your task, as defined by your signature. In AI programming, this means it manages test-time execution, including prompting techniques, tool definitions, environment procurement, and template formatting. It also handles LLM responses, either continuing a multi-turn process or extracting and formatting the final output.

There are several predefined Modules that come with DSPy, the most basic of which is `Predict`. There's no test-time strategy here; `Predict` just formats your Signature's information into a prompt template, inserts your input parameters, and manages data extraction:

`researcher = dspy.Predict(researcher_signature)`
Once we've set up a [language model](https://dspy.ai/learn/programming/language_models/), we can use our program. Together, the whole thing looks like this:

```
import dspy

# Connect to and set an LLM
lm = dspy.LM('anthropic/claude-haiku-4-5', api_key='ANTHROPIC_API_KEY', max_tokens=64000)
dspy.configure(lm=lm)

# Create our program
researcher_signature = "research_request: str -> report: str"
researcher = dspy.Predict(researcher_signature)

# Call our program
result = researcher(research_request="Write a history of Coyote Hills, a park in the East Bay Regional Parks District in California.")
print(result.report)
```

Behind the scenes, the `Predict` module prepares inputs to send to the LLM. In practice, this is often a string formatting our inputs and additional instructions. In this specific case, first a system prompt is generated:

```
Your input fields are:
1. `research_request` (str):
Your output fields are:
1. `report` (str):
All interactions will be structured in the following way, with the appropriate values filled in.

[[ ## research_request ## ]]
{research_request}

[[ ## report ## ]]
{report}

[[ ## completed ## ]]
In adhering to this structure, your objective is: 
        Given the fields `research_request`, produce the fields `report`.
```

Then it sends the user message:

```
[[ ## research_request ## ]]

Write a history of Coyote Hills, a park in the East Bay Regional Parks District in California.

Respond with the corresponding output fields, starting with the field `[[ ## report ## ]]`, and then ending with the marker for `[[ ## completed ## ]]`.
```

Claude Haiku then replies with the following, which I've truncated for length:

```
[[ ## report ## ]]

Coyote Hills Regional Park – A Brief History  
East Bay Regional Park District (EBRPD), Alameda County, California  

1. Indigenous Era (10,000+ years BP – 1770s)  
   • The park sits on the ancestral territory of the Tuibun (Ohlone) people...
   • More than 2,000 bedrock mortars, dozens of shell-mounds, and a 2,000-year-old 
     village site (CA-ALA-328) document continuous occupation.

...

[[ ## completed ## ]]
```

This response is then handled by DSPy and the `Predict` module, which extracts and validates the output fields you've defined. We don't need to parse the raw response, we simply access our output parameter with `response.report`. The point here is that we don't have to manage or worry about the specific interactions with the LLM. These are low-level decisions we're delegating to DSPy.

Depending on the model you're calling and the nature of your question, this report won't be that bad. But it can only leverage what the model has encoded in its weights.

A _proper_ deep research agent, however, needs access to the web. We need a tool or two, and a way to provide it to our program.

Defining tools in DSPy is simple. Each tool is a Python function – it can execute whatever code you'd like. What gets used by your Module is the name of the function and its docstring. Like Signature input and output names, a descriptive function name helps the LLM understand the function's utility.

Let's define our web tools:

```
from tavily import TavilyClient
from typing import Literal

tavily_client = TavilyClient(api_key=TAVILY_API)

def internet_search(query: str, max_results: int = 5, include_raw_content: bool = False): 
    """Run a web search""" 
    return tavily_client.search(
        query, max_results=max_results, 
        include_raw_content=include_raw_content, 
        topic="general",
    )

def read_webpage(url: str) -> dict:
    """Read the content of a URL."""
    response = tavily_client.extract(url)
    return response
```

We're using [Tavily](https://www.tavily.com/) as a search provider.

With these two tools, we're nearly done. We just need to update our deep research agent:

```
researcher = dspy.ReAct(researcher_signature, tools=[internet_search, read_webpage])
result = researcher(research_request="Write a history of Coyote Hills, a park in the East Bay Regional Parks District in California.")
print(result.report)
```

Instead of `Predict` we use the `ReAct` module. This module implements the [ReAct](https://www.promptingguide.ai/techniques/react) test-time strategy, where the model is prompted to reason ("Re") and then act ("Act", or call tools). The ReAct module provides instructions to the model detailing the tools and how to call them. It also manages multiple calls, until the model is done with the tools and synthesizes its final answer.

We call this program just like before...And it generates a rather good report! There's more detail and it tends to be more accurate (definitely more up to date). At this point we have a _proper_ deep research agent.

But we can do better.

* * *

## Composing Programs and Asking Clarifying Questions

When OpenAI's [deep research agent](https://openai.com/index/introducing-deep-research/) launched, it brought a novel feature to the market. The agent would ask you clarifying questions prior to conducting research, a discovery process that honed and fleshed out your request.

To add this feature to our agent, we only need to make a few adjustments.

First, we need to generate some clarifying questions and pose them to the user. Again, we'll use a string Signature and the `Predict` module to define such a program:

```
clarifying_signature = "research_request: str -> clarifying_questions: list[str]"
clarifier = dspy.Predict(clarifying_signature)
```

The pattern is the same as before, we're just asking for a new type of output (a list of strings), which gives the LLM instructions to provide multiple questions. How many questions? That's up to the LLM's discretion, but we could specify a length by changing our type to a `tuple` with a set length:

```
clarification_signature = "research_request: str -> clarifying_questions: tuple[str, str, str]"
clarifier = dspy.Predict(clarification_signature)
```

Adding this type definition gives us 3 clarifying questions.

This is a key aspect of Signature design: _types encourage and enforce specific behaviors_. It allows us to manage LLM interactions in a manner closer to code.

Another option, which increases the flexibility of our program, is to provide our desired number of questions as another input, like so:

```
clarifying_signature = "research_request: str, number_of_questions: int -> clarifying_questions: list[str]"
clarifier = dspy.Predict(clarifying_signature)
```

With commas we can add additional inputs or outputs to our signature. This is incredibly handy, but as your parameters grow or you find yourself wishing for more specifications than your variable names or typing can convey, it's probably time to move to [class-based Signatures](https://dspy.ai/learn/programming/signatures/#class-based-dspy-signatures). Translating our signature above into a class looks like this:

```
class ClarifyingSignature(dspy.Signature):
    "Generate clarifying questions to inform research work in response to the request."
    research_request: str = dspy.InputField()
    number_of_questions: int = dspy.InputField(desc="The number of clarifying questions to generate")
    clarifying_questions: list[str] = dspy.OutputField()

clarifier = dspy.Predict(ClarifyingSignature)
```

Class-based signatures are much _roomier_. We still have our variable names and types, but we now have two additional levers to convey our intent to the LLM: the _docstring_ and _field descriptions_.

The docstring, like our tool definitions, is passed through to the prompt when the Module calls the LLM. It's entirely optional – we don't really need it here, but I'm including it for demonstration purposes. Field descriptions are optional as well, but they can be very helpful when the field name may not sufficiently convey its role. For example, `number_of_questions` is a bit vague. Most models will correctly infer its relationship to `clarifying_questions`, but smaller models might get confused. With a short note, we clear up the confusion.

Running our program yields a desired amount of questions, which we then use to prompt the user, whose answers are stored in a `list` containing a `TypedDict`:

```
# Generate our questions
results = clarifier(research_request=research_request, number_of_questions=3)

# Get our answers
q_and_a = []
for question in results.clarifying_questions:
    answer = input(f"{question}\n")
    q_and_a.append({"clarifying_question": question, "user_guidance": answer})
```

Note that I'm providing rather descriptive keys in the dictionaries we add to `q_and_a`. Again, these keys will give the model a clue what the data represents.

Now all we need to do is add an input field to our `researcher_signature` and we're good to go!

```
researcher_signature = "research_request: str, clarifying_questions_and_answers -> report: str"
researcher = dspy.ReAct(researcher_signature, tools=[internet_search, read_webpage])
result = researcher(
    research_request=research_request, 
    clarifying_questions_and_answers=q_and_a
)
print(result.report)
```

Our researcher continues to improve. By adding clarifying questions, we're less likely to misinterpret user intent and more likely to focus on the areas they care about. And it took [less than 50 lines of code](https://gist.github.com/dbreunig/c13d0e950467659d51bd370a6f19e11f), including comments.

* * *

## Decomposing Our Workflow: Trading Autonomy for Reliability

The above program works, but there are several problems it might run into. Repeated web research will fill the context window, risking [context rot](https://research.trychroma.com/context-rot). The model will struggle to manage its citations, and will occasionally hallucinate resources. Sometimes the agent will completely miss subtopics the user expected and required in the output. And sometimes it's not clear _where_ the agent found a detail or fact.

Further, there are features we may want to add. For example, we may want to specify a budget for our agent so we can control both the cost and time it takes to deliver a report. And adding in tasteful defaults specifying the length of a report and the tone of the writing can yield more consistent results.

These requirements are critical to keep in mind when designing and evolving your agent. Most of the examples we see online of incredible AI abilities involve long-running, frontier models with a human in the loop, ready to handle missteps. Don't get me wrong, these are great demonstrations. But if we're building a product or workflow that's going to be run countless times and needs to prioritize _reliability_, we require decomposition and structure.

To take our agent to the next level, adding the features and fixes above, we need to define several programs to power our product:

| Program | Task | String Signature | Tools |
| --- | --- | --- | --- |
| Clarifier | Creates clarifying questions to pose to the user | `research_request: str, number_of_questions: int -> clarifying_questions: list[str]` | – |
| Planner | Identifies subtopics to research | `research_request: str, clarifying_questions_and_answers, max_number_of_sub_topics: int -> topics_to_research: list[str]` | – |
| Gatherer | Collects URLs likely to inform subtopic research | `research_request: str, subtopic_to_research: str, num_sources: int -> relevant_urls_to_investigate: list[str]` | Web Search |
| Processor | Reads URLs and extracts structured information | `research_task: str, research_subtask: str, url: str -> summary: str, relevant_facts: list[str], interesting_anecdotes: list[str]` | – |
| Synthesizer | Synthesizes processed information into a final report | `research_request: str, clarifying_questions_and_answers, subtopic_research: list[dict] -> final_report: str` | – |
| Annotator | Adds citations to the final report | `final_report: str, processed_sources: list[dict] -> annotated_report: str` | – |

You'll notice we are only providing one program with one tool. By breaking the task of identifying sources and processing them into two steps, we can load the page content programmatically then pass it to the processor. This saves us one LLM turn for each page processed, since we're able to use `Predict` and not `ReAct`.

Our system reins in the model in exchange for control. There's a number of benefits we get out of this:

*   **Budget & Cost Control:** There are numerous levers we can set in our programs. We can specify a maximum number of subtopics to define, how many URLs should be gathered per subtopic, and set a maximum number of web searches. We can expose these parameters to the user or wrap them in "light", "medium", and "deep" presets.
*   **User Control:** We were already prompting users with clarifying questions, but could expose more levers. Users could review and edit the list of subtopics identified by the Planner (in fact, this approach is what ChatGPT opts for these days). Users could also provide websites they'd like to avoid when gathering sources.
*   **Easier Evaluation:** It's really hard to write effective evals for big, monolithic tasks. By decomposing our agent into separate steps, we make evaluation easier: it's much easier to write tests for extracting facts from individual web pages than it is to write tests for the entire deep research task.
*   **Easier Optimization:** Program optimization, specifically _prompt_ optimization, is one of the chief reasons people start using DSPy. But to run effective optimizations, you need good evals and metrics. As we covered in the previous point, breaking your program up into sub-steps makes writing evals and metrics _much_ easier. Further, it lets you prioritize your eval efforts. Perhaps the Processor is the make-or-break step, but the Clarifier works well out of the box. Then you can spend your time focused on the Processor.
*   **Flexible Execution:** Separating these tasks allows you to route them to different models. The Clarifier works fine with a small, fast model; the Synthesizer benefits from a frontier model's writing quality. DSPy lets you easily assign different LLMs for different programs. Finally, we can parallelize our calls when it makes sense. All the Gatherer calls can be called at once, as can the Processors. This will speed things up greatly, especially with more subtopics and sources.
*   **Easier Auditing:** For some use cases, the ability to audit where facts come from is incredibly important. For example, if you're building a deep research system for legal case histories you're going to want to allow users to connect report details to the underlying claims and sources they originate from. In our final code, we're able to output the structured data gathered during processing, tied back to each URL. In our hypothetical legal research product, this reference will be critical to aid validation.

Taken together, the benefits above help us build, deliver, and maintain _more reliable products_. By trading the raw, unstructured intelligence of a long thinking, frontier model for a decomposed workflow, we gain control, predictability, and performance.

But there's a tension here. We've already discussed how too little structure can lead to slow, expensive, and unreliable programs. But too much structure and you're locked into rigid workflows that are slow to adapt and require maintenance. It's a balancing act.

Thankfully, DSPy helps manage this tension. Signatures and Modules are lightweight and composable. It's cheap to restructure your workflow as your understanding evolves, without having to worry about brittle prompts or response parsing. Further, by decoupling the _how_ from the _what_ (your Signatures), you can easily swap in new tactics.

One great way to _start_ a project like this is to give the largest, most-capable models your task, with little structure. As you observe its work, note its tactics, and analyze the sub-calls you'll start to inform your own patterns and discover novel ways for structuring your workflows. In fact, DSPy's [RLM](https://dspy.ai/api/modules/RLM/) is well suited to this exploration. But that's another lesson...

* * *

## What We've Built (and What Comes Next)

We started with a two-line program and progressively built a multi-step, reliable research system with clarification, planning, source gathering, processing, synthesis, and annotation.

Along the way, we've touched on the core loop of programming with DSPy. Define _what_ you want with Signatures, choose _how_ to execute with Modules, and compose programs together as you would regular Python functions. We get enforced structures with Signature typing, but can lean on descriptive names and docstrings to guide the model.

Now we have the skills needed to progress onto DSPy's _evaluation_ and _optimization_ functions. Stay tuned.
