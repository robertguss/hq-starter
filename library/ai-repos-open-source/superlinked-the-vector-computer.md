---
tags:
  - library
title: "Superlinked - The Vector Computer"
url: "https://superlinked.com/"
company: [personal]
topics: []
created: 2025-08-17
source_type: raindrop
raindrop_id: 1302567392
source_domain: "superlinked.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

The data engineer’s solution to turning data into vector embeddings.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Superlinked | Self-hosted inference for search & document processing

URL Source: https://superlinked.com/

Published Time: Fri, 17 Apr 2026 16:53:37 GMT

Markdown Content:
# Superlinked | Self-hosted inference for search & document processing
[Why did we open-source our inference engine? Read the post](https://superlinked.com/blog/launch)

[![Image 1: Superlinked](https://superlinked.com/diagrams/superlinked-logo.svg)](https://superlinked.com/)

[Models](https://superlinked.com/models)[Examples](https://superlinked.com/docs/examples)[Docs](https://superlinked.com/docs/)[Blog](https://superlinked.com/blog)

[Github 1.5K](https://github.com/superlinked/sie)

Contact us

[Models](https://superlinked.com/models)[Examples](https://superlinked.com/docs/examples)[Docs](https://superlinked.com/docs/)[Blog](https://superlinked.com/blog)

[Github 1.5K](https://github.com/superlinked/sie)

Contact us

![Image 2](https://superlinked.com/cdn/65dce6831bf9f730421e2915/65dce6831bf9f730421e292a_bg_brid.svg)

# Self-hosted inference

for search & document processing

![Image 3](https://superlinked.com/cdn/65dce6831bf9f730421e2915/arrow-right.svg) 50x cheaper vs managed model APIs 

![Image 4](https://superlinked.com/cdn/65dce6831bf9f730421e2915/arrow-right.svg) Quality boost from 85+ SOTA models 

![Image 5](https://superlinked.com/cdn/65dce6831bf9f730421e2915/arrow-right.svg) Data doesn't leave your AWS/GCP 

[Github 1.5K](https://github.com/superlinked/sie)

Contact us

 AWS  GCP  LOCAL 

# Configure
module "sie" {
  source = "superlinked/sie/aws"
  region = "us-east-1"
  gpus   = ["a100-40gb", "l4-spot"]
}
# Deploy
> terraform apply
> helm install sie oci://ghcr.io/superlinked/charts/sie-cluster
# Use
> pip install sie-sdk
client.encode("BAAI/bge-m3", Item(text="indemnification"),
    options={"lora": "legal"})# Configure
module "sie" {
  source = "superlinked/sie/google"
  region = "us-central1"
  gpus   = ["a100-40gb", "l4-spot"]
}
# Deploy
> terraform apply
> helm install sie oci://ghcr.io/superlinked/charts/sie-cluster
# Use
> pip install sie-sdk
client.encode("BAAI/bge-m3", Item(text="indemnification"),
    options={"lora": "legal"})# Run
> docker run -p 8080:8080 ghcr.io/superlinked/sie-server
# Use
> pip install sie-sdk
client.encode("BAAI/bge-m3", Item(text="indemnification"),
    options={"lora": "legal"})

## Works with your favorite tools

[Browse integrations](https://superlinked.com/docs/integrations)

[![Image 6](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/chroma-icon.svg)![Image 7](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/chroma.svg) docs "Chroma makes context engineering simple. SIE adds instruction-following rerankers and relationship extractors for even more precise retrieval." ![Image 8](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/jeff-huber.jpg) Jeff Huber CEO & Founder](https://superlinked.com/docs/integrations/chroma)[![Image 9](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/lancedb-icon.svg)![Image 10](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/lancedb.svg) docs "LanceDB centralizes multi-modal training datasets and with SIE you can self-host inference for all the required data transformations." ![Image 11](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/chang-she.jpg) Chang She CEO & Co-founder](https://superlinked.com/docs/integrations/lancedb)[![Image 12](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/qdrant-icon.svg)![Image 13](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/qdrant.svg) docs "Modern search systems compose the best indexing, scoring, filtering and ranking models. With SIE you can self-host them all in one cluster." ![Image 14](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/andre-zayarni.jpg) Andre Zayarni CEO & Co-founder](https://superlinked.com/docs/integrations/qdrant)[![Image 15](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/weaviate-icon.svg)![Image 16](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/weaviate.svg) docs "Weaviate's Query Agent unlocks natural language search and with SIE you can pre-process your query and data for better latency." ![Image 17](https://superlinked.com/cdn/65dce6831bf9f730421e2915/partners/bob-van-luijt.jpg) Bob Van Luijt CEO & Co-founder](https://superlinked.com/docs/integrations/weaviate)

## Benefits of self-hosted inference

[50x Compare price cost saving Pay for your own GPUs instead of per-token API pricing. Improve GPU utilization and stability vs. custom TEI/Infinity deployments.](https://superlinked.com/#plan-deployment)[85+ Browse models latest models Boost accuracy with latest task-specific open source models. Embeddings, rerankers, extraction, including multi-modal and multi-vector.](https://superlinked.com/models)[100% Deployment docs under your control Data never leaves your AWS/GCP. You pick models and configurations. SOC2 Type2 certified. Apache 2.0 licensed.](https://superlinked.com/docs/deployment)

## Learn from our example apps

[Browse examples](https://superlinked.com/docs/examples)

[![Image 18: SIE vs TEI vs OpenAI benchmark](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b83eb71ab5ba77bc764a36_1.avif) SIE vs TEI vs OpenAI benchmark Cost analysis, latency, and throughput - head-to-head comparison of SIE vs TEI vs OpenAI Explore Example](https://superlinked.com/docs/examples/benchmark)[![Image 19: OpenClaw semantic search](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b83eb7fb01d0cbf5c84305_2.avif) OpenClaw semantic search SIE-powered semantic memory for the OpenClaw AI agent Explore Example](https://superlinked.com/docs/examples/openclaw-semantic-search)[![Image 20: Wine Recommender](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b83eb77ed26bce23b88a35_3.avif) Wine Recommender Multimodal search over tasting notes and wine label photos using Florence2 and SigLIP Explore Example](https://superlinked.com/docs/examples/wine-recommender)[![Image 21: Regulatory Intelligence RAG](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b83ec1df66480f6697ce20_4.avif) Regulatory Intelligence RAG Custom pruner adapter and LoRA hot-loading showcase with a 3-stage pipeline on shared GPU Explore Example](https://superlinked.com/docs/examples/regulatory-intelligence-rag)[![Image 22: E-Commerce Product Search](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b83eb7b61b161e860c02fb_5.avif) E-Commerce Product Search End-to-end product search using all 3 SIE primitives - extract, encode, and score Explore Example](https://superlinked.com/docs/examples/ecommerce-product-search)[![Image 23: Semantic HF Model Search](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b83eb6e20f83be79281c76_6.avif) Semantic HF Model Search Semantic search over ~14K HF embedding model cards with task-specific MTEB scores Explore Example](https://superlinked.com/docs/examples/semantic-hf-model-search)

## SIE: Superlinked Inference Engine

Run all your Search & Document processing inference in one centralized cluster across teams and workloads.

SIE SDKs 

Build your apps

> pip install sie-sdk
> npm install @superlinked/sie-sdk
and 5+ framework integrations

Manage models & configurations via SDK

client.list_models()

SIE Cluster 

Deploy the cluster

> helm install sie
    oci://ghcr.io/superlinked/
        charts/sie-cluster
Observe with cloud-native tools, grafana and

> sie-top

SIE Infra AWS GCP

Create the infrastructure

module "sie" {
  source = "superlinked/sie/aws"
  region = "us-east-1"
  gpus   = ["a100-40gb", "l4-spot"]
}module "sie" {
  source = "superlinked/sie/google"
  region = "us-central1"
  gpus   = ["a100-40gb", "l4-spot"]
}
Deploy

> terraform apply

![Image 24: SIE Architecture](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69bdb11ea0997528e6aa8802_diagramSIE.svg)

## Plan your self-deployment

![Image 25: SIE deployment architecture](https://superlinked.com/cdn/65dce6831bf9f730421e2915/sie-stack-diagram.svg)
### How SIE fits in your stack

See where SIE sits in a typical retrieval pipeline alongside vector databases, orchestration frameworks, and your application layer.

### Cost Comparison

Compare across models, GPU types, and cloud providers.

Encode Score Extract

Provider Cost per 1B tokens Notes

OpenAI API$20 emb-3-small · $0.02/1M tok

Modal + TEI$1.30 bge-base on A10G · $1.10/hr

Your Cloud + SIE$0.50 bge-base on spot A10G · $0.38/hr

Provider Cost per 1B tokens Notes

Cohere Rerank$87 Rerank 3.5 · $2/1K queries

Vertex AI Ranking$43 Ranking API · $1/1K queries

Your Cloud + SIE$8.50 modernbert-base · spot A10G · $0.38/hr

Provider Cost per 1B tokens Notes

OpenAI API$140 GPT-4.1 Nano · $0.10/1M input

Google Cloud NL$5,000 Entity Analysis · $1/1M chars

AWS Comprehend$5,000 Entity Recog. · $1/1M chars

Your Cloud + SIE$5 GLiNER · spot A10G · $0.38/hr

[deployment documentation](https://superlinked.com/docs/deployment)

## SIE Blog

[Read all articles](https://superlinked.com/blog)

[Read article Daniel Svonava • Launch 02/04/26 Boost performance & reduce cost by self-hosting specialized AI models](https://superlinked.com/blog/launch)[Read article Superlinked • Tech 03/15/25 A Practical Guide for Choosing a Vector Database](https://superlinked.com/blog/choosing-a-vector-database)[Read article Ashish Abraham • Tech 02/10/25 Optimizing RAG with Hybrid Search & Reranking](https://superlinked.com/blog/optimizing-rag-with-hybrid-search-reranking)[Read article Rod Rivera • Tech 01/20/25 Vector Embeddings in the Browser](https://superlinked.com/blog/vector-embeddings-in-the-browser)

## Self-hosted inference for search& document processing

Cut API costs by 50x, boost quality with 85+ SOTA models, and keep your data in your own cloud.

[Github 1.5K](https://github.com/superlinked/sie)Contact us

[![Image 26: Superlinked](https://superlinked.com/diagrams/superlinked-logo-white.svg)Superlinked Inference Engine](https://superlinked.com/)![Image 27: SOC2](https://superlinked.com/cdn/65dce6831bf9f730421e2915/69b2b2368eb4ae90247d86dc_SOC2.svg)

© 2026 Superlinked. All rights reserved.

PRODUCT

[Docs](https://superlinked.com/docs/)[Models](https://superlinked.com/models)[Examples](https://superlinked.com/docs/examples)[VDB Comparison](https://superlinked.com/vector-db-comparison)

ABOUT

[About us](https://superlinked.com/about)[Careers](https://jobs.superlinked.com/)[Glossary](https://superlinked.com/glossary)

LINKS

[GitHub](https://github.com/superlinked/sie)

[Twitter](https://twitter.com/superlinked)

[LinkedIn](https://www.linkedin.com/company/superlinked/)

Subscribe for OSS updates,

tutorials and examples

Subscribe

 You are agreeing to our [Terms and Conditions](https://superlinked.com/policies/terms-and-conditions) by Subscribing. 

[Terms of Use](https://superlinked.com/policies/terms-and-conditions)[Privacy Policy](https://superlinked.com/policies/privacy-policy)[Cookies Settings](https://superlinked.com/policies/cookie-policy)

[Go back top ↑](https://superlinked.com/#)

×
## Contact us

Tell us about your use case and we'll get back to you shortly.

Name * 

Email * 

Company 

Message * 

Send message

✓

### Message sent

Thanks for reaching out! We'll get back to you soon.

Close

 We use cookies for analytics. [Learn more](https://superlinked.com/policies/cookie-policy)

Accept Decline
