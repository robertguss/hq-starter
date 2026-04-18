---
tags:
  - library
title: "10 years of personal finances in plain text files"
url: "https://sgoel.dev/posts/10-years-of-personal-finances-in-plain-text-files/"
company: [personal]
topics: []
created: 2026-01-03
source_type: raindrop
raindrop_id: 1521933888
source_domain: "sgoel.dev"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

I've been tracking my finances using Beancount in plain text files for 10 years. Here are the numbers, the workflow, and why I believe plaintext accounting will outlive any app.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: 10 years of personal finances in plain text files

URL Source: https://sgoel.dev/posts/10-years-of-personal-finances-in-plain-text-files/

Markdown Content:
Dec 20, 2025

January 2026 will mark 10 years since I started storing my personal finances in plain text files using Beancount. Since January 2016, I've taken out about 30-45 minutes every single month to download my monthly bank statements and import them into my Beancount ledger.

There's a lot to talk about here, but let's start with some fun numbers!

## The 10 year old Beancount ledger

10 years of financial transactions is a lot of data! All in all, my ledger contains over 45,000 lines of Beancount entries spread across 16 plain text files. All of it is stored in a `finances` directory (version controlled) on my laptop. Here's a snapshot:

```
❯ find . -name "*.beancount" | xargs wc -l
    4037 ./includes/2020.beancount
    3887 ./includes/2018.beancount
      27 ./includes/cash.beancount
    4398 ./includes/2021.beancount
    5531 ./includes/2019.beancount
    5267 ./includes/2022.beancount
    3287 ./includes/2017.beancount
    5506 ./includes/2024.beancount
    5606 ./includes/2023.beancount
    1454 ./includes/2016.beancount
    1089 ./includes/open/04-expenses.beancount
      66 ./includes/open/03-income.beancount
      11 ./includes/open/05-liabilities.beancount
      37 ./includes/open/02-assets.beancount
       1 ./includes/open/01-equity.beancount
    4807 ./main.beancount
   45011 total
```

Running `bean-query` on `main.beancount` tells me I have about 10,000 transactions in total, that in turn contain about 20,000 postings (in double-entry bookkeeping, one transaction may have multiple postings).

```
❯ uv run bean-query main.beancount
Input file: "Goel"
Ready with 12466 directives (19743 postings in 9895 transactions).
beanquery>
```

There are 1086 accounts in total.

```
beanquery> select count(*) from (select distinct(account));
coun
----
1086
```

... which does not mean that there are 1086 **bank** accounts. Accounts in Beancount are virtual, and you can create as many as you like. Imagine one account for categorizing supermarket spending, one for tracking your income, one for your Netflix subscription, and so on.

Next, there are about 500 documents in the repository.

```
❯ find documents/ -name "*.pdf" | wc -l
     507
```

Beancount lets you attach documents (e.g. receipts or invoices) to transactions, that makes bookkeeping very efficient. I love the fact that whenever I need to do my tax returns, I can just take a look at my Beancount ledger and find all the invoices right there next to the relevant transaction.

Lastly, in terms of postings, I started out with 715 in the year 2016, and the year 2023 was the busiest so far in terms of just the total postings count.

```
beanquery> select year(date), count(*) where year(date) < 2025 group by year(date);
year  coun
----  ----
2016   715
2017  1422
2018  1605
2019  2437
2020  1582
2021  2022
2022  2435
2023  2651
2024  2602
```

## The Monthly Ritual

I wrote earlier that every month I take about 30-45 minutes to import my financial transactions into Beancount. What does that workflow look like? I wrote another, much more detailed [blog post](https://sgoel.dev/posts/how-you-can-track-your-personal-finances-using-python/) about it a few years ago, but here's a gist.

It starts with me logging in to my bank account(s) to download my monthly statement(s) in CSV (CSV because it's much more predictable to parse compared to PDF). I then run these CSV files through what's called an "importer", that converts this CSV data into data structures that Beancount understands. I then append all those extracted entries into my current `.beancount` file (which is the main file containing **all** my financial transactions in plain text). I then go through each entry one by one and make sure it's balanced (in double-entry bookkeeping, all the postings in a transaction must sum to zero, and not all postings/transactions that an importer outputs are balanced). Some of that balancing is manual and some of it is automated (e.g. the importer code can look at the transaction's description and decide which account it should go into, and balance automatically). This last part (balancing) is where most of those 30-45 minutes go.

Whenever a new year starts, I move all the transactions from the past year into a `<year>.beancount` file and add an `include <year.beancount>` in the active `main.beancount`file, mostly to avoid the main file from becoming too long. Not that it would be an issue for Beancount, but just for the sake of readability.

With such a workflow, all my financial transactions from the beginning of time are contained in a few plain text files in one directory on my laptop.

## Building Beancount Importers for German Banks

Beancount only provides the foundations for working with money, but it has no knowledge of what your bank statements look like. This is where the concept of an importer comes in. An importer is a (Python) class that takes in a bank statement of sorts (e.g. a CSV export of your transactions) and converts them into something that Beancount can work with.

I live in Germany and my bank accounts are with German banks, so I had to write a few importers for a few different banks, specifically [beancount-dkb](https://github.com/siddhantgoel/beancount-dkb), [beancount-ing](https://github.com/siddhantgoel/beancount-ing), [beancount-n26](https://github.com/siddhantgoel/beancount-n26), and [beancount-commerzbank](https://github.com/siddhantgoel/beancount-commerzbank). I closed out my Commerzbank account a while ago, so I don't maintain that integration anymore, but the first three libraries are actively maintained (and used)!

## From User to Author

My start with Beancount was a bit bumpy. The documentation is very comprehensive but as a newcomer, I found it tricky to get a grasp on the overall workflow. It took me some trial and error to figure things out and have that "aha" moment.

I figured that if I found it tricky, maybe it's tricky for others as well. So I wrote a short book to help newcomers get up and running with Beancount easily. If you're interested, here's a link: [https://personalfinancespython.com](https://personalfinancespython.com/).

The feedback on the book has been super positive. It got mentioned on Beancount's [external contributions](https://beancount.github.io/docs/external_contributions.html) page, and the [reader reviews](https://personalfinancespython.com/#testimonials) have all been very encouraging!

## Closing Thoughts

Having all my finances in a bunch of plain text files tracked in a git repository feels invaluable to me. And hitting the 10 years mark on that almost feels like a milestone.

Perhaps the nicest bit about all this is that this data is sitting on **my own machine**, not in some data center somewhere else. All of it is in plain text files that I can open up in my editor, and analyze using the tools that the Beancount ecosystem gives me. All of it will outlive any app or service, and that, I feel, is why plaintext accounting is so powerful.
