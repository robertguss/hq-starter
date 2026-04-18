---
tags:
  - library
title: "Announcing Rolldown-Vite"
url: "https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev"
company: [personal]
topics: []
created: 2025-06-05
source_type: raindrop
raindrop_id: 1138916032
source_domain: "voidzero.dev"
source_type_raindrop: article
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

We are building the next generation of JavaScript tooling

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Announcing Rolldown-Vite

URL Source: https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev

Markdown Content:
TL;DR: Try out the Rolldown-powered Vite today by using the `rolldown-vite` package instead of the default `vite` package. It is a drop-in replacement, as Rolldown will become the default bundler for Vite in the future. Switching should reduce your build time, especially for larger projects. [Reach out](https://forms.gle/WQgjyzYJpwurpxWKA) to discover production use cases!

* * *

Over the last year, we've been working on [Rolldown](https://rolldown.rs/), a Rust-based next-generation bundler, as part of a broader effort to modernize Vite's core. Alongside Rolldown, we've developed [Oxc](https://oxc.rs/), a collection of high-performance JavaScript tools, that includes a parser, transformer, resolver, and minifier, as well as a linter and soon also a formatter. It acts as foundational layer for Rolldown, providing the necessary building blocks for efficient JavaScript and TypeScript processing.

Today, we're excited to announce that the Rolldown-powered Vite version has reached initial feature parity with today's Vite. This means you can try it as a drop-in replacement and experience the benefits right away as part of a technical preview.

Thanks to early adopters, we were able to test `rolldown-vite` with a range of projects, from basic setups to large-scale enterprise apps. The results have been impressive, with production build time reductions from 3x to 16x, and memory usage during the build process cut by up to 100x. Take a look at the [real-world impact section](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#real-world-impact) for more details.

We encourage you to try out `rolldown-vite` and share your feedback to contribute to the future development of Vite's bundling infrastructure.

## Using `rolldown-vite`[​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#using-rolldown-vite)

Getting started with `rolldown-vite` is straightforward. If you have an existing Vite project, you can replace the `vite` package with `rolldown-vite` by using an alias in your `package.json`:

json

```
{
  "dependencies": {
    "vite": "npm:rolldown-vite@latest"
  }
}
```

If you use VitePress, or a meta-framework that lists Vite as a peer dependency, you can use overrides to replace the `vite` package with `rolldown-vite` in your project:

npm pnpm yarn bun

json

```
{
  "overrides": {
    "vite": "npm:rolldown-vite@latest"
  }
}
```

json

```
{
  "pnpm": {
    "overrides": {
      "vite": "npm:rolldown-vite@latest"
    }
  }
}
```

json

```
{
  "resolutions": {
    "vite": "npm:rolldown-vite@latest"
  }
}
```

json

```
{
  "overrides": {
    "vite": "npm:rolldown-vite@latest"
  }
}
```

That's it! Now you can continue using Vite as you normally would, but with the added performance benefits of Rolldown. It's likely that you will see some warning messages about not-yet-supported options or deprecated APIs - we will continue to smooth those out across the ecosystem.

`rolldown-vite` is currently distributed as a separate package to allow for rapid iteration and to keep feedback and issues separate from the main `vite` package. This separation helps ensure stability for existing users while the Rolldown integration matures. Once `rolldown-vite` is stable, its changes will be merged into Vite and the separate package will be deprecated.

It also follows Vite's major and minor version numbers to maintain compatibility, but its patch versions are independent and may introduce breaking changes as development continues. For the latest updates and details, refer to the [`rolldown-vite` changelog](https://github.com/vitejs/rolldown-vite/blob/rolldown-vite/packages/vite/CHANGELOG.md).

* * *

## Ensuring Compatibility [​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#ensuring-compatibility)

Compatibility is a top priority for `rolldown-vite`. To ensure a smooth experience, we created a forked version of [Vite ecosystem CI](https://github.com/vitejs/vite-ecosystem-ci/blob/rolldown-vite/README-temp.md) and ran it against `rolldown-vite`. We have got the tests passing for most frameworks and plugins, but do note some frameworks or advanced use cases may still have compatibility gaps. We also recommend checking the [Rolldown migration guide](https://main.vite.dev/guide/rolldown#compatibility) for the latest compatibility notes, known issues, and migration tips. If you run into problems, please report them so we can improve support across the ecosystem.

### `esbuild` as optional dependency [​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#esbuild-as-optional-dependency)

In the current stable version of Vite, `esbuild` is a core dependency used for tasks like transforming and minifying production builds, as well as powering parts of the development server. Many Vite plugins also rely on `esbuild` through utility functions provided by Vite, such as file transformations.

With `rolldown-vite`, `esbuild` is no longer required. Instead, all internal transformations and minification are handled by Oxc, leading to improved performance using a single foundational layer. This means you don't need to install `esbuild` as a dependency unless you're using a Vite plugin that explicitly requires it and doesn't yet support Oxc transforms.

We are actively collaborating with plugin and framework authors to ensure that Vite plugins automatically leverage Oxc transforms when using `rolldown-vite`, resulting in faster builds.

If you are a plugin author, no matter if it is a Vite or Rollup plugin, you can start testing your plugins with `rolldown-vite` right away. A lot of plugins should work out of the box, but some might need tweaking, either for compatibility or performance reasons. Consult our [plugin author guide](https://vite.dev/guide/rolldown#plugin-framework-authors-guide) for more details.

* * *

## Real-World Impact [​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#real-world-impact)

`rolldown-vite` is still in development, but early adopters, ranging from side projects to large-scale enterprise apps, are already seeing remarkable results.

Some highlights:

*   _GitLab_ reduced build time from 2.5 minutes to just 40 seconds and cut their memory usage by 100x.
*   _Excalidraw_'s build dropped from 22.9 seconds to 1.4 seconds (**16x faster**).
*   _PLAID Inc._ saw one frontend's build time fall from 1 minute 20 seconds to 5 seconds (**16x faster**).
*   _Appwrite_ builds went from over 12 minutes to just 3 minutes, with memory usage being slashed by 4x.
*   _Particl_ achieved a nearly **10x speedup** compared to Vite (and almost **29x compared to Next.js**), with builds dropping from over a minute to just 6 seconds.

These results show not only much faster builds, but in some cases, orders of magnitude less memory usage. For more details or to share your own results, visit the [`vitejs/rolldown-vite-perf-wins`](https://github.com/vitejs/rolldown-vite-perf-wins) repository.

Oh and fun fact - this blog post you are reading right now is built with VitePress running on top of Rolldown-Vite, and the production build takes only 1.8s on Netlify.

* * *

## What Comes Next? [​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#what-comes-next)

Vite is generally known for its unbundled native ESM dev server, which is responsible for the fast startup time and almost instant feedback. Nevertheless, we’ve seen limitations of this approach for projects at unconventional scale, especially in Enterprise setups. To address these, we are working on a **full-bundle mode** for the dev server. With Rolldown’s performance, this mode aims to improve dev server startup times, especially for large projects, while maintaining or even enhancing startup speed for small and medium projects.

Alongside this, we plan to "rustify" more of Vite’s internals to reduce communication overhead and unlock even greater performance gains.

### Roadmap for Rolldown in Vite [​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#roadmap-for-rolldown-in-vite)

We've planned three phases for the transition to Rolldown, each designed to ensure a smooth migration while gathering valuable feedback from the community:

1.   **Phase One (Current)**: `rolldown-vite` is available as a separate package for early adopters. This allows us to gather feedback and make improvements based on real-world usage.
2.   **Phase Two**: All changes from `rolldown-vite` will be merged into the main Vite codebase when considered stable. They will also come with an opt-in full-bundle mode for development. `rolldown-vite` will be deprecated at this point.
3.   **Phase Three**: The full-bundle mode will become the default for Vite.

At the current time of writing, we expect each phase to last several months. Keep in mind that the exact duration will be determined by various factors, most importantly feedback from the community and real world usage, as well as stability and compatibility.

* * *

## Give It a Try [​](https://voidzero.dev/posts/announcing-rolldown-vite?ref=console.dev#give-it-a-try)

We encourage you to try `rolldown-vite` in your projects today! Your feedback will help shape the future of Vite's bundling infrastructure. In case you encounter any issues, such as missing or broken features, unclear error messages or performance degradations, please make sure to report these in the [`rolldown-vite` repository](https://github.com/vitejs/rolldown-vite) (not the main Vite repo). If you want to pose questions or discuss in real time, make sure to join the [Rolldown Discord](https://chat.rolldown.rs/).
