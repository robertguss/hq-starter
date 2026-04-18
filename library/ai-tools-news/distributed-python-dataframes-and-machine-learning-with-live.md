---
tags:
  - library
title: "Distributed Python dataframes and machine learning with Livebook and Elixir - Dashbit Blog"
url: "https://dashbit.co/blog/distributed-python-livebook"
company: [personal]
topics: []
created: 2026-03-12
source_type: raindrop
raindrop_id: 1639345858
source_domain: "dashbit.co"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Livebook now fully integrates with Python, from reproducible environments to distributed dataframes and machine learning.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Distributed Python dataframes and machine learning with Livebook and Elixir

URL Source: https://dashbit.co/blog/distributed-python-livebook

Markdown Content:
*    José Valim 
*    March 11th, 2026 
*   [python](https://dashbit.co/blog/tags/python) , [livebook](https://dashbit.co/blog/tags/livebook) , [distributed](https://dashbit.co/blog/tags/distributed)

Last year, we [announced the Pythonx project](https://dashbit.co/blog/running-python-in-elixir-its-fine), which embeds the Python runtime within the Erlang Virtual Machine and provide high-level bindings to Elixir.

This year, we were sponsored by [NGI0 Commons Fund](https://nlnet.nl/commonsfund), a fund established by [NLnet](https://nlnet.nl/) with financial support from the European Commission’s [Next Generation Internet](https://ngi.eu/) program, to bring full Python integration into Livebook, Elixir’s open source computational notebook platform.

This includes:

*   Creating reproducible Python environments with `uv` (announced last year alongside Pythonx)

*   Full-support for Python cells, including autocompletion, documentation on hover, and interoperability with Elixir cells

*   Zero-copy transfers of Apache Arrow data between Elixir and Python, allowing developers to load data in Elixir and transform it in Python or vice-versa

*   Distributed Python execution via the Erlang distribution, thanks to our distributed garbage collector

*   Support for spawning and running Python/Elixir code across K8s clusters and Fly.io machines

Our vision is to make Livebook a notebook platform where multiple languages coexist in the same runtime, enabling low-overhead data transfers and seamless interoperability between them. We bring Elixir’s distribution and fault-tolerance primitives to orchestrate Python workflows, allowing developers to swap between tools and scale them with the same ease that Elixir developers already expect.

To give these features a try, install the latest version of Livebook, head into the Learn section, and read our “Working with Python” notebook:

![Image 1](https://dashbit.co/images/posts/2026/python-learn.png)
## Installation and autocompletion

Livebook can manage both your Python and Elixir dependencies side-by-side. For Elixir, it uses Elixir’s built-in Mix tool, for Python, it uses `uv`. This ensures notebooks define fully reproducible environments:

![Image 2](https://dashbit.co/images/posts/2026/python-uv.png)
Once installed, you can navigate and access your dependencies as usual, with the latest Livebook version also supporting autocompletion of imports, modules, functions and variables, as well as documentation on hover:

![Image 3](https://dashbit.co/images/posts/2026/python-hover.png)
Livebook was already capable of displaying visualizations generated with Matplotlib, Seaborn, Plotly, and others, as well display tables from Polars and Pandas. But this release brings interoperabilty to the next level by supporting zero-copy data transfers thanks to Apache Arrow.

## Apache Arrow integration

Apache Arrow has become the lingua franca of data exchange. Elixir implements Apache Arrow via projects like [ADBC](https://hexdocs.pm/adbc), which allows developers to query and load data sources in Elixir, and now you can load data directly into PyArrow tables, so they can be manipulated by Polars and other libraries:

![Image 4](https://dashbit.co/images/posts/2026/python-df.png)
It is also possible to convert Python dataframes back into Elixir data through [`ADBC.Result.from_py`](https://hexdocs.pm/adbc/Adbc.Result.html#from_py/1).

## Distributed Python

Last but not least, we have added support for distributed Python execution on top of Erlang distribution. It is as simple as calling [`Pythonx.remote_eval/4`](https://hexdocs.pm/pythonx/Pythonx.html#remote_eval/4) with the name of the Erlang node you want to execute Python code at.

More importantly, we have implemented a distributed garbage collector. So when `remote_eval/4` returns, it simply holds references to objects in the remote node. This means you load a dataframe in one node, then pass the reference to another node, and decide if you want to explicitly copy it (using `pickle` or `cloudpickle`) or perform further remote execution.

To wrap it all up, we have also integrated Pythonx with [FLAME](https://github.com/phoenixframework/flame), which is a library by the Phoenix team that allows you to quickly start copies of your runtime on your Fly.io and Kubernetes clusters. This means that your notebook can now easily spawn new nodes, with your whole Elixir and Python environment, and run Python code in them:

![Image 5](https://dashbit.co/images/posts/2026/python-flame.png)
These spawned nodes are then automatically shutdown when our distributed garbage collector cleans up all remote Python references.

## Summary

2025 was deemed the “year of interoperability” for Elixir and we are very thankful to [NGI0 Commons Fund](https://nlnet.nl/commonsfund) for helping us fulfill this vision. The Python implementation sets the building blocks for future integrations, opening up the possibility of other runtimes benefiting from the distribution and fault-tolerance capabilities Elixir is known for, while paving new paths to Elixir adoption where interoperability is a strong requirement.

Kudos to [Jonatan Kłosko](https://github.com/jonatanklosko) for working on those features with support from [Michael Ruoss](https://github.com/mruoss) on the FLAME side.
