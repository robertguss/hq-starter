---
tags:
  - library
title: "Neo4j LLM Knowledge Graph Builder - Extract Nodes and Relationships from Unstructured Text - Neo4j Labs"
url: "https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/"
company: [personal]
topics: []
created: 2025-05-31
source_type: raindrop
raindrop_id: 1122228603
source_domain: "neo4j.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Neo4j LLM Knowledge Graph Builder - Extract Nodes and Relationships from Unstructured Text - Neo4j Labs

URL Source: https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/

Markdown Content:
# Neo4j LLM Knowledge Graph Builder - Extract Nodes and Relationships from Unstructured Text - Neo4j Labs

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#)[Use necessary cookies only](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#)

[![Image 2: Neo4j Developer Portal](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)[Labs](https://neo4j.com/labs/)

[Docs](https://neo4j.com/docs/)

Neo4j DBMS
*   [Getting Started](https://neo4j.com/docs/getting-started/current/)
*   [Operations](https://neo4j.com/docs/operations-manual/current/)
*   [Migration and Upgrade](https://neo4j.com/docs/migration-guide/current/)
*   [Status Codes](https://neo4j.com/docs/status-codes/current/)
*   [Java Reference](https://neo4j.com/docs/java-reference/current/)
*   [Kerberos Add-on](https://neo4j.com/docs/kerberos-add-on/current/)

[Neo4j Aura](https://neo4j.com/docs/aura/)

Neo4j Tools
*   [Neo4j Bloom](https://neo4j.com/docs/bloom-user-guide/current/)
*   [Neo4j Browser](https://neo4j.com/docs/browser/)
*   [Neo4j Data Importer](https://neo4j.com/docs/data-importer/current/)
*   [Neo4j Desktop](https://neo4j.com/docs/desktop-manual/current/)
*   [Neo4j Ops Manager](https://neo4j.com/docs/ops-manager/current/)
*   [Neodash commercial](https://neo4j.com/docs/neodash-commercial/current/)

Neo4j Graph Data Science
*   [Neo4j Graph Data Science Library](https://neo4j.com/docs/graph-data-science/current/)
*   [Neo4j Graph Data Science Client](https://neo4j.com/docs/graph-data-science-client/current/)
*   [Neo4j Graph Analytics for Snowflake](https://neo4j.com/docs/snowflake-graph-analytics/current/)

Cypher Query Language
*   [Cypher](https://neo4j.com/docs/cypher-manual/current/)
*   [Cypher Cheat Sheet](https://neo4j.com/docs/cypher-cheat-sheet/current/)
*   [APOC Library](https://neo4j.com/docs/apoc/current/)

Generative AI
*   [Neo4j GraphRAG for Python](https://neo4j.com/docs/neo4j-graphrag-python/current/)
*   [Embeddings and vector indexes tutorial](https://neo4j.com/docs/genai/tutorials/current/embeddings-vector-indexes/)
*   [GenAI plugin](https://neo4j.com/docs/genai/plugin/current/)
*   [Vector search indexes](https://neo4j.com/docs/cypher-manual/current/indexes/semantic-indexes/vector-indexes/)
*   [Vector search functions](https://neo4j.com/docs/cypher-manual/current/functions/vector/)
*   [GraphQL vector index search documentation](https://neo4j.com/docs/graphql/current/directives/indexes-and-constraints/#_vector_index_search)

Create applications
*   [Python Driver](https://neo4j.com/docs/python-manual/current/)
*   [Go Driver](https://neo4j.com/docs/go-manual/current/)
*   [Java Driver](https://neo4j.com/docs/java-manual/current/)
*   [JDBC Driver](https://neo4j.com/docs/jdbc-manual/current/)
*   [JavaScript Driver](https://neo4j.com/docs/javascript-manual/current/)
*   [.Net Driver](https://neo4j.com/docs/dotnet-manual/current/)
*   [Neo4j GraphQL Library](https://neo4j.com/docs/graphql-manual/current/)
*   [Neo4j Visualization Library](https://neo4j.com/docs/nvl/current/)
*   [OGM Library](https://neo4j.com/docs/ogm-manual/current/)
*   [Spring Data Neo4j](https://docs.spring.io/spring-data/neo4j/docs/current/reference/html/#reference)
*   [HTTP API](https://neo4j.com/docs/http-api/current/)
*   [Neo4j Query API](https://neo4j.com/docs/query-api/current/)
*   [Bolt](https://neo4j.com/docs/bolt/current/)

Connect data sources
*   [Neo4j Connector for Apache Spark](https://neo4j.com/docs/spark/current/)
*   [Neo4j Connector for Apache Kafka](https://neo4j.com/docs/kafka/)
*   [Change Data Capture (CDC)](https://neo4j.com/docs/cdc/)
*   [BigQuery to Neo4j](https://neo4j.com/docs/dataflow-bigquery/)
*   [Google Cloud to Neo4j](https://neo4j.com/docs/dataflow-google-cloud/)

[Labs](https://neo4j.com/labs/)

[GenAI Ecosystem](https://neo4j.com/labs/genai-ecosystem/)
*   [LLM Knowledge Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/)
*   [Vector Index & Search](https://neo4j.com/labs/genai-ecosystem/vector-search/)
*   [LangChain](https://neo4j.com/labs/genai-ecosystem/langchain/)
*   [LangChain.js](https://neo4j.com/labs/genai-ecosystem/langchain-js/)
*   [LlamaIndex](https://neo4j.com/labs/genai-ecosystem/llamaindex/)
*   [Haystack](https://neo4j.com/labs/genai-ecosystem/haystack/)
*   [DSPy](https://neo4j.com/labs/genai-ecosystem/dspy/)

**Developer Tools**
*   [APOC Extended](https://neo4j.com/labs/apoc/)
*   [Aura CLI](https://neo4j.com/labs/aura-cli/)
*   [arrows.app](https://neo4j.com/labs/arrows/)
*   [Cypher Workbench](https://neo4j.com/labs/cypher-workbench/)
*   [ETL Tool](https://neo4j.com/labs/etl-tool/)
*   [NeoDash](https://neo4j.com/labs/neodash/)

**Frameworks & Integrations**
*   [Needle Starter Kit](https://neo4j.com/labs/neo4j-needle-starterkit/)
*   [Neo4j Plugin for Liquibase](https://neo4j.com/labs/liquibase/)
*   [Neo4j Migrations](https://neo4j.com/labs/neo4j-migrations/)
*   [neomodel](https://neo4j.com/labs/neomodel/)

[RDF & Linked Data](https://neo4j.com/labs/neosemantics/)
*   [Neosemantics (Java)](https://neo4j.com/labs/neosemantics/)
*   [RDFLib-Neo4j (Python)](https://neo4j.com/labs/rdflib-neo4j/)

[Get Help](https://neo4j.com/developer/resources/)

[Community Forum](https://dev.neo4j.com/forum)

[Discord Chat](https://dev.neo4j.com/chat)

[Product Support](http://support.neo4j.com/)

[Neo4j Developer Blog](https://neo4j.com/blog/developer/)

[Neo4j Videos](https://neo4j.com/videos/)

[GraphAcademy](https://graphacademy.neo4j.com/?ref=docs-nav)

[Beginners Courses](https://graphacademy.neo4j.com/categories/beginners/?ref=docs-nav)
*   [Neo4j Fundamentals](https://graphacademy.neo4j.com/courses/neo4j-fundamentals/?ref=docs-nav)
*   [Cypher Fundamentals](https://graphacademy.neo4j.com/courses/cypher-fundamentals/?ref=docs-nav)
*   [Importing Data Fundamentals](https://graphacademy.neo4j.com/courses/importing-fundamentals/?ref=docs-nav)
*   [Importing CSV Data](https://graphacademy.neo4j.com/courses/importing-csv-data/?ref=docs-nav)
*   [Graph Data Modeling](https://graphacademy.neo4j.com/courses/modeling-fundamentals/?ref=docs-nav)

[Data Scientist Courses](https://graphacademy.neo4j.com/categories/data-scientist/?ref=docs-nav)
*   [Into to Graph Data Science](https://graphacademy.neo4j.com/courses/gds-product-introduction/?ref=docs-nav)
*   [Graph Data Science Fundamentals](https://graphacademy.neo4j.com/courses/graph-data-science-fundamentals/?ref=docs-nav)
*   [Path Finding](https://graphacademy.neo4j.com/courses/gds-shortest-paths/?ref=docs-nav)

[Generative AI Courses](https://graphacademy.neo4j.com/categories/llms/?ref=docs-nav)
*   [Neo4j & LLM Fundamentals](https://graphacademy.neo4j.com/courses/llm-fundamentals/?ref=docs-nav)
*   [Vector Indexes & Unstructured Data](https://graphacademy.neo4j.com/courses/llm-vectors-unstructured/?ref=docs-nav)
*   [Build a Chatbot with Python](https://graphacademy.neo4j.com/courses/llm-chatbot-python/?ref=docs-nav)
*   [Build a Chatbot with TypeScript](https://graphacademy.neo4j.com/courses/llm-chatbot-typescript/?ref=docs-nav)

[Neo4j Certification](https://graphacademy.neo4j.com/certification/?ref=docs-nav)
*   [Neo4j Certified Professional](https://graphacademy.neo4j.com/certifications/neo4j-certification/?ref=docs-nav)
*   [Neo4j Graph Data Science Certification](https://graphacademy.neo4j.com/certifications/gds-certification/?ref=docs-nav)

[Get Started Free](https://console.neo4j.io/?ref=docs-nav-get-started)

Theme

Light

Dark

[Search](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#search)

[Skip to content](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#skip-to-content "Skip to content")

Neo4j Labs

*       *   [Labs Home](https://neo4j.com/labs/)

*       *   [Neo4j Aura Terraform Provider](https://neo4j.com/labs/neo4j-aura-terraform-provider/)

*       *   [GenAI Ecosystem](https://neo4j.com/labs/genai-ecosystem/)
        *   Labs Projects
            *   [MCP Servers](https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/)
            *   [LLM Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/)
                *   [Features](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder-features/)
                *   [Deployment](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder-deployment/)

            *   [GraphRAG Demo](https://neo4j.com/labs/genai-ecosystem/rag-demo/)
            *   [NeoConverse](https://neo4j.com/labs/genai-ecosystem/neoconverse/)
            *   [GenAI Stack](https://neo4j.com/labs/genai-ecosystem/genai-stack/)

        *   Neo4j GenAI Features
            *   [GraphRAG Python Package](https://neo4j.com/developer/genai-ecosystem/graphrag-python/)
            *   [Vector Index and Search](https://neo4j.com/developer/genai-ecosystem/vector-search/)
            *   [APOC GenAI](https://neo4j.com/labs/genai-ecosystem/apoc-genai/)

        *   Cloud Examples
            *   [AWS Bedrock](https://neo4j.com/labs/genai-ecosystem/aws-demo/)
            *   [Microsoft Azure OpenAI](https://neo4j.com/labs/genai-ecosystem/microsoft-azure-demo/)
            *   [Google Cloud Vertex AI](https://neo4j.com/labs/genai-ecosystem/google-cloud-demo/)

        *   [GenAI Frameworks](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/)
            *   [LangChain](https://neo4j.com/labs/genai-ecosystem/langchain/)
            *   [LangChainJS](https://neo4j.com/labs/genai-ecosystem/langchain-js/)
            *   [LlamaIndex](https://neo4j.com/labs/genai-ecosystem/llamaindex/)
            *   [SpringAI](https://neo4j.com/labs/genai-ecosystem/spring-ai/)
            *   [LangChain4j](https://neo4j.com/labs/genai-ecosystem/langchain4j/)
            *   [Haystack](https://neo4j.com/labs/genai-ecosystem/haystack/)
            *   [MCP Toolbox](https://neo4j.com/labs/genai-ecosystem/mcp-toolbox/)
            *   [Genkit](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#genkitx-neo4j)

        *   [Agent Frameworks](https://neo4j.com/labs/genai-ecosystem/agent-frameworks/)
            *   [LangChain](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/langchain-agents/)
            *   [LlamaIndex](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/llamaindex-agents/)
            *   [LangGraph](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/langgraph/)
            *   [OpenAI Agents SDK](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/openai-agents/)
            *   [AWS Strands Agents](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/aws-strands-agents/)
            *   [Pydantic AI](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/pydantic-ai/)
            *   [Claude Agent SDK](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/claude-agent/)
            *   [Microsoft Agent Framework](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/microsoft-agent-framework/)
            *   [Google ADK](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/google-adk/)

        *   [Agent Platforms](https://neo4j.com/labs/genai-ecosystem/agent-platforms/)
            *   [AWS AgentCore](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/aws-agentcore/)
                *   [MCP Runtime (Docker)](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/aws-agentcore-mcp-docker/)
                *   [Gateway + External MCP](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/aws-agentcore-gateway/)
                *   [MCP Runtime (Neo4j SDK)](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/aws-agentcore-neo4j-sdk/)
                *   [Marketplace (CLI)](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/aws-agentcore-marketplace/)

            *   [Microsoft Foundry](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/microsoft-foundry/)
            *   [Databricks Agent Bricks](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/databricks-agent-bricks/)
                *   [UC Functions](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/databricks-uc-functions/)
                *   [Custom MCP Server](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/databricks-custom-mcp/)
                *   [Official MCP Server](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/databricks-official-mcp/)

            *   [Google Gemini Enterprise](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/google-gemini-enterprise/)
                *   [A2A MCP Wrapper](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/google-gemini-a2a-mcp-wrapper/)
                *   [A2A Direct Service](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/google-gemini-a2a-direct/)
                *   [GE Marketplace](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#genai-frameworks/google-gemini-ge-marketplace.adoc)

            *   [Salesforce Agentforce](https://neo4j.com/labs/genai-ecosystem/genai-frameworks/salesforce-agentforce/)

*       *   [APOC](https://neo4j.com/labs/apoc/)
        *   Documentation
            *   [5 - Core](https://neo4j.com/docs/apoc/current)
            *   [5 - Extended](https://neo4j.com/labs/apoc/5)
            *   [4.4](https://neo4j.com/labs/apoc/4.4)
            *   [4.3](https://neo4j.com/labs/apoc/4.3)

*       *   [Arrows](https://neo4j.com/labs/arrows/)
        *   [Launch Arrows](https://arrows.app/)

*       *   [Aura CLI](https://neo4j.com/labs/aura-cli/)
        *   Documentation
            *   [1.0](https://neo4j.com/labs/aura-cli/1.0)

*       *   [Cypher Workbench](https://neo4j.com/labs/cypher-workbench/)
        *   Documentation
            *   [Cypher Workbench Documentation](https://help.neo4j.solutions/neo4j-solutions/cypher-workbench/)

*       *   [Keymaker](https://neo4j.com/labs/keymaker/)
        *   Documentation
            *   [Keymaker Documentation](https://help.neo4j.solutions/neo4j-solutions/keymaker/)

*       *   [Neo4j ETL Tool](https://neo4j.com/labs/etl-tool/)
        *   [Documentation](https://neo4j.com/labs/etl-tool/1.5.0/)

*       *   [Halin](https://neo4j.com/labs/halin/)
        *   [Documentation](https://r.neo4j.com/halin)

*       *   [Liquibase](https://neo4j.com/labs/liquibase/)
        *   [Start using Liquibase](https://github.com/liquibase/liquibase-neo4j)

*       *   [Neo4j-Migrations](https://neo4j.com/labs/neo4j-migrations/)
        *   Documentation
            *   [2.0 (snapshot)](https://neo4j.com/labs/neo4j-migrations/2.0)

*       *   [Needle Starter Kit](https://neo4j.com/labs/neo4j-needle-starterkit/)
        *   Documentation
            *   [2.1](https://neo4j.com/labs/neo4j-needle-starterkit/2.1)

*       *   [NeoDash](https://neo4j.com/labs/neodash/)
        *   Documentation
            *   [2.4](https://neo4j.com/labs/neodash/2.4)

*       *   [neomodel](https://neo4j.com/labs/neomodel/)
        *   Documentation
            *   [4.0.10](https://neomodel.readthedocs.io/en/latest/)

*       *   [Neosemantics](https://neo4j.com/labs/neosemantics/)
        *   [Introduction](https://neo4j.com/labs/neosemantics/)
        *   [Installation](https://neo4j.com/labs/neosemantics/installation/)
        *   [Getting Started](https://neo4j.com/labs/neosemantics/tutorial/)
        *   [How To Guide](https://neo4j.com/labs/neosemantics/how-to-guide/)
        *   [Troubleshooting](https://neo4j.com/labs/neosemantics/troubleshooting/)
        *   [Graph App](https://neo4j.com/labs/neosemantics/graph-app/)
        *   [Acknowledgements](https://neo4j.com/labs/neosemantics/acknowledgements/)
        *   Documentation
            *   [4.3 (Current)](https://neo4j.com/labs/neosemantics/4.3)
            *   [4.2](https://neo4j.com/labs/neosemantics/4.2)
            *   [4.1](https://neo4j.com/labs/neosemantics/4.1)
            *   [4.0](https://neo4j.com/labs/neosemantics/4.0)
            *   [3.5](https://neo4j.com/docs/labs/nsmntx/3.5/)

*       *   [RDFlib-Neo4j](https://neo4j.com/labs/rdflib-neo4j/)
        *   Documentation
            *   [1.1](https://neo4j.com/labs/rdflib-neo4j/1.1)

*       *   [Neo4j-Spatial](https://neo4j.com/labs/spatial/)
        *   [Documentation](https://neo4j.com/labs/neo4j-spatial/5)

**Is this page helpful?**

*   [Neo4j Labs](https://neo4j.com/labs/)
*   [GenAI Ecosystem](https://neo4j.com/labs/genai-ecosystem/)
*    Labs Projects 
*   [LLM Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/)

[Edit this page](https://github.com/neo4j-documentation/labs-pages/edit/publish/modules/genai-ecosystem/pages/llm-graph-builder.adoc)

# Neo4j LLM Knowledge Graph Builder - Extract Nodes and Relationships from Unstructured Text

[![Image 3: build kg genai e1718732751482](https://dist.neo4j.com/wp-content/uploads/20240618104511/build-kg-genai-e1718732751482.png)](https://llm-graph-builder.neo4jlabs.com/)

The Neo4j LLM Knowledge Graph Builder is an [online application](https://llm-graph-builder.neo4jlabs.com/) for turning unstructured text into a knowledge graph, it provides a magical text to graph experience.

It uses ML models (LLM - OpenAI, Gemini, Llama3, Diffbot, Claude, Qwen) to transform PDFs, documents, images, web pages, and YouTube video transcripts. The extraction turns them into a lexical graph of documents and chunks (with embeddings) and an entity graph with nodes and their relationships, which are both stored in your Neo4j database. You can configure the extraction schema and apply clean-up operations after the extraction.

Afterwards you can use different RAG approaches (GraphRAG, Vector, Text2Cypher) to ask questions of your data and see how the extracted data is used to construct the answers.

*   best results for files with long-form text in English

*   less well suited for tabular data like Excel or CSV or images/diagrams/slides

*   higher quality data extraction if you configure the graph schema for nodes and relationship types

The front-end is a React Application and the back-end a Python FastAPI application running on Google Cloud Run, but you can deploy it locally using docker compose. It uses the [llm-graph-transformer module](https://python.langchain.com/docs/use_cases/graph/constructing) that Neo4j contributed to LangChain and other langchain integrations (e.g. for GraphRAG search).

All Features are documented in detail here: [Features documentation](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder-features/)

Here is a quick demo:

## [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_step_by_step_instructions)Step by Step Instructions

1.   Open the [LLM-Knowledge Graph Builder](https://llm-graph-builder.neo4jlabs.com/)

2.   Connect to a [Neo4j (Aura)](https://console.neo4j.io/) instance

3.   Provide your PDFs, Documents, URLs or S3/GCS buckets

4.   Construct Graph with the selected LLM

5.   Visualize Knowledge Graph in App

6.   Chat with your data using GraphRAG

7.   Open Neo4j Bloom for further visual exploration

8.   Use the constructed knowledge graph in your applications

![Image 4: llm graph builder viz](https://neo4j.com/labs/genai-ecosystem/_images/llm-graph-builder-viz.png)

*   Login, or create an account at [https://console.neo4j.io](https://console.neo4j.io/)

*   Under Instances, create a new AuraDB Free Database

*   Downloads the credentials file

*   Wait until the instance is running

*   Drop the credentials file on the connect dialog for the LLM Graph Builder

## [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_how_it_works)How it works

1.   Uploaded Sources are stored as `Document` nodes in the graph

2.   Each document (type) is loaded with the LangChain Loaders

3.   The content is split into Chunks

4.   Chunks are stored in the graph and connected to the Document and to each other for advanced RAG patterns

5.   Highly similar Chunks are connected with a `SIMILAR` relationship to form a kNN Graph

6.   Embeddings are computed and stored in the Chunks and Vector index

7.   Using the llm-graph-transformer or diffbot-graph-transformer entities and relationships are extracted from the text

8.   Entities and relationships are stored in the graph and connected to the originating Chunks

![Image 5: retrieval information e1718732797663](https://dist.neo4j.com/wp-content/uploads/20240618104514/retrieval-information-e1718732797663.png)

## [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_relevant_links)Relevant Links

Online Application[https://llm-graph-builder.neo4jlabs.com/](https://llm-graph-builder.neo4jlabs.com/)
Authors Michael Hunger, Tomaz Bratanic, Niels De Jong, Morgan Senechal, Persistent Team
Community Support[Neo4j Online Community](https://community.neo4j.com/c/neo4j-graph-platform/genai/214)
Repository[GitHub](https://github.com/neo4j-labs/llm-graph-builder)
Issues[GitHub Issues](https://github.com/neo4j-labs/llm-graph-builder/issues)
LangChain[LangChain KG Construction Module](https://python.langchain.com/v0.1/docs/use_cases/graph/constructing/)

## [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_installation)Installation

The [LLM Knowledge Graph Builder Application](https://llm-graph-builder.neo4jlabs.com/) is available online.

You can also run it locally, by cloning the [GitHub repository](https://github.com/neo4j-labs/llm-graph-builder) and following the instructions in the README.md file.

It is using Docker for packaging front-end and back-end, and you can run `docker-compose up` to start the whole application.

Local deployment and configuration details are available in the [Documentation for local deployments](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder-deployment/)

## [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_blog_posts)Blog Posts

*   [Introduction to the Neo4j LLM Knowledge Graph Builder](https://neo4j.com/blog/developer/llm-knowledge-graph-builder/)

*   [Community summaries, Parallel retrievers, more Models](https://neo4j.com/blog/developer/llm-knowledge-graph-builder-release/)

*   [Back-End Architecture and API Overview](https://neo4j.com/blog/developer/llm-knowledge-graph-builder-back-end/)

*   [Front-End Architecture](https://neo4j.com/blog/developer/frontend-architecture-and-integration/)

*   [Graph Extraction and Challenges](https://neo4j.com/blog/developer/knowledge-graph-extraction-challenges/)

*   [LLM Knowledge Graph Builder: From Zero to GraphRAG in Five Minutes](https://neo4j.com/blog/developer/graphrag-llm-knowledge-graph-builder/)

## [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_videos_tutorials)Videos & Tutorials

[![Image 6: llm knowledge graph construction](https://cdn.graphacademy.neo4j.com/assets/img/courses/banners/llm-knowledge-graph-construction.png)](https://graphacademy.neo4j.com/courses/llm-knowledge-graph-construction/)

### [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_detailed_walk_through)Detailed Walk-Through

### [](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_livestream_llm_knowledge_graph_builder)Livestream LLM-Knowledge Graph Builder

[GenAI Ecosystem](https://neo4j.com/labs/genai-ecosystem/)[Features](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder-features/)

## Contents

*   [Step by Step Instructions](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_step_by_step_instructions)
*   [How it works](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_how_it_works)
*   [Relevant Links](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_relevant_links)
*   [Installation](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_installation)
*   [Blog Posts](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_blog_posts)
*   [Videos & Tutorials](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_videos_tutorials)
*   [Detailed Walk-Through](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_detailed_walk_through)
*   [Livestream LLM-Knowledge Graph Builder](https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/#_livestream_llm_knowledge_graph_builder)

[Learn](https://graphacademy.neo4j.com/categories/llms/?ref=genai-docs)

## [Neo4j Developer Survey Your input matters! Share your Feedback Start Here](https://neo4j.typeform.com/to/E6yOZ2Py?utm_source=GA&utm_medium=blurb&utm_campaign=survey)

## Learn

*   [Sandbox](https://neo4j.com/sandbox/?ref=developer-footer)
*   [Neo4j Community Site](https://community.neo4j.com/?ref=developer-footer)
*   [Neo4j Developer Blog](https://medium.com/neo4j)
*   [Neo4j Videos](https://www.youtube.com/neo4j)
*   [GraphAcademy](https://neo4j.com/graphacademy/?ref=developer-footer)
*   [Neo4j Labs](https://neo4j.com/labs/?ref=developer-footer)

## Social

*   [Twitter](https://twitter.com/neo4j)
*   [Meetups](https://www.meetup.com/Neo4j-Online-Meetup/)
*   [Github](https://github.com/neo4j/neo4j)
*   [Stack Overflow](https://stackoverflow.com/questions/tagged/neo4j)
*   [Want to Speak?](https://docs.google.com/forms/d/e/1FAIpQLSdEcNnMruES5iwvOVYovmS1D_P1ZL_HdUOitFrwrvruv5PZvA/viewform)

## [Contact Us →](https://neo4j.com/contact-us/?ref=footer)

*   US: 1-855-636-4532
*   Sweden +46 171 480 113
*   UK: +44 20 3868 3223
*   France: +33 (0) 1 88 46 13 20

© 2026 Neo4j, Inc.

[Terms](https://neo4j.com/terms/) | [Privacy](https://neo4j.com/privacy-policy/) | [Sitemap](https://neo4j.com/sitemap/)

Neo4j®, Neo Technology®, Cypher®, Neo4j® Bloom™ and Neo4j® Aura™ are registered trademarks of Neo4j, Inc. All other marks are owned by their respective companies.

![Image 7](blob:https://neo4j.com/e819e39c-e660-450d-b8bf-d42c9a0325d6)
