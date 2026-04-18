---
tags:
  - library
title: "Cloudflare Workers"
url: "https://workers.cloudflare.com/#data-platform"
company: [personal]
topics: []
created: 2026-03-07
source_type: raindrop
raindrop_id: 1633481220
source_domain: "workers.cloudflare.com"
source_type_raindrop: link
collection: "Web Dev"
collection_id: 69284319
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Welcome to the Cloudflare Dev Platform - Powering the next generation of applications

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Cloudflare

URL Source: https://workers.cloudflare.com/

Markdown Content:
# Cloudflare

 Cloudflare 

Products Solutions Resources[Pricing](https://workers.cloudflare.com/plans)

[Under Attack?](https://workers.cloudflare.com/resources/under-attack)[Login](https://dash.cloudflare.com/sign-up/login)[Start building](https://dash.cloudflare.com/sign-up/workers-and-pages)[Start building](https://dash.cloudflare.com/sign-up/workers-and-pages)

 Hero animation off in Low preview — use High mode and refresh for full motion. 

Agents Week is happening now April 13 - April 17! Check out the announcements[here](https://blog.cloudflare.com/)

# Everything we learned from powering 20% of the Internet—yours by default

Cloudflare is your AI Cloud with compute, AI inference, and storage — letting you ship applications instead of managing and securing infrastructure.

[Start building](https://dash.cloudflare.com/sign-up/workers-and-pages)

### The cloud that works for you, not the other way around

Deploy serverless functions, frontends, containers, and databases to 330+ cities with one command.

AI Agents WebRTC Platforms Multiplayer Data Platform

[React Flow](https://reactflow.dev/)

Press enter or space to select a node. You can then use the arrow keys to move the node around. Press delete to remove it and escape to cancel.

Press enter or space to select an edge. You can then press delete to remove it or escape to cancel.

Build AI agents on durable objects with code execution, inference, AI gateway all built-in

"Cloudflare provided everything from OAuth to out-of-the-box remote MCP support so we could quickly build, secure, and scale a fully operational setup."

Architecture inspired by

Atlassian

Create your own app

Inspired by
Discord

### Region: Earth

Our smart network positions your workloads optimally — close to users, close to data.

###### Run everywhere

Run code in **330+ cities** around the world, within 50ms of 95% of the world's population.

###### Run anywhere

Run code near the user, database, or near your APIs. Our smart network will schedule your requests to optimize for the best latency.

###### Run at massive scale

Run on Cloudflare's infrastructure, supporting **449 Tbps** of network capacity, serving over **81 million HTTP requests** per second.

### Cloudflare powers

1 in 5 sites on the Internet

Trusted by the teams you trust. And thousands more...

![Image 1](https://workers.cloudflare.com/companies/anthropic.png)![Image 2](https://workers.cloudflare.com/companies/canva.png)![Image 3](https://workers.cloudflare.com/companies/asana.png)![Image 4](https://workers.cloudflare.com/companies/atlassian.png)![Image 5](https://workers.cloudflare.com/companies/shopify.png)![Image 6](https://workers.cloudflare.com/companies/stripe.png)![Image 7](https://workers.cloudflare.com/companies/wix.png)![Image 8](https://workers.cloudflare.com/companies/block.png)![Image 9](https://workers.cloudflare.com/companies/intercom.png)![Image 10](https://workers.cloudflare.com/companies/doordash.png)![Image 11](https://workers.cloudflare.com/companies/coreweave.png)![Image 12](https://workers.cloudflare.com/companies/leonardo.png)

anthropic

canva

asana

atlassian

shopify

stripe

wix

block

intercom

doordash

coreweave

leonardo

anthropic

canva

asana

atlassian

### Go from

### in minutes

No DevOps. Minimal cold starts. No surprise bills.

###### From first line to full scale

Deploy working code in seconds or start from hundreds of templates — all built to scale.

[See templates](https://developers.cloudflare.com/workers/get-started/quickstarts/)

Player 1

Player 2

multiplayer-cursors.tsx text-to-image.tsx hello-world.tsx

import { routePartykitRequest, Server } from "partyserver";
  
import type { OutgoingMessage, Position } from "../shared";
import type { Connection, ConnectionContext } from "partyserver";

// This is the state that we'll store on each connection
type ConnectionState = {
  position: Position;
};

export class Globe extends Server {
  onConnect(conn: Connection<ConnectionState>, ctx: ConnectionContext) {
    // Whenever a fresh connection is made, we'll
    // send the entire state to the new connection
    
    // First, let's set up the connection state
    conn.setState({ position: { x: 0, y: 0 } });
    
    // Send current state to new connection
    this.broadcast(JSON.stringify({
      type: "user-joined",
      id: conn.id,
      position: conn.state.position
    }));
  }

  onMessage(message: string, sender: Connection<ConnectionState>) {
    const data = JSON.parse(message) as OutgoingMessage;
    
    if (data.type === "position-update") {
      sender.setState({ position: data.position });
      
      // Broadcast position update to all other connections
      this.broadcast(JSON.stringify({
        type: "position-update",
        id: sender.id,
        position: data.position
      }), [sender.id]);
    }
  }

  onClose(connection: Connection<ConnectionState>) {
    this.broadcast(JSON.stringify({
      type: "user-left",
      id: connection.id
    }));
  }
}

~/workspace/multiplayer-app git:(main)

###### Deploy with one command

###### Let it spike. We got you.

Your application runs globally, handles millions of requests, and scales without you thinking about it.

### Pay only when your code runs

(Not to keep servers warm.)

###### Wall Clock vs. CPU Time

Never pay for idle time waiting for slow APIs, LLMs, or humans. Cloudflare charges only for compute, not wall time, even during long agent workflows or hibernating WebSockets.

1ms

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

LLM Call 2500ms

0.5ms

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

free

API Call 300ms

0.75ms

`Paid`

`Free`

### Free

No credit card needed

[See more](https://workers.cloudflare.com/plans)

Workers Durable Objects R2 Workers KV

###### 100,000

/  daily requests

###### 1 million

/  KV daily reads

###### 25

/  AI daily requests

###### 10GB

/  R2 Storage

### Paid

Starts at $5/month

[See more](https://workers.cloudflare.com/plans)

Workers Durable Objects R2 Workers KV

###### $0.30

/  million requests

###### $0.02

/  million CPU ms

### Why choose Cloudflare

Everything needed to build performant applications.

### Fighting infra with “cloud”

### Shipping with

Cloudflare

### Tailored to your working style

Always simple, fast, and reliable.

###### Fits into your existing workflows

Git, GitHub Actions, VS Code, and any framework. No proprietary tools or vendor lock-in.

###### Instant feedback loops

Our smart network positions your workloads optimally — close to users, close to data.

###### Observable by default

Built-in logs, metrics, and tracing. Understand your application's performance without setting up monitoring infrastructure.

###### Compatible with your stack

Use the languages and frameworks you know — JS, TS, Python, Rust, React, and more. Cloudflare works with your existing databases, APIs, and services.

/ide.tsx/avatar.svelte/func.py/api.js

import { Code } from "@/components/interactive/code-editor"
import { Icon } from "@/components/ui"
import { minDarkTheme } from "@/themes/min-dark"

export const IDE = () => {
  const [activeTab, setActiveTab] = useState(0)
  const [isHovering, setIsHovering] = useState(false)

  const tabs = [
    { icon: "typescript", name: "multiplayer.ts", language: "typescript" },
    { icon: "svelte", name: "profile.svelte", language: "svelte" },
    { icon: "python", name: "function.py", language: "python" }
  ]

  return (
    <div className="bg-background-100 mt-8 flex h-full w-full flex-col rounded-md border">
      <div className="flex">
        {tabs.map((tab, index) => (
          <button
            key={tab.name}
            className="flex items-center gap-1.5 px-3 py-2 transition-colors"
            onMouseEnter={() => {
              setIsHovering(true)
              setActiveTab(index)
            }}
          >
            <Icon icon={tab.icon} className="size-4" />
            {tab.name}
          </button>
        ))}
      </div>
      <div className="h-full w-full overflow-hidden">
        <SyntaxHighlighter
          language={activeTabData.language}
          style={minDarkTheme}
          showLineNumbers
        >
          {activeTabData.content}
        </SyntaxHighlighter>
      </div>
    </div>
  )
}

 Build section motion off in Low preview — use High mode and refresh for full motion. 

# Build without boundaries

Join thousands of developers who've eliminated infrastructure complexity and deployed globally with Cloudflare. Start building for free — no credit card required.

[Start building for free](https://dash.cloudflare.com/sign-up/workers-and-pages)[View docs](https://developers.cloudflare.com/)

 Cloudflare 

 Getting Started 

[Free Plans](https://www.cloudflare.com/plans/free/)[For Enterprises](https://www.cloudflare.com/enterprise/)[Compare Plans](https://workers.cloudflare.com/plans)[Domain Name Search](https://domains.cloudflare.com/)[Get a Recommendation](https://www.cloudflare.com/about-your-website/)[Request a Demo](https://www.cloudflare.com/plans/enterprise/demo/)[Contact Sales](https://www.cloudflare.com/plans/enterprise/contact/)

 Resources 

[Products](https://workers.cloudflare.com/products)[Startups](https://workers.cloudflare.com/startups)[Under Attack?](https://workers.cloudflare.com/resources/under-attack)[Documentation](https://developers.cloudflare.com/)[Learning Center](https://workers.cloudflare.com/learning)[Analyst Reports](https://www.cloudflare.com/threat-reports/)[App Innovation Report](https://workers.cloudflare.com/resources/app-innovation-report)[Cloudflare Radar](https://radar.cloudflare.com/)[Reference Architectures](https://www.cloudflare.com/architecture/)[Case Studies](https://workers.cloudflare.com/case-studies)[Blog](https://blog.cloudflare.com/)[Community](https://community.cloudflare.com/)[Press](https://workers.cloudflare.com/press)

 Solutions 

[Connectivity Cloud](https://www.cloudflare.com/connectivity-cloud/)[SSE and SASE Platform](https://workers.cloudflare.com/sase)[Application Services](https://www.cloudflare.com/application-services/)[Network Services](https://www.cloudflare.com/network-services/)[Global Network](https://workers.cloudflare.com/network)

© 2026 Cloudflare, Inc.

English Your Privacy Choices

[Privacy Policy](https://workers.cloudflare.com/policies/privacy), [Terms of Service](https://workers.cloudflare.com/policies/terms), [GDPR](https://www.cloudflare.com/trust-hub/gdpr/)
