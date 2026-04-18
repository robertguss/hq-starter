---
tags:
  - library
title: "Three Books You Should Read to Improve Your AI Knowledge"
url: "https://medium.datadriveninvestor.com/three-books-you-should-read-to-improve-your-ai-knowledge-d268e9e1ec4e"
company: [personal]
topics: []
created: 2025-08-31
source_type: raindrop
raindrop_id: 1320007327
source_domain: "medium.datadriveninvestor.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Three resources to learn more about Retrieval Augmented Generation (RAG), LangChain, and Multi-Agent systems

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Three Books You Should Read to Improve Your AI Knowledge

URL Source: https://medium.datadriveninvestor.com/three-books-you-should-read-to-improve-your-ai-knowledge-d268e9e1ec4e

Published Time: 2025-03-25T11:19:27Z

Markdown Content:
## Books, Artificial Intelligence

## Three resources to learn more about Retrieval Augmented Generation (RAG), LangChain, and Multi-Agent systems

[![Image 1: Angelica Lo Duca](https://miro.medium.com/v2/resize:fill:64:64/1*aJAYMw9TJpvhBsfQHE4WZw.jpeg)](https://alod83.medium.com/?source=post_page---byline--d268e9e1ec4e---------------------------------------)

9 min read

Mar 25, 2025

Press enter or click to view image in full size

![Image 2](https://miro.medium.com/v2/resize:fit:700/1*3oxF9YJjVIZMlc896qT2GQ.png)

Image by Author

Lately, AI-related concepts such as RAG and multi-agent have been all the rage. Maybe we all know these words a little, but then we don’t fully understand how to implement and use these systems in practice. Personally, I see a lot of posts and links to exciting resources on social media, but they focus on a single aspect at a time.

Today, I propose three books, each addressing a different aspect of AI. If you read all three, you will have a complete picture of the current situation in the AI ​​world. The three books are:

*   [LangChain in Action](https://www.manning.com/books/langchain-in-action) by Roberto Infante
*   [Multi-Agent Systems with AutoGen](https://www.manning.com/books/multi-agent-systems-with-autogen) by Victor Dibia
*   [A Simple Guide to Retrieval Augmented Generation](https://www.manning.com/books/a-simple-guide-to-retrieval-augmented-generation) by Abhinav Kimothi

Let’s go through them individually, starting with the first one.

As a side note, I thank Manning Publications, who exclusively offered me these three books.

## 1. LangChain in Action by Roberto Infante

### Why You Should Read This Book

[_LangChain in Action_](https://www.manning.com/books/langchain-in-action) is a hands-on guide to developing powerful LLM-driven applications using [LangChain](https://www.langchain.com/), an open-source framework quickly becoming a favourite among AI practitioners. This book will help you understand how to build real-world applications by leveraging LangChain's modular and scalable architecture.

### What You Will Learn

**LangChain’s Core Architecture.**At its core, LangChain is built around the following modular components:

*   **Document Loaders** to extract data from files, APIs, or databases.
*   **Text Splitters** to break down documents into manageable chunks.
*   **Embedding Models** to convert text into vector representations.
*   **Vector Stores** for efficient retrieval.
*   **Retrievers and Prompts** to feed relevant information into LLMs.

Here’s how you might load and split a document using LangChain components in Python.

from langchain.document_loaders import TextLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
loader = TextLoader('example.txt')

documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

docs = splitter.split_documents(documents)

print(f"Number of chunks: {len(docs)}")

print(f"First chunk content: {docs[0].page_content}")

**Prompt Engineering and Programmatic Execution.**LangChain makes creating and executing prompts programmatically simple. Here’s an example of a basic question-answering prompt.

from langchain.prompts import PromptTemplate

from langchain.chat_models import ChatOpenAI
prompt = PromptTemplate.from_template(

 "Answer the following question concisely:\n\nQuestion: {question}"

)

llm = ChatOpenAI(model_name='gpt-3.5-turbo')

formatted_prompt = prompt.format(question="What is LangChain?")

response = llm.predict(formatted_prompt)

print(response)

**Creating a Simple RAG Q&A System.**LangChain simplifies Retrieval Augmented Generation (RAG), where an LLM retrieves relevant documents from a vector store to answer a question.

from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.vectorstores import Chroma

from langchain.chains import RetrievalQA
embeddings = OpenAIEmbeddings()

vectorstore = Chroma.from_documents(docs, embedding=embeddings)

retriever = vectorstore.as_retriever()

qa_chain = RetrievalQA.from_chain_type(

 llm=llm,

 chain_type="stuff", 

 retriever=retriever

)

question = "What is the purpose of LangChain?"

result = qa_chain.run(question)

print(result)

**Agentic Workflows with LangGraph.**For more complex use cases, such as multi-agent systems that collaborate to solve a task, _LangChain in Action_ introduces [**LangGraph**](https://www.langchain.com/langgraph).

Here’s a simplified conceptual example:

from langgraph.graph import StateGraph

from langchain.agents import create_openai_functions_agent

from langchain.tools import Tool
def search_tool(query: str):

 

 return f"Search result for '{query}'"

tool = Tool.from_function(

 func=search_tool,

 name="SearchTool",

 description="Tool to perform a search query."

)

agent = create_openai_functions_agent(

 llm=llm,

 tools=[tool]

)

graph = StateGraph()

graph.add_node(agent)

graph.add_edge(agent, agent) 

graph.finalize()

result = graph.invoke("Find the latest AI research papers.")

print(result)

### Who This Book Is For

*   Developers and data scientists looking to prototype or deploy LLM-powered applications quickly.
*   AI practitioners interested in Retrieval Augmented Generation and multi-agent workflows.
*   Anyone who wants a hands-on introduction to LangChain and its ecosystem.

Press enter or click to view image in full size

![Image 3](https://miro.medium.com/v2/resize:fit:700/1*mm9ZRDlX3RhferUJHvEsTg.png)

Image generated with DALL-E using this prompt: Generate a 16:9 image related to this topic: LangChain in Action.

## 2. Multi-Agent Systems with AutoGen by Victor Dibia

### Why You Should Read This Book

[_Multi-Agent Systems with AutoGen_](https://www.manning.com/books/multi-agent-systems-with-autogen) is an in-depth guide to building intelligent systems with multiple autonomous agents using the [AutoGen](https://microsoft.github.io/autogen/stable//index.html) framework. It offers foundational knowledge and practical techniques for designing, orchestrating, and deploying multi-agent AI systems that can reason, communicate, and act collaboratively.

### What You Will Learn

**Foundations of Multi-Agent Systems (MAS).**First, you’ll learn the core principles behind multi-agent systems: decentralized decision-making, collaboration, and autonomy. Next, you’ll learn how to decompose complex tasks into modular roles performed by distinct agents. Finally, the book will focus on key use cases: automated research assistants, dynamic task managers, and complex data analysis workflows.

**Introduction to AutoGen Framework.**AutoGen is an open-source framework designed to simplify the development of multi-agent AI systems by leveraging LLMs and enabling agents to:

*   Communicate asynchronously.
*   Share memory and tools.
*   Adapt their behavior based on feedback and external signals.

In the following example, two agents collaborate to complete a task: one agent acts as a **Planner**, the other as an **Executor**.

import autogen

from autogen import AssistantAgent, UserProxyAgent
assistant = AssistantAgent(

 name="ExecutorAgent",

 llm_config={"model": "gpt-4"}

)

planner = UserProxyAgent(

 name="PlannerAgent",

 code_execution_config={"work_dir": "workspace"}

)

planner.initiate_chat(

 assistant,

 message="Create a step-by-step plan to generate a data analysis report on recent AI research papers."

)

The **PlannerAgent** provides a high-level strategy. The **ExecutorAgent** uses its LLM capabilities to perform each step, such as retrieving data, analyzing it, and generating a report.

**Designing and Orchestrating Agent Teams.**The book guides you in:

*   Creating **interface agents** that interact with web apps, APIs, and OS systems.
*   Implementing **specialized agents** with specific roles (e.g., data gathering, summarization, validation).
*   Building **agent teams** that dynamically collaborate based on task complexity.

The following example implements a Multi-Agent Chat with Task Specialization:

data_retriever = AssistantAgent(

 name="DataRetrieverAgent",

 llm_config={"model": "gpt-4"}

)
data_analyzer = AssistantAgent(

 name="DataAnalyzerAgent",

 llm_config={"model": "gpt-4"}

)

planner.initiate_chat(

 [data_retriever, data_analyzer],

 message=(

 "DataRetrieverAgent, collect the latest AI publications from arXiv. "

 "DataAnalyzerAgent, analyze the collected data for key trends."

 )

)

**Evaluating and Optimizing Multi-Agent Systems.**In the book, you’ll learn how to benchmark and assess MAS performance using metrics like task completion rate, accuracy, and resource efficiency. You’ll also see how to fine-tune small models for specific agents. Finally, you’ll learn parallel processing and scaling agents across distributed systems.

## Get Angelica Lo Duca’s stories in your inbox

Join Medium for free to get updates from this writer.

Remember me for faster sign in

**Open Challenges and Responsible AI in MAS.**The book covers:

*   Trade-offs between controllability and agent autonomy.
*   Ethical concerns and security (e.g., preventing agents from unintended actions).
*   Continuous learning strategies to improve system adaptability.

### Who This Book Is For

*   AI engineers and researchers who want to build dynamic, scalable AI systems.
*   Developers seeking to move beyond single-model applications into collaborative agent ecosystems.
*   Practitioners interested in the future of autonomous AI and responsible multi-agent system design.

Press enter or click to view image in full size

![Image 4](https://miro.medium.com/v2/resize:fit:700/1*PbFqoac3NmG4d37oOuKmQg.png)

Image generated with DALL-E using the following prompt: Generate a 16:9 image related to this topic: Multi-Agent Systems with AutoGen

## 3. A Simple Guide to Retrieval Augmented Generation by Abhinav Kimothi

### Why You Should Read This Book

[_A Simple Guide to Retrieval Augmented Generation_](https://www.manning.com/books/a-simple-guide-to-retrieval-augmented-generation) by Abhinav Kimothi tackles these issues head-on by introducing Retrieval Augmented Generation (RAG). This powerful technique combines LLMs with external data sources to provide accurate, context-aware, and up-to-date answers.

This book is an excellent starting point for developers, AI practitioners, and anyone who wants to implement reliable AI systems. It offers a clear and practical guide to designing, building, and evaluating RAG-enabled applications.

### What You Will Learn

**Understanding RAG Fundamentals.**You’ll learn what RAG is and why it’s necessary: improving LLM reliability by augmenting their knowledge with external data. You’ll also understand how RAG addresses LLM limitations like hallucination and outdated information. Finally, you’ll implement use cases of RAG, from chatbots and document searches to scientific research assistants.

**Architecture of a RAG System.**The basic architecture of a RAG system includes:

*   **Indexing Pipeline**: How to ingest, preprocess, and store documents in a vector database.
*   **Retrieval Pipeline**: How to query relevant documents based on user input.
*   **Generation Pipeline**: Combining retrieved information with prompts to generate accurate responses.

**Evaluating RAG Systems.**You’ll learn to measure the accuracy, relevance, and faithfulness of generated answers. You’ll also deepen into techniques for evaluating retrieval and generation quality separately. Finally, you’ll see modular evaluation strategies to diagnose and improve different components of the RAG pipeline.

The following code evaluates retrieval precision by checking whether the correct documents are returned from the vector store before generation happens.

relevant_docs = retriever.get_relevant_documents("Explain RAG in simple terms")

for idx, doc in enumerate(relevant_docs):

 print(f"Document {idx + 1}: {doc.page_content[:200]}...")
**Advanced RAG Techniques and Production Considerations.**You’ll learn how to transition from simple prototypes to production-grade RAG systems. You’ll also deepen into advanced strategies, including graph-based RAG, multimodal RAG, and agentic RAG. You’ll build scalable indexing pipelines and modular generation pipelines for enterprise applications. Finally, the book also covers tools and frameworks like Chroma, Weaviate, LlamaIndex, and integrations with OpenAI and Hugging Face.

For example, you can enhance relevance by filtering documents based on metadata (e.g., date, source) through the following code:

filtered_docs = retriever.get_relevant_documents(

 "Explain RAG",

 filters={"source": "research_papers", "year": "2024"}

)
for doc in filtered_docs:

 print(doc.metadata, doc.page_content[:200])

### Who This Book Is For

*   AI developers who want to enhance the reliability of LLM-powered applications.
*   Data scientists and researchers working on information retrieval and knowledge management.
*   Product teams looking to deploy scalable and accurate AI-driven search and Q&A systems.

Press enter or click to view image in full size

![Image 5](https://miro.medium.com/v2/resize:fit:700/1*9cD6FtLpaYLuY1hlpQGAvg.png)

Image generated with DALL-E using the following prompt: Generate a 16:9 image related to this topic: A Simple Guide to Retrieval Augmented Generation

## Summary

Congratulations! You have just seen three books that deepen your understanding of hot AI topics: Retrieval Augmented Generation (RAG), multi-agent systems, and large language model (LLM) application frameworks. Each book focuses on a different but complementary area, offering both theoretical insights and practical, hands-on examples to help you implement these technologies effectively.

**LangChain in Action by Roberto Infante**

A practical guide to building LLM-powered applications using the LangChain framework. The book covers everything from prompt engineering to creating Retrieval Augmented Generation (RAG) systems and agentic workflows with LangGraph. It’s ideal for developers and data scientists interested in building scalable and modular AI solutions.

**Multi-Agent Systems with AutoGen by Victor Dibia**

This book delves into designing and implementing multi-agent AI systems using the AutoGen framework. It explains how to orchestrate multiple autonomous agents that can reason, communicate, and collaborate on complex tasks. It’s a must-read for AI engineers and researchers looking to develop dynamic, scalable multi-agent systems.

**A Simple Guide to Retrieval Augmented Generation by Abhinav Kimothi**

This book is a clear and accessible introduction to RAG. It explains how to enhance LLM reliability by integrating external knowledge bases. It guides readers through RAG systems' architecture, evaluation, and advanced strategies, making it perfect for AI practitioners and teams aiming to deploy robust and accurate AI solutions.

These three books offer a well-rounded view of today’s AI landscape. Whether you’re interested in building intelligent chatbots, orchestrating autonomous agent teams, or enhancing LLM outputs with external knowledge retrieval, these resources will help you take your AI expertise to the next level.

## Bonus Book

So far, the books you’ve seen describe AI-related technologies in generic contexts, with detailed examples. You can read my book [Data Storytelling with Altair and AI](https://www.manning.com/books/data-storytelling-with-altair-and-ai) if you want to apply these technologies to a specific case: data storytelling[. In it](https://www.manning.com/books/data-storytelling-with-altair-and-ai), I explain, among other things, how to use RAG and fine-tuning to generate comments to insert into data visualization charts.

Press enter or click to view image in full size

![Image 6](https://miro.medium.com/v2/resize:fit:700/1*cpEDBSGJXqoflKr4d6AodQ.png)

A screenshot from the book Data Storytelling with Altair and AI, by Manning Publications.

Watch the following video to learn more…

## You may also be interested in…
