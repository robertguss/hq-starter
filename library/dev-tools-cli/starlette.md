---
tags:
  - library
title: "Starlette"
url: "https://www.starlette.io/"
company: [personal]
topics: []
created: 2025-05-23
source_type: raindrop
raindrop_id: 1068712787
source_domain: "starlette.io"
source_type_raindrop: link
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

The little ASGI library that shines.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Introduction - Starlette

URL Source: https://www.starlette.io/

Published Time: Sun, 22 Mar 2026 18:29:39 GMT

Markdown Content:
# Introduction - Starlette
- [x] - [x] 

[Skip to content](https://www.starlette.io/#introduction)

[❤️ Support Starlette via **sponsors**!](https://www.starlette.io/sponsorship/)[📚 Do you like the new docs? **Let us know!**](https://github.com/Kludex/starlette/discussions/3099)

[](https://www.starlette.io/ "Starlette")

 Starlette 

 Introduction 

 Search 

[Kludex/starlette](https://github.com/Kludex/starlette "Go to repository")

[](https://www.starlette.io/ "Starlette") Starlette  

[Kludex/starlette](https://github.com/Kludex/starlette "Go to repository")

*   - [x]  Introduction  [Introduction](https://www.starlette.io/) On this page  

    [Sponsorship](https://www.starlette.io/#sponsorship)

[Installation](https://www.starlette.io/#installation)
[Example](https://www.starlette.io/#example)
[Dependencies](https://www.starlette.io/#dependencies)
[Framework or Toolkit](https://www.starlette.io/#framework-or-toolkit)
[Modularity](https://www.starlette.io/#modularity)
*   - [x]  Features   Features  
    *   [Applications](https://www.starlette.io/applications/)
    *   [Requests](https://www.starlette.io/requests/)
    *   [Responses](https://www.starlette.io/responses/)
    *   [WebSockets](https://www.starlette.io/websockets/)
    *   [Routing](https://www.starlette.io/routing/)
    *   [Endpoints](https://www.starlette.io/endpoints/)
    *   [Middleware](https://www.starlette.io/middleware/)
    *   [Static Files](https://www.starlette.io/staticfiles/)
    *   [Templates](https://www.starlette.io/templates/)
    *   [Database](https://www.starlette.io/database/)
    *   [GraphQL](https://www.starlette.io/graphql/)
    *   [Authentication](https://www.starlette.io/authentication/)
    *   [API Schemas](https://www.starlette.io/schemas/)
    *   [Lifespan](https://www.starlette.io/lifespan/)
    *   [Background Tasks](https://www.starlette.io/background/)
    *   [Server Push](https://www.starlette.io/server-push/)
    *   [Exceptions](https://www.starlette.io/exceptions/)
    *   [Configuration](https://www.starlette.io/config/)
    *   [Thread Pool](https://www.starlette.io/threadpool/)
    *   [Test Client](https://www.starlette.io/testclient/)

*   [Release Notes](https://www.starlette.io/release-notes/)
*   - [x]  Community   Community  
    *   [Third Party Packages](https://www.starlette.io/third-party-packages/)
    *   [Contributing](https://www.starlette.io/contributing/)

 On this page  

[Sponsorship](https://www.starlette.io/#sponsorship)
[Installation](https://www.starlette.io/#installation)
[Example](https://www.starlette.io/#example)
[Dependencies](https://www.starlette.io/#dependencies)
[Framework or Toolkit](https://www.starlette.io/#framework-or-toolkit)
[Modularity](https://www.starlette.io/#modularity)

![Image 1: starlette](https://www.starlette.io/img/starlette.svg#only-light)![Image 2: starlette](https://www.starlette.io/img/starlette_dark.svg#only-dark)

_✨ The little ASGI framework that shines. ✨_

[![Image 3: Build Status](https://github.com/Kludex/starlette/workflows/Test%20Suite/badge.svg)](https://github.com/Kludex/starlette/actions)[![Image 4: Package version](https://badge.fury.io/py/starlette.svg)](https://pypi.org/project/starlette/)[![Image 5: Supported Python versions](https://img.shields.io/pypi/pyversions/starlette.svg?color=%2334D058)](https://pypi.org/project/starlette)[![Image 6: Discord](https://img.shields.io/discord/1051468649518616576?logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://discord.gg/RxKUF5JuHs)

* * *

**Documentation**: [https://starlette.dev](https://starlette.dev/)

**Source Code**: [https://github.com/Kludex/starlette](https://github.com/Kludex/starlette)

* * *

# Introduction

Starlette is a lightweight [ASGI](https://asgi.readthedocs.io/en/latest/) framework/toolkit, which is ideal for building async web services in Python.

It is production-ready, and gives you the following:

*   A lightweight, low-complexity HTTP web framework.
*   WebSocket support.
*   In-process background tasks.
*   Startup and shutdown events.
*   Test client built on `httpx`.
*   CORS, GZip, Static Files, Streaming responses.
*   Session and Cookie support.
*   100% test coverage.
*   100% type annotated codebase.
*   Few hard dependencies.
*   Compatible with `asyncio` and `trio` backends.
*   Great overall performance [against independent benchmarks](https://www.techempower.com/benchmarks/#hw=ph&test=fortune&l=zijzen-sf).

## Sponsorship

Help us keep Starlette maintained and sustainable by [becoming a sponsor](https://github.com/sponsors/Kludex).

**Current sponsors:**

[![Image 7: FastAPI](https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png)](https://fastapi.tiangolo.com/)[![Image 8: Hugging Face](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.svg)](https://huggingface.co/)

## Installation

```
pip install starlette
```

You'll also want to install an ASGI server, such as [uvicorn](https://www.uvicorn.org/), [daphne](https://github.com/django/daphne/), or [hypercorn](https://hypercorn.readthedocs.io/en/latest/).

```
pip install uvicorn
```

## Example

main.py
```
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def homepage(request):
    return JSONResponse({'hello': 'world'})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
])
```

Then run the application...

```
uvicorn main:app
```

## Dependencies

Starlette only requires `anyio`, and the following dependencies are optional:

*   [`httpx`](https://www.python-httpx.org/) - Required if you want to use the `TestClient`.
*   [`jinja2`](https://jinja.palletsprojects.com/) - Required if you want to use `Jinja2Templates`.
*   [`python-multipart`](https://multipart.fastapiexpert.com/) - Required if you want to support form parsing, with `request.form()`.
*   [`itsdangerous`](https://itsdangerous.palletsprojects.com/) - Required for `SessionMiddleware` support.
*   [`pyyaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) - Required for `SchemaGenerator` support.

You can install all of these with `pip install starlette[full]`.

## Framework or Toolkit

Starlette is designed to be used either as a complete framework, or as an ASGI toolkit. You can use any of its components independently.

main.py
```
from starlette.responses import PlainTextResponse

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)
```

Run the `app` application in `main.py`:

```
$ uvicorn main:app
INFO: Started server process [11509]
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Run uvicorn with `--reload` to enable auto-reloading on code changes.

## Modularity

The modularity that Starlette is designed on promotes building re-usable components that can be shared between any ASGI framework. This should enable an ecosystem of shared middleware and mountable applications.

The clean API separation also means it's easier to understand each component in isolation.

* * *

_Starlette is [BSD licensed](https://github.com/Kludex/starlette/blob/main/LICENSE.md) code.

Designed & crafted with care._

— ⭐️ —

 Made with [Zensical](https://zensical.org/)

[](https://github.com/Kludex/starlette "github.com")[](https://discord.com/invite/RxKUF5JuHs "discord.com")[](https://x.com/marcelotryle "x.com")[](https://www.linkedin.com/in/marcelotryle "www.linkedin.com")[](https://fastapiexpert.com/ "fastapiexpert.com")
