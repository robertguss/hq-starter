---
tags:
  - library
title: "Implementing Advanced Retrieval RAG Strategies With Neo4j"
url: "https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/"
company: [personal]
topics: []
created: 2025-03-24
source_type: raindrop
raindrop_id: 998927969
source_domain: "neo4j.com"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

In this blog, you will learn how to use the neo4j-advanced-rag template in LangServe Playground to implement advanced RAG strategies.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Developer Archives

URL Source: https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/

Markdown Content:
# Developer Archives - Graph Database & Analytics

This website uses cookies

We use cookies to offer you a better browsing experience, analyze site traffic, personalize content and serve targeted ads. Learn about how we use cookies and how you can control them in [Cookie Settings](https://neo4j.com/neo4j-cookie-and-tracking-policy/). By using our site. you consent to our use of cookies.

[Accept Cookies](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/#)[Use necessary cookies only](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/#)

[Skip to content](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/#skip-to-content "Skip to content")

Complete the [opens in new tab Aura Agents Course](https://graphacademy.neo4j.com/courses/aura-agents/?category=aura) Between Apr 15 - May 15 | The First 500 Win Aura Credits

[![Image 1: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)Menu

![Image 2: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)Search Close Menu

*   [Products](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Back](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   GRAPH DATABASE
    *   [Neo4j AuraDB Fully managed graph database as a service](https://neo4j.com/product/auradb/)
    *   [Neo4j Graph Database Self managed, deploy anywhere graph database](https://neo4j.com/product/neo4j-graph-database/)
    *   GRAPH ANALYTICS
    *   [Neo4j Aura Graph Analytics Fully managed graph analytics as a service](https://neo4j.com/product/aura-graph-analytics/)
    *   [Neo4j Graph Data Science Self managed graph algorithms and ML modeling](https://neo4j.com/product/graph-data-science/)
    *   GRAPH AI
    *   [Neo4j Aura Agent Fully managed knowledge-graph-powered AI agent creation platform](https://neo4j.com/product/aura-agent/)
    *   GRAPH TOOLS
    *   [Neo4j Fleet Manager A single control plane to manage all your DB instances](https://neo4j.com/product/fleet-manager/)
    *   [Neo4j Bloom Easy graph visualization and exploration](https://neo4j.com/product/bloom/)
    *   PARTNER SOLUTIONS
    *   [Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud](https://neo4j.com/neo4j-graph-analytics-snowflake/)
    *   [Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric](https://neo4j.com/neo4j-graph-intelligence-microsoft-fabric/)

*   [Use Cases](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Back](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [AI Systems Back your LLMs with a knowledge graph for better business AI](https://neo4j.com/use-cases/ai-systems/)
    *   [Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more](https://neo4j.com/use-cases/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)

*   [Developers](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Back](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Developer Center Best practices, guides, tutorials, and downloads](https://neo4j.com/developer/)
    *   [opens in new tab GraphAcademy![Image 3](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications. Join the 100K+ Neo4j experts.](https://graphacademy.neo4j.com/)
    *   DEVELOPERS
    *   [Deployment Center Deploy Neo4j on any cloud or architecture](https://neo4j.com/deployment-center/)
    *   [Documentation![Image 4](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [Developer Blog Deep dives into more technical Neo4j topics](https://neo4j.com/blog/developer/)
    *   [opens in new tab Community A global forum for online discussion](https://community.neo4j.com/)
    *   DATA SCIENTISTS
    *   [Data Science Documentation![Image 5](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for the Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/)
    *   [Graph Data Science Home Learn what Neo4j offers for data science](https://neo4j.com/product/graph-data-science/)
    *   [Get Started With Graph Data Science Download or get started in Sandbox today](https://neo4j.com/graph-data-science-software/)
    *   [opens in new tab Data Science Community A global forum for data-driven professionals](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/)

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   [Learn](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Back](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   LEARN
    *   [Documentation![Image 6](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [GraphAcademy![Image 7](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications](https://graphacademy.neo4j.com/)
    *   [Resource Library White papers, datasheets, and more](https://neo4j.com/resources/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)
    *   CONNECT
    *   [Neo4j Events Hub![Image 8](https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg)Live and on-demand events, training, webinars, and demos](https://neo4j.com/events/)
    *   [Neo4j Blog Announcements, guides, and best practices](https://neo4j.com/blog/)
    *   [Neo4j Video Hub Covering graph databases, data science, analytics & AI](https://neo4j.com/videos/)
    *   FEATURED EVENTS
    *   [GraphSummit 2026 Graphs + AI: Transform Your Data Into Knowledge](https://neo4j.com/graphsummit/)
    *   [NODES 2026 | November 12 Virtual Conference: Engineering Better Intelligence](https://neo4j.com/nodes/)

*   [Pricing](https://neo4j.com/pricing/)
*   QUICK LINKS
*   [Partners](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Back](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Find a Partner](https://neo4j.com/partners/directory/)
    *   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
    *   [Solution Partners](https://neo4j.com/partners/solution-partners/)
    *   [OEM Partners](https://neo4j.com/partners/oem-partners/)
    *   [Technology Partners](https://neo4j.com/partners/technology-partners/)
    *   [Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

*   [Company](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [Back](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)
    *   [About Us](https://neo4j.com/company/)
    *   [Newsroom](https://neo4j.com/newsroom/)
    *   [Awards and Honors](https://neo4j.com/awards/)
    *   [Graphs4Good](https://neo4j.com/graphs4good/)
    *   [Careers](https://neo4j.com/careers/)
    *   [Culture](https://neo4j.com/culture/)
    *   [Leadership](https://neo4j.com/leadership/)

*   [Support](https://support.neo4j.com/s/)
*   [Aura Login](https://console.neo4j.io/)

[Get Started](https://neo4j.com/product/auradb/?ref=nav-get-started-cta)[Contact Us](https://neo4j.com/contact-us/)

*   [Aura Login](https://console.neo4j.io/)
*   [Partners](https://neo4j.com/partners/)Partners: submenu

    *   [Find a Partner](https://neo4j.com/partners/directory/)
    *   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
    *   [Solution Partners](https://neo4j.com/partners/solution-partners/)
    *   [OEM Partners](https://neo4j.com/partners/oem-partners/)
    *   [Technology Partners](https://neo4j.com/partners/technology-partners/)
    *   [opens in new tab Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

*   Company Company: submenu

    *   [About Us](https://neo4j.com/company/)
    *   [Newsroom](https://neo4j.com/newsroom/)
    *   [Awards and Honors](https://neo4j.com/awards/)
    *   [Graphs4Good](https://neo4j.com/graphs4good/)
    *   [Careers](https://neo4j.com/careers/)
    *   [Culture](https://neo4j.com/culture/)
    *   [Leadership](https://neo4j.com/leadership/)

*   [Support](https://support.neo4j.com/s/)
*   Search

[![Image 9: Neo4j logo](https://dist.neo4j.com/wp-content/uploads/20230926084108/Logo_FullColor_RGB_TransBG.svg)](https://neo4j.com/)

*   Products Products: submenu

GRAPH DATABASE
    *   [![Image 10: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083548/aura.svg) Neo4j AuraDB Fully managed graph database as a service](https://neo4j.com/product/auradb/)
    *   [![Image 11: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083552/Neo4j_db.svg) Neo4j Graph Database Self managed, deploy anywhere graph database](https://neo4j.com/product/neo4j-graph-database/)

GRAPH ANALYTICS
    *   [![Image 12: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083556/networkmagnifier_chart.svg) Neo4j Aura Graph Analytics Fully managed graph analytics as a service](https://neo4j.com/product/aura-graph-analytics/)
    *   [![Image 13: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083550/Graph_data_science.svg) Neo4j Graph Data Science Self managed graph algorithms and ML modeling](https://neo4j.com/product/graph-data-science/)

GRAPH AI
    *   [![Image 14: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083551/neo4j_aura_agent.svg) Neo4j Aura Agent Fully managed knowledge-graph-powered AI agent creation platform](https://neo4j.com/product/aura-agent/)

 PARTNER SOLUTIONS 

    *   [![Image 15: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083554/Neo4j_on_Fabric.svg) Neo4j Graph Intelligence for Microsoft Fabric Fully managed graph database and analytics integrated in Fabric](https://neo4j.com/neo4j-graph-intelligence-microsoft-fabric/)

    *   [![Image 16: \"menu](https://dist.neo4j.com/wp-content/uploads/20260408083555/Neo4j_on_Snowflake.svg) Neo4j Graph Analytics for Snowflake Fully managed graph analytics within Snowflake AI Data Cloud](https://neo4j.com/neo4j-graph-analytics-snowflake/)

Graph Tools

    *   [Neo4j Fleet Manager A single control plane to manage all your DB instances](https://neo4j.com/product/fleet-manager/)
    *   [Neo4j Bloom Easy graph visualization and exploration](https://neo4j.com/product/bloom/)

*   Use Cases Use Cases: submenu

    *   [![Image 17](https://dist.neo4j.com/wp-content/uploads/20240329130329/genai.svg) AI Systems Back your LLMs with a Knowledge Graph for better business AI Learn More](https://neo4j.com/use-cases/ai-systems/)
    *   [Industries and Use Cases Fraud detection, knowledge graphs, financial services, and more All Use Cases](https://neo4j.com/use-cases/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more All Customer Stories](https://neo4j.com/customer-stories/)

*   Developers Developers: submenu

    *   [Developer Center Best practices, guides, tutorials, and downloads Learn More](https://neo4j.com/developer/)[opens in new tab GraphAcademy Free online courses and certifications. Join the 100K+ Neo4j experts. Learn More](https://graphacademy.neo4j.com/)
    *   Developers
        *   [Deployment Center Deploy Neo4j on any cloud or architecture](https://neo4j.com/deployment-center/)
        *   [Documentation![Image 18](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
        *   [Developer Blog Deep dives into more technical Neo4j topics](https://neo4j.com/blog/developer/)
        *   [opens in new tab Community A global forum for online discussion](https://community.neo4j.com/)

DATA SCIENTISTS

    *   [Data Science Documentation![Image 19](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for the Graph Data Science library](https://neo4j.com/docs/graph-data-science/current/)
    *   [Graph Data Science Home Learn what Neo4j offers for data science](https://neo4j.com/product/graph-data-science/)
    *   [Get Started With Graph Data Science Download or get started in Sandbox today](https://neo4j.com/graph-data-science-software/)
    *   [opens in new tab Data Science Community A global forum for data-driven professionals](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/)

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   Learn Learn: submenu

LEARN

    *   [Documentation![Image 20](https://dist.neo4j.com/wp-content/uploads/20240401103728/Icon-Documentation.svg)Manuals for Neo4j products, Cypher, and drivers](https://neo4j.com/docs/)
    *   [GraphAcademy![Image 21](https://dist.neo4j.com/wp-content/uploads/20240402072516/Icon-GraphAcademy.svg)Free online courses and certifications](https://graphacademy.neo4j.com/)
    *   [Resource Library White papers, datasheets, and more](https://neo4j.com/resources/)
    *   [Customer Success Stories Case studies, customer videos, proof points, and more](https://neo4j.com/customer-stories/)

CONNECT

    *   [Neo4j Events Hub![Image 22](https://dist.neo4j.com/wp-content/uploads/20240402072514/Icon-Events.svg)Live and on-demand events, training, webinars, and demos](https://neo4j.com/events/)
    *   [Neo4j Blog Announcements, guides, and best practices](https://neo4j.com/blog/)
    *   [Neo4j Video Hub Covering graph databases, data science, analytics & AI](https://neo4j.com/videos/)

FEATURED EVENTS

    *   [![Image 23: GraphSummit Logo](https://dist.neo4j.com/wp-content/uploads/20250306090638/graphsummit-logo.svg) Graphs + AI: Transform Your Data Into Knowledge Learn more](https://neo4j.com/graphsummit/)
    *   [opens in new tab![Image 24: Neo4j Nodes 2026](https://dist.neo4j.com/wp-content/uploads/20260416111036/nodes-2026-logo.svg) Call for Papers Virtual Conference: Engineering Better Intelligence Submit a session abstract by June 15, 2026 Submit a Talk](https://sessionize.com/nodes26/)

*   [Pricing](https://neo4j.com/pricing/)
*   [Contact Us](https://neo4j.com/contact-us/)
*   [Get Started Free](https://console.neo4j.io/)

Blog Home 

Close

*   [Blog Home](https://neo4j.com/blog/)
*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)
*   [News](https://neo4j.com/blog/news/)

![Image 25](https://dist.neo4j.com/wp-content/uploads/20250109095231/icon-category-header-1.svg)

![Image 26](https://dist.neo4j.com/wp-content/uploads/20250109095232/icon-category-header-2.svg)

![Image 27](https://dist.neo4j.com/wp-content/uploads/20250109095234/icon-category-header-3.svg)

![Image 28](https://dist.neo4j.com/wp-content/uploads/20250109095236/icon-category-header-4.svg)

# Developer

Topic

No results found

Developer

Cypher & GQL

GenAI

Knowledge Graph

Graph Visualization

Graph Data Science

AuraDB

News

GraphQL

Machine Learning

Graph Database

Fraud Detection

Aura Graph Analytics

Security

Healthcare

NODES

Network & IT Operations

Real-Time Recommendations

Supply Chain & Logistics

Master Data Management

Agentic AI

Financial Services

Identity & Access Management

Clear Filter

![Image 29](https://dist.neo4j.com/wp-content/uploads/20260415090718/1P_nU3k5L0-_ZqI7yYhjtVw.png)

*   [Developer](https://neo4j.com/blog/developer/)

## Building a Neo4j Graph Agent for Gemini Enterprise

[22 min read](https://neo4j.com/blog/developer/building-a-neo4j-graph-agent-for-gemini-enterprise/)

![Image 30: When Your Agents Share a Brain: Building Multi-Agent Memory with Neo4j](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-1.jpg)

*   [Developer](https://neo4j.com/blog/developer/)

## How to Create and Integrate an Okta OIDC Service Account with Neo4j

[7 min read](https://neo4j.com/blog/developer/how-to-create-and-integrate-an-okta-oidc-service-account-with-neo4j/)

![Image 31](https://dist.neo4j.com/wp-content/uploads/20260414034838/networkandit-technicians-scaled.jpg)

*   [Developer](https://neo4j.com/blog/developer/)

## Neo4j GraphML Detects Network Intrusion in Snowflake

[4 min read](https://neo4j.com/blog/developer/graph-ml-detects-network-intrusion-snowflake/)

![Image 32: Building an AI Agent with Memory: Microsoft Agent Framework + Neo4j](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-3.jpg)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## Architecting Graph-Based Agentic System: When a Regulator Asks “Why Was This Loan Approved?”

[11 min read](https://neo4j.com/blog/developer/architecting-graph-based-agentic-system-when-a-regulator-asks-why-was-this-loan-approved/)

![Image 33: Using Agents to Secure Satellites’ Supply Chain Systems](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-2.jpg)

*   [Cypher & GQL](https://neo4j.com/blog/cypher-and-gql/)
*   [Developer](https://neo4j.com/blog/developer/)

## Batching Like a Pro

[8 min read](https://neo4j.com/blog/developer/batching-like-a-pro/)

![Image 34: When Your Agents Share a Brain: Building Multi-Agent Memory with Neo4j](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-1.jpg)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## When Your Agents Share a Brain: Building Multi-Agent Memory with Neo4j

[9 min read](https://neo4j.com/blog/developer/when-your-agents-share-a-brain-building-multi-agent-memory-with-neo4j/)

![Image 35](https://dist.neo4j.com/wp-content/uploads/20260415125053/sheep.png)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)

## From recall to reasoning: How context graphs upgrade an agent’s brain

[11 min read](https://neo4j.com/blog/genai/from-recall-to-reasoning-how-context-graphs-upgrade-an-agents-brain/)

![Image 36: Using Agents to Secure Satellites’ Supply Chain Systems](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-2.jpg)

*   [Developer](https://neo4j.com/blog/developer/)
*   [GenAI](https://neo4j.com/blog/genai/)
*   [Security](https://neo4j.com/blog/security/)

## Using Agents to Secure Satellites’ Supply Chain Systems

[4 min read](https://neo4j.com/blog/genai/using-agents-to-secure-satellites-supply-chain-systems/)

![Image 37: Building an AI Agent with Memory: Microsoft Agent Framework + Neo4j](https://neo4j.com/wp-content/themes/neo4jweb/assets/images/blog-card-default-3.jpg)

*   [Developer](https://neo4j.com/blog/developer/)

## Building an AI Agent with Memory: Microsoft Agent Framework + Neo4j

[17 min read](https://neo4j.com/blog/developer/building-an-ai-agent-with-memory-microsoft-agent-framework-neo4j/)

See More

![Image 38](https://dist.neo4j.com/wp-content/uploads/20230921083327/homepage-viz_ART-left.svg)![Image 39](https://dist.neo4j.com/wp-content/uploads/20230921083329/homepage-viz_ART-right.svg)![Image 40](https://dist.neo4j.com/wp-content/uploads/20230921082858/homepage-viz_left-side-art_375.svg)![Image 41](https://dist.neo4j.com/wp-content/uploads/20230921082910/homepage-viz_right-side-art_375.svg)

## Build Intelligent Apps Easily

Transform your data into knowledge to build smart, accurate, and adaptive applications.

[Start Building](https://neo4j.com/product/auradb/)

Products

*   [Neo4j AuraDB](https://neo4j.com/product/auradb/)
*   [Neo4j Graph Database](https://neo4j.com/product/neo4j-graph-database/)
*   [Neo4j Graph Analytics](https://neo4j.com/product/aura-graph-analytics/)
*   [Neo4j Graph Data Science](https://neo4j.com/product/graph-data-science/)
*   [Neo4j Fleet Manager](https://neo4j.com/product/fleet-manager/)
*   [Neo4j Bloom](https://neo4j.com/product/bloom/)
*   [Cypher Query Language](https://neo4j.com/product/cypher-graph-query-language/)
*   [Neo4j GraphQL](https://neo4j.com/product/graphql-library/)
*   [Pricing](https://neo4j.com/pricing/)
*   [Neo4j Community Edition](https://neo4j.com/product/community-edition/)

Use Cases

*   [AI Systems](https://neo4j.com/use-cases/ai-systems/)
*   [Generative AI](https://neo4j.com/generativeai/)
*   [Knowledge Graphs](https://neo4j.com/use-cases/knowledge-graph/)
*   [Pattern Matching](https://neo4j.com/use-cases/pattern-matching/)
*   [Industries & Use Cases](https://neo4j.com/use-cases/)
*   [Case Studies](https://neo4j.com/customer-stories/)

Developers

*   [Developer Home](https://neo4j.com/developer/)
*   [Documentation](https://neo4j.com/docs/)
*   [Deployment Center](https://neo4j.com/deployment-center/)
*   [Developer Blog](https://neo4j.com/blog/developer/)
*   [opens in new tab Community](https://community.neo4j.com/)
*   [Virtual Events](https://neo4j.com/events/?_event_type=virtual)
*   [opens in new tab GraphAcademy](https://graphacademy.neo4j.com/)
*   [Release Notes](https://neo4j.com/release-notes/)

Data Scientists

*   [Graph Data Science Home](https://neo4j.com/product/graph-data-science/)
*   [Data Science Documentation](https://neo4j.com/docs/graph-data-science/current/)
*   [Get Started with Graph Data Science](https://neo4j.com/graph-data-science-software/)
*   [opens in new tab Data Science Community](https://community.neo4j.com/c/neo4j-graph-platform/graph-algorithms/73)
*   [opens in new tab GraphAcademy for Data Science](https://graphacademy.neo4j.com/categories/data-scientist/)

Learn

*   [Resource Library](https://neo4j.com/resources/)
*   [Neo4j Blog](https://neo4j.com/blog/)
*   [opens in new tab GraphAcademy](https://graphacademy.neo4j.com/)
*   [Research Center](https://neo4j.com/research/)
*   [Case Studies](https://neo4j.com/customer-stories/)
*   [Neo4j Video Hub](https://neo4j.com/videos/)
*   [Neo4j Events Hub](https://neo4j.com/events/)
*   [GraphSummit](https://neo4j.com/graphsummit/)
*   [NODES](https://neo4j.com/nodes-2025/)
*   [Webinars](https://neo4j.com/webinars/)
*   [opens in new tab GraphRAG](https://graphrag.com/)

Partners

*   [Find a Partner](https://neo4j.com/partners/directory/)
*   [Become a Partner](https://neo4j.com/partners/neo4j-partner-program/)
*   [Solution Partners](https://neo4j.com/partners/solution-partners/)
*   [OEM Partners](https://neo4j.com/partners/oem-partners/)
*   [Technology Partners](https://neo4j.com/partners/technology-partners/)
*   [opens in new tab Partner Portal Login](https://neo4j.my.site.com/Neo4jPartnerCommunity)

Company

*   [About Us](https://neo4j.com/company/)
*   [Newsroom](https://neo4j.com/news/)
*   [Awards and Honors](https://neo4j.com/awards/)
*   [Graphs4Good](https://neo4j.com/graphs4good/)
*   [Careers](https://neo4j.com/careers/)
*   [Culture](https://neo4j.com/culture/)
*   [Leadership](https://neo4j.com/leadership/)
*   [opens in new tab Support](https://support.neo4j.com/s/)
*   [opens in new tab Trust Center](https://trust.neo4j.com/)

[Contact Us →](https://neo4j.com/contact-us/?ref=footer)

*   US: [1-855-636-4532](tel:1-855-636-4532)
*   Sweden: [+46 171 480 113](tel:+46 171 480 113)
*   UK: [+44 20 3868 3223](tel:+44 20 3868 3223)
*   France: [+33 (0) 1 88 46 13 20](tel:+33 (0) 1 88 46 13 20)
*   Singapore: [+65 6859 0336](tel:+65 6859 0336)
*   Australia: [+61 2 8395 2895](tel:+61 2 8395 2895)
*   India: [+91 6827 521 210](tel:+91 6827 521 210)

Social Networks

[opens in new tab](https://www.linkedin.com/company/neo4j)[opens in new tab](https://x.com/neo4j)[opens in new tab](https://youtube.com/neo4j)[opens in new tab](https://www.facebook.com/neo4j.graph.database)[opens in new tab](https://community.neo4j.com/)[opens in new tab](https://github.com/neo4j)

© 2026 Neo4j, Inc. 

[Terms](https://legal.neo4j.com/#website-terms-of-use) | [Privacy Notice](https://neo4j.com/legal-terms/privacy-notice/) | [Sitemap](https://neo4j.com/sitemap/)

[opens in new tab Anti-Corruption Policy](https://assets.neo4j.com/Neo4j_Anti-Corruption_Policy.pdf)

 ©2026 Neo4j, Inc., Neo Technology®, Neo4j®, Cypher®, Neo4j Bloom™, Neo4j Graph Data Science Library™, Neo4j® Aura™, and Neo4j® AuraDB™ are registered trademarks or a trademark of Neo4j, Inc. All other marks are owned by their respective companies. 

[![Image 42](https://dist.neo4j.com/wp-content/uploads/20210608133508/icon-tooltip-info.svg) Contact Us](https://neo4j.com/contact-us/)

[](https://neo4j.com/blog/developer/advanced-rag-strategies-neo4j/)![Image 43](blob:https://neo4j.com/37c1a353-970a-47b5-bfff-983ce1c73f3f)
