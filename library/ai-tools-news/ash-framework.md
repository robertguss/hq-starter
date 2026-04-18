---
tags:
  - library
title: "Ash Framework"
url: "https://www.ash-hq.org/"
company: [personal]
topics: []
created: 2026-03-06
source_type: raindrop
raindrop_id: 1631965641
source_domain: "ash-hq.org"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Model your domain, derive the rest.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Ash Framework

URL Source: https://www.ash-hq.org/

Markdown Content:
# Ash Framework

[![Image 1: Ash Framework](https://www.ash-hq.org/images/ash_logo_orange.svg)](https://www.ash-hq.org/ "Home")

[Documentation](https://hexdocs.pm/ash "Documentation")[Community](https://www.ash-hq.org/community "Community")[Media](https://www.ash-hq.org/media "Media")

[Premium Support](https://alembic.com.au/services/ash-framework-premium-support "Premium Support")

[![Image 2: Ash Framework](https://www.ash-hq.org/images/ash_logo_orange.svg)](https://www.ash-hq.org/ "Home")[Docs](https://hexdocs.pm/ash "Documentation")[Community](https://www.ash-hq.org/community "Community")[Media](https://www.ash-hq.org/media "Media")[Support](https://alembic.com.au/services/ash-framework-premium-support "Premium Support")

![Image 3: Ash Framework](https://www.ash-hq.org/images/ash-logo-side.svg)

# Model your domain,  derive the rest

The Elixir backend framework for unparalleled productivity. Declarative tools that let you stop wasting time. Use with Phoenix LiveView or build APIs in minutes for your front-end of choice.

[GitHub](https://github.com/ash-project/ash)

[Learn More](https://www.ash-hq.org/#ash-animation)[Install Now](https://www.ash-hq.org/#get-started)

[![Image 4: Run in Livebook](https://livebook.dev/badge/v1/pink.svg)](https://livebook.dev/run?url=https%3A%2F%2Fgithub.com%2Fash-project%2Fash_tutorial%2Fblob%2Fmaster%2Foverview.livemd)

### Resources & Actions

Resources & Actions are the core abstraction in Ash. Actions are fully typed and introspectable (your application can examine them at runtime). This means extensions can automatically understand and build on top of them.

lib/myapp/blog/post.ex

### Functional Interface

MyApp.Blog.Post.reading_time("content string") 

Takes:

content: String

Returns:

Integer (minutes)

Example:

reading_time("A long blog post...") → 3

## Discover Ash Features

### Resources & Actions

Resources & Actions are the core abstraction in Ash. Actions are fully typed and introspectable (your application can examine them at runtime). This means extensions can automatically understand and build on top of them.

```
defmodule MyApp.Blog.Post do
  use Ash.Resource
  actions do
    action :reading_time, :integer do
      argument :content, :string,
        allow_nil?: false

      run fn input, _ ->
        words =
          input.arguments.content
          |> String.split()
          |> length()

        {:ok, div(words, 200) + 1}
      end
    end
  end
end
```

→ Creates a functional interface that returns reading time in minutes 

### Persistence

Add persistent storage while keeping existing behavior. Your resource combines behavior and state.

→ Creates "posts" table with automatic migrations 

### GraphQL

Add a full GraphQL API with minimal configuration. Automatically generates queries, mutations, and types.

→ Full GraphQL API with introspectable schema 

### JSON:API

Add a REST JSON:API alongside GraphQL. Expose your domain through multiple API standards.

→ REST endpoints at /posts with JSON:API format 

### Policies

Add fine-grained authorization with policies. Control who can perform actions and filter data transparently.

→ Role-based access control with data filtering 

### Encryption

Add encryption at rest with Cloak integration. Content is automatically encrypted when stored and decrypted when read.

→ Transparent encryption - no API changes needed 

### AI Tools

Add AI-powered actions and expose your domain as tools for LLMs. Perfect for building AI features or MCP servers.

→ Prompt-backed actions with LLM integration 

### State Machine

Add declarative state validations and transitions. Each extension builds on previous ones seamlessly.

→ Declarative state validations and transitions 

### Authentication

Complete user authentication with password and OAuth strategies. Built-in support for multiple providers.

→ Password, OAuth, magic links, and more 

### Background Jobs

Add reliable background job processing with triggers and scheduled actions. Perfect for notifications and maintenance tasks.

[→ Powered by Oban for reliable job processing](https://oban.pro/)

 View on a larger screen for an interactive introduction 

[![Image 5: New Book Cover](https://www.ash-hq.org/images/book-beta.jpg) ## Get the book!](https://pragprog.com/titles/ldash/ash-framework/)

[Check out the Ash Weekly newsletter!](https://ashweekly.substack.com/)

## The Ash  Ecosystem

Powerful extensions that integrate seamlessly with your resources. Build everything from APIs to admin interfaces with declarative configuration.

[Ash Core framework](https://hexdocs.pm/ash/)[AshPostgres PostgreSQL data layer](https://hexdocs.pm/ash_postgres/)[AshPhoenix Phoenix integration](https://hexdocs.pm/ash_phoenix/)[AshGraphQL GraphQL API extension](https://hexdocs.pm/ash_graphql/)[AshJsonApi JSON:API extension](https://hexdocs.pm/ash_json_api/)[Reactor Workflows & Sagas](https://hexdocs.pm/reactor/)[AshAuthentication Authentication](https://hexdocs.pm/ash_authentication/)[AshAdmin Admin interface](https://hexdocs.pm/ash_admin/)[AshOban Background jobs](https://hexdocs.pm/ash_oban/)[AshStateMachine State machines](https://hexdocs.pm/ash_state_machine/)[AshArchival Soft deletion](https://hexdocs.pm/ash_archival/)[AshPaperTrail Audit logs](https://hexdocs.pm/ash_paper_trail/)[AshRateLimiter Rate Limiting](https://hexdocs.pm/ash_rate_limiter/)[AshCsv CSV data layer](https://hexdocs.pm/ash_csv/)[AshMoney Financial data types](https://hexdocs.pm/ash_money/)[AshDoubleEntry Double-entry accounting](https://hexdocs.pm/ash_double_entry/)[AshCloak Encryption](https://hexdocs.pm/ash_cloak/)[AshSqlite SQLite data layer](https://hexdocs.pm/ash_sqlite/)[AshCubDB CubDB data layer](https://hexdocs.pm/ash_cubdb/)[AshGeo Geospatial data](https://hexdocs.pm/ash_geo/)[AshAi LLM features](https://hexdocs.pm/ash_ai/)[UsageRules Usage guidelines](https://hexdocs.pm/usage_rules/)[AshTypescript TypeScript generation](https://hexdocs.pm/ash_typescript/)[AshAppSignal APM monitoring](https://hexdocs.pm/ash_appsignal/)[OpentelemetryAsh Telemetry tracing](https://hexdocs.pm/opentelemetry_ash/)[AshEvents Event sourcing](https://hexdocs.pm/ash_events/)

[And many more on Hex.pm!](https://hex.pm/packages?search=depends%3Ahexpm%3Aash&sort=total_downloads)

## Looking for a tutorial?

Follow our comprehensive getting started guide to build your first Ash application. Learn the fundamentals and get up and running in minutes.

[Get Started Guide](https://hexdocs.pm/ash/get-started.html)

## Get Your Installer

Project Name 

 New Project  Existing App 

- [x]  Install Elixir for me  

 Advanced Options 

 Simple Options 

## Presets

 Phoenix LiveView  Phoenix LiveView   React + TypeScript  React + TypeScript   GraphQL  GraphQL   JSON:API  JSON:API  

### Web

 Phoenix  Phoenix 

 

 GraphQL  GraphQL 

 

 JSON:API  JSON:API 

 

 TypeScript  TypeScript 

 

### Data Layers

 Postgres  Postgres 

 

 SQLite  SQLite 

 

 CSV  CSV 

 

### Authentication

 Password  Password 

 

 Magic Link  Magic Link 

 

 API Keys  API Keys 

 

 OAuth2  OAuth2 

 

### AI

 Tidewave * Tidewave *

 

 Ash AI  Ash AI 

 

 Usage Rules  Usage Rules 

 

### Finance

 Money  Money 

 

 Double Entry Accounting  Double Entry Accounting 

 

### Automation

 Oban * Oban *

 

 State Machines  State Machines 

 

 Event Sourcing  Event Sourcing 

 

### Safety & Security

 Archival  Archival 

 

 Paper Trail  Paper Trail 

 

 Encryption  Encryption 

 

### Dev Tools

 Live Debugger * Live Debugger *

 

 Admin UI  Admin UI 

 

### UI Components

 Mishka Chelekom * Mishka Chelekom *

 

 Cinder  Cinder 

 

* Is or contains an external package, not maintained by the Ash team. 

Uses [igniter](https://hexdocs.pm/igniter) to install Ash into your application

sh <(curl 'https://ash-hq.org/install/pimento_cheese?install=phoenix') \
    && cd pimento_cheese && mix igniter.install ash ash_phoenix \
    ash_postgres ash_authentication ash_authentication_phoenix ash_admin \
    live_debugger --auth-strategy magic_link --setup --yes

## Some selected features require manual setup:

## Read the docs:

Copy

## Trusted  in production

[![Image 6: Alembic](https://www.ash-hq.org/images/alembic.svg)](https://www.alembic.com.au/)[![Image 7: Daylite](https://www.ash-hq.org/images/daylite-logo.svg)](https://www.daylite.app/)[![Image 8: Heretask](https://www.ash-hq.org/images/heretask-logo-light.svg)](https://www.heretask.com/)[![Image 9: GroupFlow](https://www.ash-hq.org/images/groupflow-logo.svg)](https://www.groupflow.app/developers?utm_source=ash)[![Image 10: Zoonect](https://www.ash-hq.org/images/zoonect-dark.svg)](https://www.zoonect.com/en/homepage)[![Image 11: ScribbleVet](https://www.ash-hq.org/images/scribble-vet-logo.png)](https://www.scribblevet.com/)[![Image 12: Plangora](https://www.ash-hq.org/images/plangora-logo-dark.png)](https://www.plangora.com/)[![Image 13: Coinbits](https://www.ash-hq.org/images/coinbits-logo.png)](https://coinbits.app/)[![Image 14: Wintermeyer Consulting](https://www.ash-hq.org/images/wintermeyer-logo-dark.svg)](https://www.wintermeyer-consulting.de/)[![Image 15: Boring Business Leads](https://www.ash-hq.org/images/self-storage-leads-logo-light.svg)](https://boringbusinessleads.com/)[![Image 16: Linguavid](https://www.ash-hq.org/images/linguavid-logo.png)](https://linguavid.net/)[![Image 17: Communities](https://www.ash-hq.org/images/communities-logo.svg)](https://communities.support/)

## Upcoming  events

![Image 18: Ash Framework](https://www.ash-hq.org/images/ash_logo_orange.svg)
A declarative, resource-oriented application framework for Elixir. Model your domain, derive the rest.

### Documentation

*   [Getting Started](https://hexdocs.pm/ash/get-started.html)
*   [Guides](https://hexdocs.pm/ash/readme.html)
*   [API Reference](https://hexdocs.pm/ash/Ash.html)

### Help & Support

*   [Community](https://www.ash-hq.org/community)
*   [Report a Bug](https://github.com/ash-project/ash/issues/new?template=bug_report.md)
*   [Security Policy](https://github.com/ash-project/ash?tab=security-ov-file#readme)
*   [Premium Support](https://alembic.com.au/services/ash-framework-premium-support)

© 2026 Ash Framework. Open source and built with ❤️

[](https://github.com/ash-project/ash "GitHub")[](https://bsky.app/profile/ash-hq.org "Bluesky")
