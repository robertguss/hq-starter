---
tags:
  - library
title: "Graphile | Powerful, Extensible and Performant GraphQL APIs Rapidly"
url: "https://www.graphile.org/postgraphile/"
company: [personal]
topics: []
created: 2025-05-23
source_type: raindrop
raindrop_id: 1068725493
source_domain: "graphile.org"
source_type_raindrop: link
collection: "Web Dev"
collection_id: 69284319
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Utilities to build powerful, performant and extensible GraphQL APIs rapidly

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Introduction | PostGraphile

URL Source: https://www.graphile.org/postgraphile/

Markdown Content:
# Introduction | PostGraphile

[Skip to main content](https://www.graphile.org/postgraphile/#__docusaurus_skipToContent_fallback)

[![Image 1: PostGraphile Logo](https://www.graphile.org/img/logo.svg) **PostGraphile**](https://www.graphile.org/)[Documentation](https://www.graphile.org/postgraphile/4/)

[v4.x](https://www.graphile.org/postgraphile/4/)
*   [🚧 Preview](https://www.graphile.org/postgraphile/next/)
*   [v5.x](https://www.graphile.org/postgraphile/5/)
*   [v4.x](https://www.graphile.org/postgraphile/4/)

[News](https://www.graphile.org/news)[Sponsor](https://www.graphile.org/sponsor)[Go Pro](https://www.graphile.org/pricing)[Support](https://www.graphile.org/support)[GitHub](https://github.com/graphile/crystal)

Search

*   #### OVERVIEW

*   [Introduction](https://www.graphile.org/postgraphile/4/)
*   [Example Gallery](https://www.graphile.org/postgraphile/4/examples/) 
*   [Usage](https://www.graphile.org/postgraphile/4/usage) 
*   [Performance](https://www.graphile.org/postgraphile/4/performance)
*   [Requirements](https://www.graphile.org/postgraphile/4/requirements)
*   [Required Knowledge](https://www.graphile.org/postgraphile/4/required-knowledge)
*   #### OPERATION

*   [Quick Start Guide](https://www.graphile.org/postgraphile/4/quick-start-guide)
*   [Namespaces](https://www.graphile.org/postgraphile/4/namespaces)
*   [Inflection](https://www.graphile.org/postgraphile/4/inflection)
*   [Tables](https://www.graphile.org/postgraphile/4/tables) 
*   [Functions](https://www.graphile.org/postgraphile/4/functions) 
*   [Enums](https://www.graphile.org/postgraphile/4/enums)
*   [Views](https://www.graphile.org/postgraphile/4/views)
*   [Aggregates](https://www.graphile.org/postgraphile/4/aggregates)
*   [PostgreSQL Indexes](https://www.graphile.org/postgraphile/4/postgresql-indexes)
*   [Security](https://www.graphile.org/postgraphile/4/security)
*   [Realtime](https://www.graphile.org/postgraphile/4/realtime) 
*   [Background Tasks](https://www.graphile.org/postgraphile/4/background-tasks)
*   [Reserved Keywords](https://www.graphile.org/postgraphile/4/reserved-keywords)
*   [Debugging](https://www.graphile.org/postgraphile/4/debugging)
*   #### CUSTOMIZING

*   [Smart Tags](https://www.graphile.org/postgraphile/4/smart-tags) 
*   [Schema Plugins](https://www.graphile.org/postgraphile/4/extending) 
*   [Server Plugins](https://www.graphile.org/postgraphile/4/plugins)
*   #### GUIDES

*   [PostgreSQL Schema Design](https://www.graphile.org/postgraphile/4/postgresql-schema-design)
*   [Evaluating PostGraphile](https://www.graphile.org/postgraphile/4/evaluating)
*   [Best Practices](https://www.graphile.org/postgraphile/4/best-practices)
*   [Production Considerations](https://www.graphile.org/postgraphile/4/production)
*   [PostGraphile JWT Guide](https://www.graphile.org/postgraphile/4/jwt-guide)
*   [JWK Verification (e.g. Auth0)](https://www.graphile.org/postgraphile/4/jwk-verification)
*   [The Default Role](https://www.graphile.org/postgraphile/4/default-role)
*   [@graphile/pg-pubsub Migration Guide](https://www.graphile.org/postgraphile/4/pg-pubsub-migration)
*   [v4 Feature Guide](https://www.graphile.org/postgraphile/4/v4-new-features)
*   [v3 → v4 Migration Guide](https://www.graphile.org/postgraphile/4/v3-migration)
*   [Testing with Jest](https://www.graphile.org/postgraphile/4/testing-jest)
*   [Bundling with Webpack](https://www.graphile.org/postgraphile/4/bundling-webpack)
*   [Multiple GraphQL Schemas](https://www.graphile.org/postgraphile/4/multiple-schemas)
*   [Running PostGraphile in Docker](https://www.graphile.org/postgraphile/4/running-postgraphile-in-docker)
*   [Running PostGraphile as a Library in Docker](https://www.graphile.org/postgraphile/4/running-postgraphile-as-a-library-in-docker)
*   #### DEPLOYING

*   [Deploying to Heroku](https://www.graphile.org/postgraphile/4/deploying-heroku)
*   [Deploying with Docker](https://www.graphile.org/postgraphile/4/deploying-docker)
*   [Deploying to AWS Lambda](https://www.graphile.org/postgraphile/4/deploying-lambda)
*   [Deploying to GCP](https://www.graphile.org/postgraphile/4/deploying-gcp)
*   #### COMMUNITY

*   [Community Contributions](https://www.graphile.org/postgraphile/4/community-contributions)
*   [Community Chat](https://www.graphile.org/postgraphile/4/community-chat)
*   [Code of Conduct](https://www.graphile.org/postgraphile/4/code-of-conduct)
*   #### FAQ

*   [Introspection?](https://www.graphile.org/postgraphile/4/introspection)
*   [Why is it Nullable?](https://www.graphile.org/postgraphile/4/why-nullable)
*   [Versioning Policy?](https://www.graphile.org/postgraphile/4/versioning-policy)

*   [](https://www.graphile.org/)
*   Introduction

Version: v4.x

# PostGraphile Introduction

PostGraphile (formerly PostGraphQL) builds a powerful, extensible and performant GraphQL API from a PostgreSQL schema in seconds; saving you weeks if not months of development time.

If you already use PostgreSQL then you understand the value that a strongly typed and well defined schema can bring to application development; GraphQL is the perfect match for this technology when it comes to making your data layer accessible to your frontend application developers (or even API clients). Why duplicate your authorization and business logic in a custom API when you can leverage the tried and tested capabilities built into [the worlds most advanced open source database](https://www.postgresql.org/)?

_If you are new to GraphQL then we recommend you read through the official introduction to GraphQL [here](https://graphql.org/learn/) before continuing through the PostGraphile documentation._

By combining powerful features such as PostgreSQL's [role-based grant system](https://www.postgresql.org/docs/current/static/user-manag.html) and [row-level security policies](https://www.postgresql.org/docs/current/static/ddl-rowsecurity.html) with Graphile Engine's advanced [GraphQL look-ahead](https://build.graphile.org/graphile-build/4/look-ahead) and [plugin expansion](https://build.graphile.org/graphile-build/4/plugins) technologies, PostGraphile ensures your generated schema is secure, performant and extensible.

Some of the features we offer:

*   [Incredible performance](https://www.graphile.org/postgraphile/4/performance) - no N+1 query issues
*   Extensibility via [schema](https://www.graphile.org/postgraphile/4/extending) and [server](https://www.graphile.org/postgraphile/4/plugins) plugins
*   [Auto-discovered relations](https://www.graphile.org/postgraphile/4/relations) e.g. `userByAuthorId`
*   [Computed columns](https://www.graphile.org/postgraphile/4/computed-columns) allowing easy expansion of your API
*   [Custom query procedures](https://www.graphile.org/postgraphile/4/custom-queries) enabling arbitrary SQL queries
*   [Automatic CRUD mutations](https://www.graphile.org/postgraphile/4/crud-mutations) e.g. `updatePost`
*   [Custom mutation procedures](https://www.graphile.org/postgraphile/4/custom-mutations) enabling complex changes to be exposed simply
*   [Real-time](https://www.graphile.org/postgraphile/4/realtime) features powered by LISTEN/NOTIFY and/or logical decoding

The easiest way to get started is with the [CLI interface](https://www.graphile.org/postgraphile/4/usage-cli); if you have `npx` installed you can try it out with:

`npx postgraphile -c 'postgres://user:pass@localhost/mydb' --watch --enhance-graphiql --dynamic-json`

(replacing user, pass and mydb with your PostgreSQL username, password and the name of your database)

[Edit this page](https://github.com/graphile/crystal/tree/main/postgraphile/website/postgraphile/index.mdx)

Last updated on **Jun 25, 2025**

[Next PostGraphile Example Gallery](https://www.graphile.org/postgraphile/4/examples/)

Docs

*   [PostGraphile](https://postgraphile.org/)
*   [Gra _fast_](https://grafast.org/)
*   [Graphile Build](https://build.graphile.org/)
*   [Graphile*](https://star.graphile.org/)
*   [Ruru](https://grafast.org/ruru/)

Community

*   [Discord](https://discord.gg/graphile)
*   [Twitter](https://twitter.com/GraphileHQ)
*   [Mastodon](https://fosstodon.org/@graphile)

More

*   [GitHub](https://github.com/graphile/crystal)
*   [Sponsor](https://graphile.org/sponsor/)

![Image 2: PostGraphile Logo](https://www.graphile.org/img/logo.svg)

Copyright © 2026 Graphile Ltd. Built with Docusaurus.
