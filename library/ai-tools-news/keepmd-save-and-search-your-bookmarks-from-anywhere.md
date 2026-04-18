---
tags:
  - library
title: "keep.md | save and search your bookmarks from anywhere"
url: "https://keep.md/"
company: [personal]
topics: []
created: 2026-03-09
source_type: raindrop
raindrop_id: 1636498832
source_domain: "keep.md"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Keep your bookmarks as markdown and search them from the web, the api, or with your personal AI agent.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Keep | Save and search your bookmarks from anywhere

URL Source: https://keep.md/

Markdown Content:
> This tutorial involves a lot of code and is therefore also available as markdown here. See more of my writing here.

In this post, I'll start from scratch and build up to OpenClaw's architecture step by step, showing how you could have invented it yourself from first principles, using nothing but a messaging API, an LLM, and the desire to make AI actually useful _*outside*_ the chat window.

End goal: understand how persistent AI assistants work, so you can build your own (or become an OpenClaw power user).

### First, let's establish the problem

When you use ChatGPT or Claude in a browser, there are several limitations:

**It's stateless.** Every conversation starts from zero. It doesn't know your name, your preferences, what you asked yesterday, or what project you're working on. You're constantly re-explaining context.

**It's passive.** You go to it. It never comes to you. It can't wake up at 7am and brief you on your calendar, monitor your email, or run a recurring task. It only works when you're sitting in front of it.

**It's isolated.** It can't run commands on your machine, browse the web for you, control your apps, or send messages on your behalf. It lives in a text box with no hands.

**It's single-channel.** Your real life happens across WhatsApp, Telegram, Discord, Slack, iMessage - but the AI lives in its own separate tab. There's no way to text it where you already are, let alone have it maintain one continuous memory across all those surfaces.

What if instead, you had an AI that:

*   Lived in the messaging apps you already use - all of them, with shared memory

*   Remembered your preferences, your projects, and your past conversations across sessions

*   Could run commands on your computer, browse the web, and control a real browser

*   Woke up on a schedule to handle recurring tasks without being asked

*   Ran on your own hardware - your laptop, a VPS, a Mac Mini - always on, under your control

This is what OpenClaw does. It's not a chatbot - it's a personal AI assistant with a persistent identity, tools, and presence across every channel you use.

Let's build one from scratch.

## The Simplest Possible Bot

Let's start with the absolute minimum: an AI that responds to messages on Telegram.

```
import os
import anthropic
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

client = anthropic.Anthropic()

async def handle_message(update: Update, context):
    user_message = update.message.text

response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_message}]
    )

await update.message.reply_text(response.content[0].text)

app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
```

Run it, send a message on Telegram, and the AI responds. Simple.

But this is basically a worse version of the Claude web interface. Every message is independent. No memory. No tools. No personality.

What if we gave it memory?

## Goal: Persistent Sessions

A problem with our simple bot is statelessness. Every message is a fresh conversation. Ask it "what did I say earlier?" and it has no idea.

The fix is sessions. Keep a conversation history per user.

```
import json
import os
import anthropic
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

client = anthropic.Anthropic()
SESSIONS_DIR = "./sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

def get_session_path(user_id):
    return os.path.join(SESSIONS_DIR, f"{user_id}.jsonl")

def load_session(user_id):
    """Load conversation history from disk."""
    path = get_session_path(user_id)
    messages = []
    if os.path.exists(path):
        with open(path, "r") as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
    return messages

def append_to_session(user_id, message):
    """Append a single message to the session file."""
    path = get_session_path(user_id)
    with open(path, "a") as f:
        f.write(json.dumps(message) + "\n")

def save_session(user_id, messages):
    """Overwrite the session file with the full message list."""
    path = get_session_path(user_id)
    with open(path, "w") as f:
        for message in messages:
            f.write(json.dumps(message) + "\n")

async def handle_message(update: Update, context):
    user_id = str(update.effective_user.id)
    user_message = update.message.text

# Load existing conversation
    messages = load_session(user_id)

# Add new user message
    user_msg = {"role": "user", "content": user_message}
    messages.append(user_msg)
    append_to_session(user_id, user_msg)

# Call the AI with full history
    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        messages=messages
    )

# Save assistant response
    assistant_msg = {"role": "assistant", "content": response.content[0].text}
    append_to_session(user_id, assistant_msg)

await update.message.reply_text(response.content[0].text)

app = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))
app.run_polling()
```

Now you can have an actual conversation:

```
You: My name is Nader
Bot: Nice to meet you, Nader!

[hours later...]

You: What's my name?
Bot: Your name is Nader!
```

The key insight is the JSONL format. Each line is one message. Append-only. If the process crashes mid-write, you lose at most one line. This is exactly what OpenClaw uses for session transcripts:

```
~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
```

Each session maps to a file. Each file is a conversation. Restart the process and everything is still there.
