---
tags:
  - library
title: "1-Week SaaS MVP Checklist | Notion"
url: "https://ethan-trang.notion.site/1-Week-SaaS-MVP-Checklist-1bd873af2ad180a8bfc2f543787d565c"
company: [personal]
topics: []
created: 2025-06-16
source_type: raindrop
raindrop_id: 1171945174
source_domain: "ethan-trang.notion.site"
source_type_raindrop: link
collection: "Marketing & Business"
collection_id: 69284316
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

My take: No boilerplate or template can help you or is helpful if you don’t understand how things work at a high level and what is minimally viable

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: 1-Week SaaS MVP Checklist

URL Source: https://ethan-trang.notion.site/1-Week-SaaS-MVP-Checklist-1bd873af2ad180a8bfc2f543787d565c

Markdown Content:
My take:No boilerplate or template can help you or is helpful if you don’t understand how things work at a high level and what is minimally viable

NextJs 14 App Router

Typescript

Tailwind CSS

Supabase

Stripe

Vercel

Cursor

Start empty NextJs project in terminal

Create new Github repository

Push local template code to new Github repository

Create new project on Supabase add API keys to environmental variables

Deploy the app on Vercel

Landing page design

Pricing page design

Sign in page design

Application page design (home page, other feature pages)

TOS and Privacy policy page

(Optional) Blogs page design

Mobile responsiveness for all pages

Google OAuth Consent Screen for Google sign in

Supabase authentication (set up callback web hook route)

(Optional) Set up Resend and Supabase SMTP for email auth

Supabase: create tables (profiles table,…), RLS polices, and database functions

(Optional) Supabase storage bucket set up

Create API routes for each object (follow CRUD - GET, POST, DELETE, PATCH for each objects)

Link backend functionality to front end

Create pricing cards component that call a /checkout route

Create /portal route for users to access their billing portal

Feature flagging/limiting functions, profiles table design

Upgrade dialog to funnel into pricing

Stripe web hook to listen to events to edit access for users (upgrade, cancel)

Set up SEO metadata in app layout

Push code to Github repository

Host on Vercel; remember to put environmental variables

Buy domain on Namecheap

Custom domain on Supabase

(Optional but recommended) Add authorized domain to consent screen

Set up Posthog analytics

(Optional) Verify ownership on Google Search console

Keep copywriting in a libs/config.ts file

For AI projects, keep prompts in a libs/prompts.ts file

Make user limits functions in a libs/limits.ts file

Don’t let files get longer than 500 lines (effectiveness of Cursor drops significantly, use Cursor to refactor into a separate components)

Design Database

Copy table schema from existing tables to ensure consistency and context

Use Cursor to generate SQL for table creation

Set up triggers and RLS policies

Example prompt

Example SQL query to get table schema (Supabase)

Design UI

Intentionally tell Cursor to not implement functionality and use mock data instead

Reference other pages' UI to maintain design system consistency

Iterate until design is correct

Use separate chats for isolated fixes and changes

Example prompt

Design API

Include relevant table schema and endpoint references

Implement the standard 5 endpoints

Example: implementing a way to create chatbots on the platform

/chatbots/route.ts

GET - Fetch all user's chatbots

POST - Create new chatbot

/chatbots/[chatbot_id]/route.ts

GET - Fetch specific chatbot details

DELETE - Remove chatbot

PATCH - Update chatbot details

Example prompt

Integrate APIs/functionality with UI components

Example prompt

Key Takeaways:

Limit implementation scope using mock data for more modular development

Leverage Context:

Reference similar pages and components for consistent design and functionality

Use separate chats for isolated frontend or backend debugging
