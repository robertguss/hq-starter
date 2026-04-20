---
tags:
  - library
title: "Convex | The reactive database for app developers"
url: "https://www.convex.dev/"
company: [personal]
topics: []
created: 2025-05-23
source_type: raindrop
raindrop_id: 1069456113
source_domain: "convex.dev"
source_type_raindrop: link
collection: "Web Dev"
collection_id: 69284319
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: defuddle
---
## Excerpt

Convex is the reactive database for app developers. Everything you need to build your full-stack project.

## Raw Content

<!-- Hydrated 2026-04-20 via defuddle -->

[Blog](https://stack.convex.dev/) [Changelog](https://ship.convex.dev/) [Docs](https://docs.convex.dev/) [Pricing](https://www.convex.dev/pricing)

[Log in](https://www.convex.dev/login)

[Start building](https://www.convex.dev/start)

npm *create convex*

import { mutation, query } from "./\_generated/server";

import { v } from "convex/values";

export const setComplete = mutation({

args: { id: v.id("todos") },

handler: async (ctx, args) => {

await ctx.db.patch("todos", args.id, {

// Try checking a todo--nothing happens!

// Change this to \`true\` and try again.

completed: false,

});

},

});

export const list = query({ … });

export const add = mutation({ … });

export const setIncomplete = mutation({ … });

Try it out!

import { defineSchema, defineTable } from "convex/server";

import { v } from "convex/values";

export default defineSchema({

todos: defineTable({

text: v.string(),

category: v.optional(v.string()),

completed: v.boolean(),

}).index("by\_completed", \["completed"\]),

});

<iframe src="https://www.convex.dev/iframe/index.html"></iframe>

import { api } from "../../convex/\_generated/api";

import { TodoList } from "./TodoList";

import { useQuery } from "convex/react";

export function TodoApp() {

// Load more by changing \`count\` to 10.

// Everything updates reactively.

const todos = useQuery(api.todos.list, { count: 5 });

return <TodoList todos={todos} />;

}

Try it out!

import { mutation, query } from "./\_generated/server";

import { v } from "convex/values";

export const setComplete = mutation({ … });

export const list = query({

args: { count: v.number() },

handler: async (ctx, args) => {

return await ctx.db.query("todos").order("desc").take(args.count);

},

});

export const add = mutation({ … });

export const setIncomplete = mutation({ … });

<iframe src="https://www.convex.dev/iframe/index.html"></iframe>

import { cronJobs } from "convex/server";

import { internal } from "./\_generated/api";

const crons = cronJobs();

crons.interval(

"categorize todos",

{ seconds: 5 },

internal.categorize.categorize,

{

// Add categories "Sports" and "Health"

// to see the todos categorized on the

// next cron job run.

categories: \["Chores", "Work"\],

},

);

export default crons;

Try it out!

import { v } from "convex/values";

import { api, internal } from "./\_generated/api";

import { Doc, Id } from "./\_generated/dataModel";

import { internalAction, internalMutation } from "./\_generated/server";

import Anthropic from "@anthropic-ai/sdk";

type AiCategorizeResponse = {

id: Id<"todos">;

category: string;

};

export const categorize = internalAction({

args: { categories: v.array(v.string()) },

handler: async (ctx, args) => {

const todos = await ctx.runQuery(api.todos.list, { count: 100 });

const response = await categorizeTodos(todos, args.categories);

await ctx.runMutation(internal.categorize.setCategories, {

categories: response,

});

},

});

export const setCategories = internalMutation({

args: {

categories: v.array(v.object({ id: v.id("todos"), category: v.string() })),

},

handler: async (ctx, args) => {

for (const category of args.categories) {

await ctx.db.patch("todos", category.id, {

category: category.category,

});

}

},

});

async function categorizeTodos(

todos: Doc<"todos">\[\],

categories: string\[\],

): Promise<AiCategorizeResponse\[\]> { … }

import { defineSchema, defineTable } from "convex/server";

import { v } from "convex/values";

export default defineSchema({

todos: defineTable({

text: v.string(),

category: v.optional(v.string()),

completed: v.boolean(),

}).index("by\_completed", \["completed"\]),

});

<iframe src="https://www.convex.dev/iframe/index.html"></iframe>

AI Tools

## LLMs love Convex

With Convex, everything is just TypeScript. This means your favorite AI tools are pre-equipped to generate high quality code.

[Learn more](https://www.convex.dev/ai)[Try Convex with](https://chef.convex.dev/)

[![Convex Chef](https://www.convex.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fchef-isolated.0-dg8~xmli_f-.svg&w=256&q=75)](https://chef.convex.dev/)

Product

## Not just a database

Everything your product deserves to build, launch, and scale.

[Learn more](https://docs.convex.dev/) ![Illustration of the features provided by Convex, including realtime updates, type safety, and automatic caching.](https://www.convex.dev/_next/image?url=%2Fhome%2Fdiagram-content-wide.png&w=1536&q=75)

Customer Love

## Loved by developers

What people building their business on Convex are saying.

Get your app up and running in minutes

[Start building](https://www.convex.dev/start) ![](https://www.convex.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fpixel-burst.15brrhd.99cxo.svg&w=256&q=75)
