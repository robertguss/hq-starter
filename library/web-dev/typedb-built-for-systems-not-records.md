---
tags:
  - library
title: "TypeDB - Built for systems, not records"
url: "https://typedb.com/"
company: [personal]
topics: []
created: 2026-02-15
source_type: raindrop
raindrop_id: 1603674063
source_domain: "typedb.com"
source_type_raindrop: link
collection: "Web Dev"
collection_id: 69284319
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Tables and edges capture your data, but they force system logic into code. TypeDB is a systems database. It enforces that logic at the data layer, so your application doesn't have to reinvent it everywhere.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: TypeDB - Built for systems, not records

URL Source: https://typedb.com/

Markdown Content:
# TypeDB: The knowledge engineering database
[](https://typedb.com/)

*   Products 

##### Services

[Database Meet TypeDB and TypeQL](https://typedb.com/features)[Enterprise Host TypeDB in your own environment](https://typedb.com/support#enterprise-support)[Community Edition The open-source edition of TypeDB](https://github.com/typedb/typedb) ##### Platform

[Cloud Scale effortlessly on our cloud platform](https://typedb.com/cloud)  ##### Tools

[Studio Build with our live web studio](https://typedb.com/docs/tools/studio)[Console Build in the terminal](https://typedb.com/docs/tools/console)[Driver SDKs Integrate your apps and services](https://typedb.com/docs/home/install/drivers)    
    *   ##### What is TypeDB?

[Read article](https://typedb.com/docs/home/what-is-typedb)
    *   ##### Why TypeDB?

[Read article](https://typedb.com/docs/home/why-typedb)
    *   ##### Start building

[Go to dashboard](https://cloud.typedb.com/sign-up)

*   Solutions ##### By use case

[Cyber threat intelligence TypeDB in CTI](https://typedb.com/use-cases/cyber-threat-intelligence)[Agentic systems TypeDB in agentic systems and AI](https://typedb.com/use-cases/agentic-systems)[Knowledge graphs TypeDB as a knowledge graph](https://typedb.com/use-cases/knowledge-graphs)  ##### By industry

[Financial intelligence TypeDB in financial intelligence](https://typedb.com/use-cases/financial-intelligence)[Robotics TypeDB in autonomous robots](https://typedb.com/use-cases/robotics)   [Startup program Are you a builder or breaker?](https://typedb.com/startup-program)[Code examples Samples built on real-world use cases](https://typedb.com/docs/examples/use-cases)  
*   Learn ##### Learn

[TypeDB Docs Browse TypeDB's developer docs](https://typedb.com/docs)[Quickstart TypeDB quickstart tutorial](https://typedb.com/docs/home/get-started/)[Examples Learn from examples and use cases](https://typedb.com/docs/examples/)[TypeDB Academy An end-to-end learning experience](https://typedb.com/docs/academy/)  ##### Content

[Blog Dev blogs, news, and insights](https://typedb.com/blog)[Research Academic research papers](https://typedb.com/papers)[Videos Be sure to like and subscribe](https://www.youtube.com/@typedb)   [Enterprise support Dedicated support for your business](https://typedb.com/support)[Community chat server Live chat with our Discord community](https://typedb.com/discord)  
*   [Pricing](https://typedb.com/pricing)

[4k](https://github.com/typedb/typedb)*   [Get in touch](https://typedb.com/#contact)
*   [Sign in](https://cloud.typedb.com/sign-in)
*   [Start building](https://cloud.typedb.com/sign-up)

# The knowledge engineering database

Built on a typed hypergraph with native inheritance and polymorphism, TypeDB is for teams building systems that need to provide deep context and reasoning efficiently.

We are the database that models how you think.

[Start building](https://cloud.typedb.com/sign-up)[Go open source](https://typedb.com/docs/home/install/ce)[Explore docs](https://typedb.com/docs)

1.   1
2.   2
3.   3
4.   4
5.   5
6.   6
7.   7

```typeql
insert
$cypher isa language;
$typeql isa language;
$evo isa evolution (past: $sql, future: $typeql);
```

## Learn about the hot topics at TypeDB

[![Image 4](https://cdn.sanity.io/images/xndl14mc/production/410c1f1e7f83a8bfd753127db4cb99d2f74b3142-1920x1096.png) ### The power of first-class Attributes: When every fish is aquatic, but not everything aquatic is a fish. TypeDB's first-class attributes let you define a concept once and connect it everywhere. Read article](https://typedb.com/blog/the-power-of-first-class-attributes-when-every-fish-is-aquatic-but-not-everything-aquatic-is-a-fish)[![Image 5](https://cdn.sanity.io/images/xndl14mc/production/40bfae3d6a1cbe5f22fa3d8707762d3cb29f54c0-1920x1080.webp) ### Inside TypeDB Studio: Part 2 - Querying Read article](https://typedb.com/blog/inside-typedb-studio-part-2-querying)[![Image 6](https://cdn.sanity.io/images/xndl14mc/production/903b4a2d01e2695f552d803fc3d0fcc338b50909-1920x1080.png) ### Everyone is making structured graphs now Let's look at how and why graph-y databases are validating structure. Read article](https://typedb.com/blog/everyone-is-making-structured-graphs-now)[![Image 7](https://cdn.sanity.io/images/xndl14mc/production/eba34a003e0a2391f01dd0f998d53a4034a84e7a-1920x1080.png) ### The deal graph: How knowledge graphs change the way banks execute complex transactions A major acquisition involves multiple parties, with multiple relationships, and decisions that depend on understanding how all of them connect. Many banks are still managing this in spreadsheets. Read article](https://typedb.com/blog/knowledge-graphs-in-banking)[![Image 8](https://cdn.sanity.io/images/xndl14mc/production/b0ead70f51dc613fe44c41f3e40ce87fb90fcda0-512x512.webp) ### TypeDB C# driver: bringing .NET to TypeDB 3 Announcing the new C# driver for TypeDB. Read article](https://typedb.com/blog/typedb-c-driver-bringing-net-to-typedb-3)

[Read more in blog](https://typedb.com/blog)

## Structured for machines, intuitive for humans

TypeQL is human readable, machine writable language built on modern programming paradigms, that allows you to embed logic into the database.

Its clarity and structured nature make it perfect for LLMs and vibe coding, readying your data for the next wave of AI-driven applications and automation.

1.   1
2.   2
3.   3
4.   4
5.   5
6.   6
7.   7
8.   8
9.   9
10.   10
11.   11
12.   12
13.   13
14.   14
15.   15
16.   16
17.   17
18.   18
19.   19
20.   20
21.   21
22.   22
23.   23
24.   24
25.   25

```typeql
define
attribute username, value string;
attribute page-visibility, value string @values("public", "private");
attribute address, value string;
attribute dob, value date;

entity profile @abstract, 
  owns username @key,
  owns page-visibility @card(1);

entity person,
  sub profile,
  owns dob,
  plays employment:employee;

entity company,
  sub profile,
  owns address @card(0..),
  plays employment:employer;

relation employment,
  relates employer,
  relates employee;
```

## A database for complex systems

Forget tables and joins. TypeDB is built to model multi-dimensional, highly interconnected data, without losing structure or semantic meaning.

TypeDB Studio

![Image 9](https://cdn.sanity.io/images/xndl14mc/production/374bf54e38135ebc3b8714143f7e603bbf60251a-3922x2178.webp)

## A programming language, not just a schema

With TypeQL, you describe your data like code. It’s readable, writable, and logical, enabling full expressiveness with real constraints and inference.

### TypeDB

Find users that have access to different types of resources. Return user emails, resource IDs and resource types

1.   1
2.   2
3.   3
4.   4
5.   5
6.   6
7.   7
8.   8
9.   9
10.   10
11.   11

```typeql
match
  $user isa user;
  $resource isa! $resource-type;
  $resource-type sub resource;
  resource-ownership (resource: $resource, owner: $user);
fetch {
  "email": $user.email,
  "resource-id": $resource.id,
  "resource-type": $resource-type
};
```

### Relational

In relational DBs, define one table for each resource type, using a UNION ALL query and JOINs to fetch interconnected data

1.   1
2.   2
3.   3
4.   4
5.   5
6.   6
7.   7
8.   8
9.   9
10.   10
11.   11
12.   12
13.   13
14.   14
15.   15
16.   16
17.   17
18.   18
19.   19
20.   20
21.   21
22.   22
23.   23
24.   24
25.   25
26.   26
27.   27
28.   28
29.   29
30.   30
31.   31
32.   32
33.   33
34.   34
35.   35
36.   36
37.   37
38.   38
39.   39
40.   40
41.   41
42.   42
43.   43
44.   44
45.   45
46.   46
47.   47
48.   48
49.   49
50.   50
51.   51
52.   52
53.   53
54.   54
55.   55
56.   56
57.   57
58.   58
59.   59
60.   60
61.   61
62.   62
63.   63
64.   64
65.   65
66.   66
67.   67
68.   68
69.   69
70.   70
71.   71
72.   72
73.   73
74.   74
75.   75
76.   76
77.   77
78.   78
79.   79
80.   80
81.   81
82.   82
83.   83
84.   84
85.   85
86.   86

```sql
SELECT
  ue.email AS email,
  'file' AS resource_type,
  f.path AS id
FROM users u
JOIN user_emails ue
ON u.id = ue.user_id
JOIN resource_ownerships ro
ON u.id = ro.user_id
JOIN resources r
ON ro.resource_id = r.id
JOIN files f
ON r.id = f.resource_id
UNION ALL
SELECT
  ue.email AS email,
  'directory' AS resource_type,
  d.path AS id
FROM users u
JOIN user_emails ue
ON u.id = ue.user_id
JOIN resource_ownerships ro
ON u.id = ro.user_id
JOIN resources r
ON ro.resource_id = r.id
JOIN directories d
ON r.id = d.resource_id
UNION ALL
SELECT
  ue.email AS email,
  'commit' AS resource_type,
  c.hash AS id
FROM users u
JOIN user_emails ue
ON u.id = ue.user_id
JOIN resource_ownerships ro
ON u.id = ro.user_id
JOIN resources r
ON ro.resource_id = r.id
JOIN commits c
ON r.id = c.resource_id
UNION ALL
SELECT
  ue.email AS email,
  'repository' AS resource_type,
  re.name AS id
FROM users u
JOIN user_emails ue
ON u.id = ue.user_id
JOIN resource_ownerships ro
ON u.id = ro.user_id
JOIN resources r
ON ro.resource_id = r.id
JOIN repositories re
ON r.id = re.resource_id
UNION ALL
SELECT
  ue.email AS email,
  'table' AS resource_type,
  t.name AS id
FROM users u
JOIN user_emails ue
ON u.id = ue.user_id
JOIN resource_ownerships ro
ON u.id = ro.user_id
JOIN resources r
ON ro.resource_id = r.id
JOIN tables t
ON r.id = t.resource_id
UNION ALL
SELECT
  ue.email AS email,
  'database' AS resource_type,
  f.name AS id
FROM users u
JOIN user_emails ue
ON u.id = ue.user_id
JOIN resource_ownerships ro
ON u.id = ro.user_id
JOIN resources r
ON ro.resource_id = r.id
JOIN databases d
ON r.id = d.resource_id;
```

### Document

In document DBs, freeform structures make writes trivial, but reading and validating data becomes a significant challenge

1.   1
2.   2
3.   3
4.   4
5.   5
6.   6
7.   7
8.   8
9.   9
10.   10
11.   11
12.   12
13.   13
14.   14
15.   15
16.   16
17.   17
18.   18
19.   19
20.   20
21.   21
22.   22
23.   23
24.   24
25.   25
26.   26
27.   27
28.   28
29.   29
30.   30
31.   31
32.   32
33.   33
34.   34
35.   35
36.   36
37.   37
38.   38
39.   39
40.   40
41.   41
42.   42
43.   43
44.   44
45.   45
46.   46
47.   47
48.   48
49.   49
50.   50
51.   51
52.   52
53.   53
54.   54
55.   55
56.   56
57.   57
58.   58
59.   59
60.   60
61.   61
62.   62
63.   63
64.   64
65.   65
66.   66
67.   67
68.   68
69.   69
70.   70
71.   71
72.   72
73.   73
74.   74
75.   75
76.   76
77.   77
78.   78
79.   79
80.   80
81.   81
82.   82
83.   83
84.   84
85.   85
86.   86
87.   87
88.   88
89.   89
90.   90
91.   91
92.   92
93.   93
94.   94
95.   95

```typescript
db.resource_ownerships.aggregate( [
  {
    $lookup:
    {
      from: "resources",
      localField: "resource",
      foreignField: "_id",
      as: "resource"
    }
  },
  {
    $unwind:
    {
      path: "$resource"
    }
  },
  {
    $lookup:
    {
      from: "users",
      localField: "owner",
      foreignField: "_id",
      as: "owner"
    }
  },
  {
    $unwind:
    {
      path: "$owner"
    }
  },
  {
    $unwind:
    {
      path: "$owner.emails"
    }
  },
  {
    $addFields:
    {
      resource_id: {
        $switch: {
          branches: [
            {
              case: { 
                $eq: ["$resource.resource_type", "file"]
              }, 
              then: "$resource.path" 
            },
            {
              case: { 
                $eq: ["$resource.resource_type", "directory"]
              }, 
              then: "$resource.path" 
            },
            {
              case: { 
                $eq: ["$resource.resource_type", "commit"]
              }, 
              then: "$resource.hash" 
            },
            {
              case: { 
                $eq: ["$resource.resource_type", "repository"]
              }, 
              then: "$resource.name" 
            },
            {
              case: { 
                $eq: ["$resource.resource_type", "table"]
              }, 
              then: "$resource.name" 
            },
            {
              case: { 
                $eq: ["$resource.resource_type", "database"]
              }, 
              then: "$resource.name" 
            }
          ]
        }
      }
    }
  },
  {
    $project: {
      _id: false,
      email: "$owner.emails",
      resource_type: "$resource.resource_type",
      id: "$resource_id"
    }
  }
 ] )
```

### Graph

In graph DBs, properties are attached directly to the nodes that own them, rather than being nodes themselves

1.   1
2.   2
3.   3
4.   4
5.   5
6.   6
7.   7
8.   8
9.   9
10.   10
11.   11
12.   12
13.   13
14.   14
15.   15
16.   16
17.   17
18.   18
19.   19
20.   20
21.   21
22.   22
23.   23
24.   24
25.   25

```cypher
MATCH
  (user:User)-[:OWNS]->(rsrc:Resource)
WITH
  rsrc,
  [user.primary_email] + user.alias_emails AS emails,
  labels(rsrc) AS resource_types,
  keys(rsrc) AS properties
UNWIND emails AS email
UNWIND resource_types AS resource_type
WITH
  rsrc, email, resource_type, properties,
  {
    File: "path",
    Directory: "path",
    Commit: "hash",
    Repository: "name",
    Table: "name",
    Database: "name"
  } AS id_type_map
WHERE resource_type IN keys(id_type_map)
AND id_type_map[resource_type] IN properties
RETURN email, resource_type, rsrc[id_type_map[resource_type]] AS id
```

## The power of a knowledge graph

TypeDB uses a hypergraph model to represent entities, relationships, and nested concepts natively, making it uniquely suited for applications where context, structure, and inference matter.

TypeDB Studio

![Image 10](https://cdn.sanity.io/images/xndl14mc/production/e020b75137bcba24c4a7a85e09f34a88074d8262-4086x2172.webp)

## Explore with our live web studio

Want to dive in and see what TypeDB can do? Sign up to Cloud and connect instantly to our web studio to see what we can do in just a few minutes.

TypeDB Studio

![Image 11](https://cdn.sanity.io/images/xndl14mc/production/afab34703c3c49b6f5442e8f9161c95b14d5d54e-4086x2172.webp)

## Collaborate with other builders

We are used by major enterprises, cutting edge AI businesses, world-leading researchers, and everything else you can imagine.

#### [GitHub](https://github.com/typedb)#### [Discord](https://typedb.com/discord)#### [YouTube](https://www.youtube.com/@typedb)#### [LinkedIn](https://www.linkedin.com/company/typedb)

## Leverage the power of programming.

In your database

Using the Polymorphic-Entity-Relations-Attribute (PERA) model as the basis of TypeQL leads to a general, expressive, intuitive, and strongly typed language! Since data must be instantiated from the schema, the system can make strong guarantees about data integrity and shape.

## Write less to do more

Queries are shorter, more intuitive, and more expressive. You don’t have to specify how data joins; Just say what you need and retrieve it in a simple, single database call.

[Learn more](https://typedb.com/docs)

## Eliminate a significant amount of your tech debt

Data logic belongs in the structure, not the query. Our query variables match all valid types so doesn’t need updating even when you add new subtypes.

[Learn more](https://typedb.com/docs)

## Your data holds more answers than you know

TypeDB is the only database built for interconnected data and intelligent applications. Build systems that understand, reason, and adapt, solving problems traditional databases cannot.

TypeDB Studio

![Image 12](https://cdn.sanity.io/images/xndl14mc/production/374bf54e38135ebc3b8714143f7e603bbf60251a-3922x2178.webp)

## Batteries included

Connect your production application with our dedicated drivers, supporting the major languages, with more added regularly.

[![Image 13](https://cdn.sanity.io/images/xndl14mc/production/58545a6c18d9a648f9e86543107b97ca6d196ec7-106x106.svg)Develop with ### Rust](https://typedb.com/docs/home/install/drivers#_rust)[![Image 14](https://cdn.sanity.io/images/xndl14mc/production/01ccaf6b86165033da9d9d07fb63e72cfca0acfb-234x428.svg)Develop with ### Java](https://typedb.com/docs/home/install/drivers#_java)[![Image 15](https://cdn.sanity.io/images/xndl14mc/production/4b320c65481ee7630795330f6d288779c785ecdf-83x101.svg)Develop with ### Python](https://typedb.com/docs/home/install/drivers#_python)[![Image 16](https://cdn.sanity.io/images/xndl14mc/production/cc380bfc50845deb8fc583c0e3608b7e9775182c-512x512.svg)Develop with ### TypeScript](https://typedb.com/docs/home/install/drivers#_typescript_http)

[![Image 17](https://cdn.sanity.io/images/xndl14mc/production/7a05581e3e4f22339b604d195b160e5e696298f4-256x288.svg) #### C#](https://typedb.com/docs/home/install/drivers)[![Image 18](https://cdn.sanity.io/images/xndl14mc/production/2eac840744bac6c55eb85f1c8968ff9fe66791bf-306x344.svg) #### C++](https://typedb.com/docs/home/install/drivers)[![Image 19](https://cdn.sanity.io/images/xndl14mc/production/3f96dc57e3ce5740c859896e7898c0cd226fe966-360x405.png) #### C](https://typedb.com/docs/home/install/drivers)#### [View all in docs →](https://typedb.com/docs/home/install/drivers)

## Useful resources to get started

[![Image 20](https://cdn.sanity.io/images/xndl14mc/production/d20958db991eec9305c8daa3b8bb71e565aeeeb2-1920x1080.webp) ### First look at TypeDB 3 benchmarks A first look at TypeDB 3 benchmarks, analyzing performance at scale on OLTP workloads using comparisons to previous versions of TypeDB and Neo4j Read article](https://typedb.com/blog/first-look-at-typedb-3-benchmarks)[![Image 21](https://cdn.sanity.io/images/xndl14mc/production/c43195f62f2e9979898088909e84870d8f2cdcf9-1920x1080.webp) ### The case for a polymorphic database Most databases can't model the real world. Learn how TypeDB brings polymorphism into the schema, so your data becomes safer, smarter, and easier to evolve. Read article](https://typedb.com/blog/the-case-for-a-polymorphic-database)[![Image 22](https://cdn.sanity.io/images/xndl14mc/production/b801f72482835faa5e916f64a1b87b90d73c9c33-1920x1080.webp) ### Why TypeDB isn't a graph, but it can behave as one Learn how TypeDB combines graph semantics with strong schema and reasoning to model complex domains. Read article](https://typedb.com/blog/why-typedb-isnt-a-graph-database-but-it-can-behave-as-one)[![Image 23](https://cdn.sanity.io/images/xndl14mc/production/bd687bc3edbdcd555f51d322bd514275f5475924-1920x1080.png) ### Why agents need ontologies Learn how ontology databases enable AI agent validation, multi-agent coordination, and explainable decisions. A guide to building safe operational agents. Read article](https://typedb.com/blog/why-agents-need-ontologies)

## Start free, upgrade when ready

## Go to production in weeks, not months

TypeDB delivers a clear, structured data model and a human-readable, beautiful query language, ideal for powering agentic systems, cyber threat intelligence, robotics and much more.

[Start building](https://cloud.typedb.com/sign-up)

![Image 24](https://cdn.sanity.io/images/xndl14mc/production/afab34703c3c49b6f5442e8f9161c95b14d5d54e-4086x2172.webp)

[Subscribe to Newsletter](https://typedb.com/#newsletter)

[undefined](https://github.com/typedb)[Discord](https://typedb.com/discord)[YouTube](https://www.youtube.com/@typedb)[LinkedIn](https://www.linkedin.com/company/typedb)

### Connect

*   [Chat on Discord](https://typedb.com/discord)
*   [Get in Touch](https://typedb.com/#contact)

### Products

*   [Database](https://typedb.com/features)
*   [Cloud](https://typedb.com/cloud)
*   [Studio](https://typedb.com/docs/tools/studio)
*   [Community Edition](https://typedb.com/docs/home/install/ce)
*   [Enterprise](https://typedb.com/support#enterprise-support)
*   [Pricing](https://typedb.com/pricing)

### Use Cases

*   [Cyber threat intelligence](https://typedb.com/use-cases/cyber-threat-intelligence)
*   [Agentic systems](https://typedb.com/use-cases/agentic-systems)
*   [Knowledge graphs](https://typedb.com/use-cases/knowledge-graphs)
*   [Financial intelligence](https://typedb.com/use-cases/financial-intelligence)
*   [Robotics](https://typedb.com/use-cases/robotics)

### Resources

*   [What is TypeDB?](https://typedb.com/docs/home/what-is-typedb)
*   [Why TypeDB?](https://typedb.com/docs/home/why-typedb)
*   [Lectures](https://typedb.com/lectures)
*   [Papers](https://typedb.com/papers)
*   [Blog](https://typedb.com/blog)
*   [Engineering Blog](https://typedb.com/blog/category/engineering)
*   [Product Blog](https://typedb.com/blog/category/product)
*   [Insights](https://typedb.com/blog/category/insights)
*   [Startup Program](https://typedb.com/startup-program)

### Learn

*   [Documentation](https://typedb.com/docs/home/)
*   [Examples](https://typedb.com/docs/examples/)
*   [Guides](https://typedb.com/docs/guides)
*   [Core Concepts](https://typedb.com/docs/core-concepts/)
*   [Tools](https://typedb.com/docs/tools/)
*   [Maintenance](https://typedb.com/docs/maintenance-operation)
*   [Reference](https://typedb.com/docs/reference)
*   [TypeQL Reference](https://typedb.com/docs/typeql-reference/)
*   [TypeDB Academy](https://typedb.com/docs/academy/)

### Company

*   [LinkedIn](https://www.linkedin.com/company/typedb)
*   [GitHub](https://github.com/typedb)
*   [Privacy Policy](https://typedb.com/legal/privacy-policy)
*   [Terms of Service](https://typedb.com/legal/terms-of-service)

© 2026 TypeDB Ltd 

 TypeDB™ and TypeQL™ are trademarks of TypeDB Ltd

[Feedback](https://typedb.com/)
