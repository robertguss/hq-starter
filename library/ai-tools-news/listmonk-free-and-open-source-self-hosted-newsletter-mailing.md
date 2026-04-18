---
tags:
  - library
title: "listmonk - Free and open source self-hosted newsletter, mailing list manager, and transactional mails"
url: "https://listmonk.app/"
company: [personal]
topics: []
created: 2026-01-19
source_type: raindrop
raindrop_id: 1552913853
source_domain: "listmonk.app"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Send e-mail campaigns and transactional e-mails. High performance and features packed into one app.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: listmonk - Free and open source self-hosted newsletter, mailing list manager, and transactional mails

URL Source: https://listmonk.app/

Published Time: Thu, 16 Apr 2026 18:29:32 GMT

Markdown Content:
# listmonk - Free and open source self-hosted newsletter, mailing list manager, and transactional mails

[![Image 1: Listmonk logo](https://listmonk.app/static/images/logo.svg)](https://listmonk.app/)

[Download](https://listmonk.app/#download)[Docs](https://listmonk.app/docs)

[GitHub](https://github.com/knadh/listmonk)

![Image 2](https://listmonk.app/static/images/s4.webp)

# Self-hosted newsletter and mailing list manager

### Performance and features packed into a single binary.

**Free and open source.**

[Live demo](https://demo.listmonk.app/)

![Image 3](https://listmonk.app/static/images/s1.webp)![Image 4](https://listmonk.app/static/images/s2.webp)![Image 5](https://listmonk.app/static/images/s3.webp)![Image 6: listmonk screenshot](https://listmonk.app/static/images/splash.webp)

## Download

The latest version is **v6.1.0** released on 29 Mar 2026. See [release notes.](https://github.com/knadh/listmonk/releases/tag/v6.1.0)

### Binary

Download binary (64 bit)

[![Image 7: Darwin](https://listmonk.app/static/images/logo-darwin.svg)Darwin](https://github.com/knadh/listmonk/releases/download/v6.1.0/listmonk_6.1.0_darwin_amd64.tar.gz)[![Image 8: Freebsd](https://listmonk.app/static/images/logo-freebsd.svg)Freebsd](https://github.com/knadh/listmonk/releases/download/v6.1.0/listmonk_6.1.0_freebsd_amd64.tar.gz)[![Image 9: Linux](https://listmonk.app/static/images/logo-linux.svg)Linux](https://github.com/knadh/listmonk/releases/download/v6.1.0/listmonk_6.1.0_linux_amd64.tar.gz)[![Image 10: Netbsd](https://listmonk.app/static/images/logo-netbsd.svg)Netbsd](https://github.com/knadh/listmonk/releases/download/v6.1.0/listmonk_6.1.0_netbsd_amd64.tar.gz)[![Image 11: Openbsd](https://listmonk.app/static/images/logo-openbsd.webp)Openbsd](https://github.com/knadh/listmonk/releases/download/v6.1.0/listmonk_6.1.0_openbsd_amd64.tar.gz)[![Image 12: Windows](https://listmonk.app/static/images/logo-windows.svg)Windows](https://github.com/knadh/listmonk/releases/download/v6.1.0/listmonk_6.1.0_windows_amd64.tar.gz)

Install

*   `./listmonk --new-config` to generate config.toml. Edit it.
*   `./listmonk --install` to setup the Postgres DB or `--upgrade` to upgrade an existing DB.
*   Run `./listmonk` and visit `http://localhost:9000`

[Installation docs →](https://listmonk.app/docs/installation)

### Docker

[`listmonk/listmonk:latest`](https://hub.docker.com/r/listmonk/listmonk/tags?page=1&ordering=last_updated&name=latest)

Download and use the sample [docker-compose.yml](https://github.com/knadh/listmonk/blob/master/docker-compose.yml)

# Download the compose file to the current directory.
curl -LO https://github.com/knadh/listmonk/raw/master/docker-compose.yml

# Run the services in the background.
docker compose up -d

Visit `http://localhost:9000`

[Installation docs →](https://listmonk.app/docs/installation)

## Hosting providers

[![Image 13: Deploy to Nodion](https://listmonk.app/static/images/host-nodion.svg)](https://www.nodion.com/en/deploy/listmonk/)[![Image 14: One-click deploy on Kloudbean](https://listmonk.app/static/images/host-kloudbean.svg)](https://www.kloudbean.com/listmonk-self-hosted)[![Image 15: One-click deploy on Northflank](https://listmonk.app/static/images/host-northflank.webp)](https://northflank.com/stacks/deploy-listmonk)[![Image 16: One-click deploy on Railway](https://listmonk.app/static/images/host-railway.svg)](https://railway.app/new/template/listmonk)[![Image 17: Deploy on PikaPod](https://listmonk.app/static/images/host-pikapods.svg)](https://www.pikapods.com/pods?run=listmonk)[![Image 18: Deploy on Elestio](https://listmonk.app/static/images/host-elestio.webp)](https://elest.io/open-source/listmonk)[![Image 19: Deploy on Zeabur](https://listmonk.app/static/images/host-zeabur.svg)](https://zeabur.com/templates/5EDMN6)[![Image 20: Deploy to Cloudzy](https://listmonk.app/static/images/host-cloudzy.svg)](https://cloudzy.com/marketplace/listmonk/)

*listmonk has no affiliation with these providers

## One-way mailing lists

Manage millions of subscribers across single and double opt-in lists. Query and segment subscribers with SQL expressions.

![Image 21: Screenshot of list management feature](https://listmonk.app/static/images/lists.webp)

## Analytics

Built-in analytics to visualize campaign performance, bounces, top links and more across campaigns.

![Image 22: Screenshot of analytics feature](https://listmonk.app/static/images/analytics.webp)

## Templating

Create powerful, dynamic e-mail templates with the [Go templating language](https://golang.org/pkg/text/template/). Use template expressions, logic, and 100+ functions in subject lines and content. Write HTML e-mails using a visual drag-and-drop builder, a WYSIWYG editor, Markdown, raw syntax-highlighted HTML, or just plain text.

![Image 23: Screenshot of templating feature](https://listmonk.app/static/images/templating.webp)

## Performance

Multi-threaded, high-throughput, multi-SMTP e-mail queues. Throughput and sliding window rate limiting for fine grained control. Single binary application with nominal CPU and memory footprint that runs everywhere.

![Image 24: Screenshot of performance metrics](https://listmonk.app/static/images/performance.webp)

A production listmonk instance sending a campaign of 7+ million e-mails.

CPU usage is a fraction of a single core with peak RAM usage of 57 MB.

## Transactional mails

Simple API to send arbitrary transactional messages to subscribers using pre-defined templates. Send messages as e-mail, SMS, Whatsapp messages or any medium via Messenger interfaces.

![Image 25: Screenshot of transactional API](https://listmonk.app/static/images/tx.webp)

## Extensible

More than just e-mail campaigns. Messenger HTTP webhooks to send SMS, Whatsapp, FCM notifications, or any type of messages. Extensive API coverage for all features.

![Image 26: Screenshot of Messenger feature](https://listmonk.app/static/images/messengers.webp)

## And a lot more ...

Full privacy control for subscribers, OIDC SSO authentication with granular roles and permissions, granular API tokens, media library with S3-compatible backend and a lot more.

[Download](https://listmonk.app/#download)

![Image 27](https://listmonk.app/static/images/s3.webp)

## Developers

listmonk is free and open source software licensed under AGPLv3. If you are interested in contributing, check out the [GitHub repository](https://github.com/knadh/listmonk) and refer to the [developer setup](https://listmonk.app/docs/developer-setup). The backend is written in Go and the frontend is Vue with Buefy for UI.

© 2018-2026 / [Kailash Nadh](https://nadh.in/)
