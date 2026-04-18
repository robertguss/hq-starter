---
tags:
  - library
title: "PocketBase - Open Source backend in 1 file"
url: "https://pocketbase.io/"
company: [personal]
topics: []
created: 2025-06-19
source_type: raindrop
raindrop_id: 1183002586
source_domain: "pocketbase.io"
source_type_raindrop: link
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Open Source backend in 1 file with realtime database, authentication, file storage and admin dashboard

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: PocketBase - Open Source backend in 1 file

URL Source: https://pocketbase.io/

Markdown Content:
# PocketBase - Open Source backend in 1 file

[![Image 1: PocketBase logo](https://pocketbase.io/images/logo.svg)Pocket**Base**v0.36.9](https://pocketbase.io/)

Go JavaScript

[FAQ](https://pocketbase.io/faq)[](https://github.com/pocketbase/pocketbase "GitHub Repo")[Documentation](https://pocketbase.io/docs)

Open Source backend

**in 1 file**

Realtime database

Authentication

File storage

Admin dashboard

![Image 2: Gopher](blob:http://localhost/6423885fd1dc1ff3158f95ef3d26e589)

![Image 3: PocketBase dashboard preview](blob:http://localhost/da1d1e5b54f60fd4d48c1a06a7b03276)

[Live demo](https://pocketbase.io/demo/)[Read the documentation](https://pocketbase.io/docs)

## Ready to use out of the box

#### Realtime database

Embedded performant database with schema builder, data validations, realtime subscriptions and easy to use REST api.

#### Authentication

Manage your app users and handle email/password and OAuth2 sign ups (Google, Facebook, GitHub, GitLab) without the hassle.

#### File storage

Safely store files locally or in a S3 storage. Easily attach media to your database records and generate thumbs on the fly.

#### Extendable

Use as a standalone app OR as a framework, that you can extend via Go and JavaScript hooks to create your own custom portable backend.

[Explore all features](https://pocketbase.io/docs)

JavaScript Dart

```
// JavaScript SDK
import PocketBase from 'pocketbase';

const pb = new PocketBase('http://127.0.0.1:8090');

...

// list and search for 'example' collection records
const list = await pb.collection('example').getList(1, 100, {
    filter: 'title != "" && created > "2022-08-01"',
    sort: '-created,title',
});

// or fetch a single 'example' collection record
const record = await pb.collection('example').getOne('RECORD_ID');

// delete a single 'example' collection record
await pb.collection('example').delete('RECORD_ID');

// create a new 'example' collection record
const newRecord = await pb.collection('example').create({
    title: 'Lorem ipsum dolor sit amet',
});

// subscribe to changes in any record from the 'example' collection
pb.collection('example').subscribe('*', function (e) {
    console.log(e.record);
});

// stop listening for changes in the 'example' collection
pb.collection('example').unsubscribe();
```

## Integrate nicely with your favorite frontend stack

[![Image 4: Flutter logo](https://pocketbase.io/images/flutter_logo.svg?v2)](https://github.com/pocketbase/dart-sdk)[![Image 5: Svelte logo](https://pocketbase.io/images/svelte_logo.svg?v2)](https://github.com/pocketbase/js-sdk)[![Image 6: Vue logo](https://pocketbase.io/images/vue_logo.svg?v2)](https://github.com/pocketbase/js-sdk)[![Image 7: React logo](https://pocketbase.io/images/react_logo.svg?v2)](https://github.com/pocketbase/js-sdk)[![Image 8: Angular logo](https://pocketbase.io/images/angular_logo.svg?v2)](https://github.com/pocketbase/js-sdk)

[FAQ](https://pocketbase.io/faq)[Discussions](https://github.com/pocketbase/pocketbase/discussions)[Documentation](https://pocketbase.io/docs)[JavaScript SDK](https://github.com/pocketbase/js-sdk)[Dart SDK](https://github.com/pocketbase/dart-sdk)

Pocket**Base**

[](mailto:support)[](https://github.com/pocketbase/pocketbase)

© 2023-2026 Pocket**Base**The Gopher artwork is from [marcusolsson/gophers](https://github.com/marcusolsson/gophers)

Crafted by [**Gani**](https://gani.bg/)
