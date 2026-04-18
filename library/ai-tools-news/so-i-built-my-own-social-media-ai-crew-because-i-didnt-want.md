---
tags:
  - library
title: "So I Built My Own Social Media AI Crew Because I Didn’t Want to Pay for Jasper.ai"
url: "https://medium.com/@ShaniCodes/so-i-built-my-own-social-media-ai-crew-because-i-didnt-want-to-pay-for-jasper-ai-40a279ffe89a"
company: [personal]
topics: []
created: 2025-08-19
source_type: raindrop
raindrop_id: 1305917844
source_domain: "medium.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Lazy Girl Hacks

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: So I Built My Own Social Media AI Crew Because I Didn’t Want to Pay for Jasper.ai

URL Source: https://medium.com/@ShaniCodes/so-i-built-my-own-social-media-ai-crew-because-i-didnt-want-to-pay-for-jasper-ai-40a279ffe89a

Published Time: 2025-08-16T14:26:07Z

Markdown Content:
[![Image 1: Shani Rivers](https://miro.medium.com/v2/resize:fill:32:32/1*DSBBhwMypgXfTjuL58dgKg.jpeg)](https://medium.com/@ShaniCodes?source=post_page---byline--40a279ffe89a---------------------------------------)

9 min read

Aug 16, 2025

This all really started with taking several free social media marketing webinars from [SCORE](https://www.score.org/) over the past 6 months or so. I had just started freelancing as a tutor after getting laidoff and had several clients in between looking for a new job, but I wanted to learn how to market my new side hustle nevertheless. I found the marketing strategies very helpful and I learned a lot about what platforms I wanted to be on.

But what I also found was that almost all of them to be overwhelming in implementation and very time consuming, as you had to do a lot of it manually using spreadsheets or fork out the money to use expensive AI tools.

I had also learned another programming language, Python, soon after my layoff. Since I had so much “free time”, I decided to also dive head first into AI by taking free courses on [DeepLearning.ai](https://www.deeplearning.ai/), and in particular, those dealing with building AI agent crews.

I built my first one, a [vacation crew](https://medium.com/@ShaniCodes/design-a-low-cost-staycation-with-ai-agents-free-tools-affd47800e61). And then I built another that wrote blog posts based on research results from [Exa](https://exa.ai/) and trends from [xAI’s Grok](https://x.ai/api), but I didn’t really use it, because I honestly like writing my own.

What I don’t like to do — is to post on social media.

It’s one of the things that I least like about this digital age, but you need other people to read your stuff or buy whatever it is that you are selling, so you kind of need to do it.

But for me, it’s right up there with cleaning the toilet. 🚽

![Image 2](https://miro.medium.com/v2/resize:fit:480/1*CTpHTQzk1bXmDFLoLbDdOQ.gif)

I know that there might be some folks who just “love” all things social media marketing and that’s ok. But I truly don’t.

On the bright side, I finally found a perfect use case for building yet another AI crew, where I could use and take the all tips and strategies from those SCORE webinars to task.

The only platform that does this, that I’m aware of, is [Jasper.ai](https://www.jasper.ai/). Jasper.ai is a popular AI tool for content creation and although I did use their 7-day free trial after one of those webinars, I absolutely refuse to spend that amount of money per month on anything.

So I decided to build my own crew to market on the socials in such a way as without it sounding like it’s been written by a bot and all I have to do is edit a little bit before posting. Plus I can add as many knowledge assets as I want, since I had blasted past Jasper’s limit, which is only 5 assets at the lowest tier.

Plus my crew is dirt cheap compared to [Jasper](https://www.jasper.ai/)’s lowest tier at $60 per month — I literally spend a few pennies per API call.

![Image 3](https://miro.medium.com/v2/resize:fit:500/1*RxFEa1uEEDbNulB5n408Uw.gif)

Given that I hope to ramp up to writing 4 articles and creating about the same amount of Youtube videos every month, it’ll come out to be less than a tall latte with alternative milk from Starbucks!

![Image 4](https://miro.medium.com/v2/resize:fit:480/1*3RQmjhVxUlcb43Fm6KsSEw.gif)

I also wanted my AI crew to use a social media strategy, so they don’t just create posts for the sake of creating them, and I don’t have to manage it. **BUT** they also need to use details about the brand **AND** have specialist-specific knowledge regarding the various platforms I will be using — like how many hashtags to use per platform, for example.

You wouldn’t post the same way on X as you would on Instagram, just like you wouldn’t for LinkedIn or even when creating content for YouTube, which is a beast all of its own.

So I dug around [CrewAI’s](https://www.crewai.com/) documentation and figured out how best to do it.

What I discovered is that I needed a pretty small crew with [Pydantic](https://docs.pydantic.dev/latest/) structured outputs, as I need the results to be reproducible. Plus there’s a bit of simple classifications that they will need to do and a couple of the agents are required to output their results in JSON.

So it will be **Option 2** for my project, which according to the [documentation](https://docs.crewai.com/guides/concepts/evaluating-use-cases), is a **Low Complexity, High Precision**crew:

*   Simple workflows that require exact, structured outputs ✅
*   Need for reproducible results ✅
*   Limited steps, but high accuracy requirements ✅
*   Often involves data processing or transformation ✅

**Recommended Approach:** Flows with direct LLM calls or simple Crews with structured outputs

**Example Use Cases:**

*   Data extraction and transformation
*   Form filling and validation
*   Structured content generation (JSON, XML)
*   Simple classification tasks

As I need my crew to classify the content of my articles and video transcripts, I wanted to give them some guidelines on how to do this, so that they do it consistently and I don’t have to worry about making sure that their task description setup isn’t too verbose.

Plus it saves on bandwidth and burning through those pesky API credits, by giving them a single source of truth about how to do their task, so they don’t have to go out to the interwebs and try to figure out exactly what I want and what the heck I am referring to EVERY. SINGLE. TIME.

Here’s where [Knowledge](https://docs.crewai.com/concepts/knowledge#agent-vs-crew-knowledge-complete-guide) comes in, because the analysis and content creation tasks I want them to perform is primarily creative and analytical, they need structure and guidance on how to best to do it. Plus I need this information for tracking the social media posts they output, the KPIs, in my content calendar and for their future iterations.

[Knowledge](https://docs.crewai.com/concepts/knowledge#agent-vs-crew-knowledge-complete-guide) in CrewAI is a powerful system that allows my AI agents to access and utilize external information sources during their tasks. Think of it as giving your agents a reference library or job manuals that they can consult while working.

Key benefits of using Knowledge is that it:

*   Enhances agents with domain-specific information,
*   Supports decisions with real-world data,
*   Maintains context across conversations, and
*   Grounds their responses in factual information

![Image 5](https://miro.medium.com/v2/resize:fit:350/1*uFK1vRi5LHwXj0p6tsDg5A.gif)

## The Code

So this is the part of the article where I talk code.

## Get Shani Rivers’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

I decided to add the `knowledge` directory to the project level. Please note that it will download to the same storage system as memory by default and where exactly that might be is platform dependent, see [the documentation for where exactly](https://docs.crewai.com/concepts/knowledge#where-crewai-stores-knowledge-files), because it’s different for every operating system.

import os

from pathlib import Path

project_root = Path.cwd()

knowledge_dir = project_root / "knowledge_storage"

os.environ["CREWAI_STORAGE_DIR"] = str(knowledge_dir)

And since I am first testing this out in my Jupyter notebook, I have to use the Jupyter-safe way of storing them, hence why I’m using `project_root = Path.cwd()`.

Otherwise, I would use `project_root = Path(__file__).parent` .

Now that I have the directory where I want it, I can now save my knowledge assets directly into all of my agents’ wee, little AI brains.🧠🧠🧠

![Image 6](https://miro.medium.com/v2/resize:fit:500/0*DcRRckNsN431PVk9.gif)

I ran this code to see if the LLM was working and if it knew “where” my `knowledge` directory was located:

import os

from openai import OpenAI

from dotenv import load_dotenv

import requests

def test_llm_connection():

 """Test if the LLM client can be initialized and make a simple request."""
load_dotenv()

print(f"Current working directory: {os.getcwd()}")

knowledge_dir = os.path.join(os.getcwd(), "knowledge")

 if os.path.exists(knowledge_dir):

 print(f"Files in knowledge directory:")

 for file in os.listdir(knowledge_dir):

 print(f" - {os.path.join(knowledge_dir, file)}")

 else:

 print(f"Knowledge directory not found at {knowledge_dir}")

ref_dir = os.path.join(os.getcwd(), "reference")

 if os.path.exists(ref_dir):

 print(f"Files in reference directory:")

 for file in os.listdir(ref_dir):

 print(f" - {os.path.join(ref_dir, file)}")

 else:

 print(f"Reference directory not found at {ref_dir}")

try:

 client = OpenAI(

 api_key=os.getenv("XAI_API_KEY"),

 base_url="https://api.x.ai/v1",

 )

completion = client.chat.completions.create(

 model="grok-3-mini",

 messages=[{"role": "user", "content": "Hello, Grok!"}],

 max_tokens=10

 )

print("XAI Client Test Results:")

 print(f"Response: {completion.choices[0].message.content}")

 print("LLM connection successful!")

return True

 except Exception as e:

 print(f"XAI client error: {e}")

try:

 client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(

 model="gpt-3.5-turbo",

 messages=[{"role": "user", "content": "Hello!"}],

 max_tokens=10

 )

print("OpenAI Client Test Results:")

 print(f"Response: {completion.choices[0].message.content}")

 print("LLM connection successful with OpenAI fallback!")

return True

 except Exception as e2:

 print(f"OpenAI client error: {e2}")

 return False

if __name__ == "__main__":

 test_llm_connection()

And when I ran it, it listed where everything was and that my LLM was able to connect to the mothership:

Current working directory: /Users/user_name/Documents/AI Social Media Agency

Files in knowledge directory:

 - /Users/user_name/Documents/AI Social Media Agency/knowledge/content_guidelines.txt

 - /Users/user_name/Documents/AI Social Media Agency/knowledge/acmes_brand_kit.txt

XAI Client Test Results:

Response: 

LLM connection successful!
Now it’s time to bring in the Knowledge!

You will need a library call and what kind of source you are bringing in, as the knowledge source call will be different [depending on what type of file](http://docs.crewai.com/concepts/knowledge#supported-knowledge-sources) you decide to use, in my case I am using `.txt` files.

from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
Then, define the sources.

content_guidelines_source = TextFileKnowledgeSource(

 file_paths=["content_guidelines.txt"]

)brand_kit_source = TextFileKnowledgeSource(

 file_paths=["acmes_brand_kit.txt"]

)
Finally, I assign the `TextFileKnowledgeSource` at the agent or crew level. You will use the `knowledge_sources`parameter for both.

Here it is at the crew level, where all the agents have access to that same knowledge that they should all make use of.

content_creation_crew = Crew (

 agents=[

 content_analyst_agent, 

 some_other_agent,

 ...

 ],

 tasks=[

 content_analysis_task,

 some_other_task,

 ...

 ],

 knowledge_sources=[acme_brand_kit_source] 

)
Here’s my set up for just one of my agent’s:

content_creator_agent = Agent(

 config=agents_config['content_creator_agent'], 

 

 knowledge_sources=[content_guidelines_source] 

![Image 7](https://miro.medium.com/v2/resize:fit:480/0*bQ8NHiW_P1HO6GPL.gif)

And just like that, they know how to analyze an article for my blog or transcript in the way I want them to, so they can parse the content the “right” way for posts, while also using the brand kit that I gave them and what they should be analyzing for — before outputting anything.

Now it’s time to test and observe, by feeding them one of my articles and seeing what they do with it.

![Image 8](https://miro.medium.com/v2/resize:fit:400/0*bpRxxy9Yq8Pp-pW6.gif)

The results…

![Image 9](https://miro.medium.com/v2/resize:fit:400/0*74cEVM2cIbQV46hA.gif)

…are so much better than I had hoped. 🙌

I can now give them updates to their Knowledge at either the agent or crew level, and if I need to modify their behavior — I can at any time!

Since I’ve given them some Knowledge, they really don’t hallucinate very much and they don’t get stuck in “thinking” mode, plus setting the LLM temperature to zero also helps with getting a consistent output every time.

The crew is almost ready for battle… er, production.

But first I need to convert this social media crew from my Jupyter notebook into a “real” program, so if you want to begin watching the series — check out my Youtube video on how I setup the project.

The only way to really see if they are successful is to use what they output by track the KPIs over time and releasing them into the wild to see if others might find them as useful as I do, but that’s for another article.

So stay tuned.

## References

*   [CrewAI Knowledge](https://docs.crewai.com/concepts/knowledge)
*   [Pydantic](https://docs.pydantic.dev/latest/)
