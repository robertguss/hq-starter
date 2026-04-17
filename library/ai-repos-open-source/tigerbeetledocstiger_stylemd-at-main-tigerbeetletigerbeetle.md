---
tags:
  - library
title: "tigerbeetle/docs/TIGER_STYLE.md at main · tigerbeetle/tigerbeetle"
url: "https://github.com/tigerbeetle/tigerbeetle/blob/main/docs/TIGER_STYLE.md"
company: [personal]
topics: []
created: 2026-02-01
source_type: raindrop
raindrop_id: 1572537966
source_domain: "github.com"
source_type_raindrop: link
collection: "AI Repos & Open Source"
collection_id: 69284315
hydrated: true
hydrated_at: 2026-04-17
hydrated_via: github-api
---
## Excerpt

The financial transactions database designed for mission critical safety and performance. - tigerbeetle/tigerbeetle

## Raw Content

<!-- Hydrated 2026-04-17 via github-api -->

# tigerbeetle

*TigerBeetle is the financial transactions database designed for mission critical safety and performance to power the next 30 years of [OLTP](https://docs.tigerbeetle.com/concepts/oltp).*

## Documentation

* <https://docs.tigerbeetle.com>
* [The Primeagen](https://www.youtube.com/watch?v=sC1B3d9C_sI) video introduction to our
  design decisions regarding performance, safety, and debit/credit primitives.
* [Redesigning OLTP for a New Order of Magnitude (QCon SF)](https://www.infoq.com/presentations/redesign-oltp/)
  talk with a deeper dive into TigerBeetle’s local storage engine and global consensus protocol.
* [TIGER_STYLE.md](./docs/TIGER_STYLE.md), the engineering methodology behind TigerBeetle.

## Start

Run a single-replica cluster on Linux (or [other platforms](https://docs.tigerbeetle.com/start/)):

```console
$ curl -Lo tigerbeetle.zip https://linux.tigerbeetle.com && unzip tigerbeetle.zip
$ ./tigerbeetle version
$ ./tigerbeetle format --cluster=0 --replica=0 --replica-count=1 --development 0_0.tigerbeetle
$ ./tigerbeetle start --addresses=3000 --development 0_0.tigerbeetle
```

Connect to the cluster and make a transfer:

```console
$ ./tigerbeetle repl --cluster=0 --addresses=3000
> create_accounts id=1 code=10 ledger=700, id=2 code=10 ledger=700;
{
  "timestamp": "1761605367595515148",
  "status": "tigerbeetle.CreateAccountStatus.created"
}
{
  "timestamp": "1761605367595515149",
  "status": "tigerbeetle.CreateAccountStatus.created"
}
> create_transfers id=1 debit_account_id=1 credit_account_id=2 amount=10 ledger=700 code=10;
{
  "timestamp": "1761605382476666870",
  "status": "tigerbeetle.CreateTransferStatus.created"
}
> lookup_accounts id=1, id=2;
{
  "id": "1",
  "user_data": "0",
  "ledger": "700",
  "code": "10",
  "flags": "",
  "debits_pending": "0",
  "debits_posted": "10",
  "credits_pending": "0",
  "credits_posted": "0"
}
{
  "id": "2",
  "user_data": "0",
  "ledger": "700",
  "code": "10",
  "flags": "",
  "debits_pending": "0",
  "debits_posted": "0",
  "credits_pending": "0",
  "credits_posted": "10"
}
```

Want to learn more? See <https://docs.tigerbeetle.com>.
