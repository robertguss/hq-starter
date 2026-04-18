---
tags:
  - library
title: "Discord for Developers"
url: "https://discord.com/developers/docs/reference"
company: [personal]
topics: []
created: 2025-07-18
source_type: raindrop
raindrop_id: 1257114300
source_domain: "discord.com"
source_type_raindrop: link
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---

## Excerpt

Build games, experiences, and integrations for millions of users on Discord.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: API Reference - Documentation - Discord

URL Source: https://discord.com/developers/docs/reference

Markdown Content:
**Base URL**

```
https://discord.com/api
```

## API Versioning

Discord exposes different versions of our API[.](https://c.tenor.com/BuZl66EegkgAAAAC/westworld-dolores.gif) You should specify which version to use by including it in the request path like `https://discord.com/api/v{version_number}`. Omitting the version number from the route will route requests to the current default version (marked below). You can find the change log for the newest API version [here](https://docs.discord.com/developers/change-log).

**API Versions**

| Version | Status       | Default |
| ------- | ------------ | ------- |
| 10      | Available    |         |
| 9       | Available    |         |
| 8       | Deprecated   |         |
| 7       | Deprecated   |         |
| 6       | Deprecated   |         |
| 5       | Discontinued |         |
| 4       | Discontinued |         |
| 3       | Discontinued |         |

## Error Messages

Starting in API v8, we’ve improved error formatting in form error responses. The response will tell you which JSON key contains the error, the error code, and a human readable error message. We will be frequently adding new error messages, so a complete list of errors is not feasible and would be almost instantly out of date. Here are some examples instead:**Array Error**

```
{
  "code": 50035,
  "errors": {
    "activities": {
      "0": {
        "platform": {
          "_errors": [
            {
              "code": "BASE_TYPE_CHOICES",
              "message": "Value must be one of ('desktop', 'android', 'ios')."
            }
          ]
        },
        "type": {
          "_errors": [
            {
              "code": "BASE_TYPE_CHOICES",
              "message": "Value must be one of (0, 1, 2, 3, 4, 5)."
            }
          ]
        }
      }
    }
  },
  "message": "Invalid Form Body"
}
```

**Object Error**

```
{
  "code": 50035,
  "errors": {
    "access_token": {
      "_errors": [
        {
          "code": "BASE_TYPE_REQUIRED",
          "message": "This field is required"
        }
      ]
    }
  },
  "message": "Invalid Form Body"
}
```

**Request Error**

```
{
  "code": 50035,
  "message": "Invalid Form Body",
  "errors": {
    "_errors": [
      {
        "code": "APPLICATION_COMMAND_TOO_LARGE",
        "message": "Command exceeds maximum size (8000)"
      }
    ]
  }
}
```

## Authentication

Authenticating with the Discord API can be done in one of two ways:

1.  Using a bot token found on the Bot page within your app’s settings. For more information on bots see [bots vs user accounts](https://docs.discord.com/developers/topics/oauth2#bot-vs-user-accounts).
2.  Using an OAuth2 bearer token gained through the [OAuth2 API](https://docs.discord.com/developers/topics/oauth2).

For all authentication types, authentication is performed with the `Authorization` HTTP header in the format `Authorization: TOKEN_TYPE TOKEN`.**Example Bot Token Authorization Header**

```
Authorization: Bot <REDACTED_EXAMPLE_TOKEN>
```

**Example Bearer Token Authorization Header**

```
Authorization: Bearer CZhtkLDpNYXgPH9Ml6shqh2OwykChw
```

## Encryption

All HTTP-layer services and protocols (e.g. HTTP, WebSocket) within the Discord API are using TLS 1.2.

## Snowflakes

Discord utilizes Twitter’s [snowflake](https://github.com/twitter-archive/snowflake/tree/snowflake-2010) format for uniquely identifiable descriptors (IDs). These IDs are guaranteed to be unique across all of Discord, except in some unique scenarios in which child objects share their parent’s ID. Because Snowflake IDs are up to 64 bits in size (e.g. a uint64), they are always returned as strings in the HTTP API to prevent integer overflows in some languages. See [Gateway ETF/JSON](https://docs.discord.com/developers/events/gateway#encoding-and-compression) for more information regarding Gateway encoding.**Snowflake ID Broken Down in Binary**

```
111111111111111111111111111111111111111111 11111 11111 111111111111
64                                         22    17    12          0
```

**Snowflake ID Format Structure (Left to Right)**

| Field               | Bits     | Number of bits | Description                                                                  | Retrieval                           |
| ------------------- | -------- | -------------- | ---------------------------------------------------------------------------- | ----------------------------------- |
| Timestamp           | 63 to 22 | 42 bits        | Milliseconds since Discord Epoch, the first second of 2015 or 1420070400000. | `(snowflake >> 22) + 1420070400000` |
| Internal worker ID  | 21 to 17 | 5 bits         |                                                                              | `(snowflake & 0x3E0000) >> 17`      |
| Internal process ID | 16 to 12 | 5 bits         |                                                                              | `(snowflake & 0x1F000) >> 12`       |
| Increment           | 11 to 0  | 12 bits        | For every ID that is generated on that process, this number is incremented   | `snowflake & 0xFFF`                 |

### Convert Snowflake to DateTime

We typically use snowflake IDs in many of our API routes for pagination. The standardized pagination paradigm we utilize is one in which you can specify IDs `before` and `after` in combination with `limit` to retrieve a desired page of results. You will want to refer to the specific endpoint documentation for details.It is useful to note that snowflake IDs are just numbers with a timestamp, so when dealing with pagination where you want results from the beginning of time (in Discord Epoch, but `0` works here too) or before/after a specific time you can generate a snowflake ID for that time.**Generating a snowflake ID from a Timestamp Example**

```
(timestamp_ms - DISCORD_EPOCH) << 22
```

## ID Serialization

There are some cases in which our API and Gateway may return IDs in an unexpected format. Internally, Discord stores IDs as integer snowflakes. When we serialize IDs to JSON, we transform `bigints` into strings. Given that all Discord IDs are snowflakes, you should always expect a string.However, there are cases in which passing something to our API will instead return IDs serialized as an integer; this is the case when you send our API or Gateway a value in an `id` field that is not `bigint` size. For example, when requesting `GUILD_MEMBERS_CHUNK` from our gateway:

```
// Send
{
  op: 8,
  d: {
    guild_id: '308994132968210433',
    user_ids: [ '123123' ]
  }
}

// Receive
{
  t: 'GUILD_MEMBERS_CHUNK',
  s: 3,
  op: 0,
  d: {
    not_found: [ 123123 ],
    members: [],
    guild_id: '308994132968210433'
  }
}
```

You can see in this case that the sent `user_id` is not a `bigint`; therefore, when it is serialized back to JSON by Discord, it is not transformed into a string. This will never happen with IDs that come from Discord. But, this can happen if you send malformed data in your requests.

## ISO8601 Date/Time

Discord utilizes the [ISO8601 format](https://www.loc.gov/standards/datetime/iso-tc154-wg5_n0038_iso_wd_8601-1_2016-02-16.pdf) for most Date/Times returned in our models. This format is referred to as type `ISO8601` within tables in this documentation.

## Nullable and Optional Resource Fields

Resource fields that may contain a `null` value have types that are prefixed with a question mark. Resource fields that are optional have names that are suffixed with a question mark.**Example Nullable and Optional Fields**

| Field                        | Type    |
| ---------------------------- | ------- |
| optional_field?              | string  |
| nullable_field               | ?string |
| optional_and_nullable_field? | ?string |

## Consistency

Discord operates at a scale where true consistency is impossible. Because of this, lots of operations in our API and in-between our services are [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency). Due to this, client actions can never be serialized and may be executed in any order (if executed at all). Along with these constraints, events in Discord may:

- Never be sent to a client
- Be sent exactly one time to the client
- Be sent up to N times per client

Clients should operate on events and results from the API in as much of an idempotent behavior as possible.

## HTTP API

### User Agent

Clients using the HTTP API must provide a valid [User Agent](https://www.rfc-editor.org/rfc/rfc9110.html#section-10.1.5) which specifies information about the client library and version in the following format:**User Agent Example**

```
User-Agent: DiscordBot ($url, $versionNumber)
```

Clients may append more information and metadata to the end of this string as they wish.

### Content Type

Clients using the HTTP API must provide a valid `Content-Type` header, either `application/json`, `application/x-www-form-urlencoded`, or `multipart/form-data`, except where specified. Failing to do so will result in a `50035` “Invalid form body” error.

### Rate Limiting

The HTTP API implements a process for limiting and preventing excessive requests in accordance with [RFC 6585](https://tools.ietf.org/html/rfc6585#section-4). API users that regularly hit and ignore rate limits will have their API keys revoked, and be blocked from the platform. For more information on rate limiting of requests, please see the [Rate Limits](https://docs.discord.com/developers/topics/rate-limits) section.

### Boolean Query Strings

Certain endpoints in the API are documented to accept booleans for their query string parameters. While there is no standard system for boolean representation in query string parameters, Discord represents such cases using `True`, `true`, or `1` for true and `False`, `false` or `0` for false.

### Array Query Strings

Certain endpoints in the API are documented to accept arrays for their query string parameters. Unless otherwise specified, Discord represents such cases using multiple instances of the same query string parameter. For example, `?id=123&id=456` for `["123", "456"]`.

## Gateway (WebSocket) API

Discord’s Gateway API is used for maintaining persistent, stateful websocket connections between your client and our servers. These connections are used for sending and receiving real-time events your client can use to track and update local state. The Gateway API uses secure websocket connections as specified in [RFC 6455](https://tools.ietf.org/html/rfc6455). For information on opening Gateway connections, please see the [Gateway API](https://docs.discord.com/developers/events/gateway#connections) section.

## Message Formatting

Discord utilizes a subset of markdown for rendering message content on its clients, while also adding some custom functionality to enable things like mentioning users and channels. This functionality uses the following formats:

**Formats**

| Type                                | Structure                                | Example                               |
| ----------------------------------- | ---------------------------------------- | ------------------------------------- |
| User                                | `<@USER_ID>`                             | `<@80351110224678912>`                |
| User \*                             | `<@!USER_ID>`                            | `<@!80351110224678912>`               |
| Channel                             | `<#CHANNEL_ID>`                          | `<#103735883630395392>`               |
| Role                                | `<@&ROLE_ID>`                            | `<@&165511591545143296>`              |
| Slash command                       | `</NAME:COMMAND_ID>`                     | `</airhorn:816437322781949972>`       |
| Slash command with subcommand       | `</NAME SUBCOMMAND:ID>`                  | `</foo bar:123456789012345678>`       |
| Slash command with subcommand group | `</NAME SUBCOMMAND_GROUP SUBCOMMAND:ID>` | `</foo group bar:123456789012345678>` |
| Standard emoji                      | Unicode characters                       | 🪴                                    |
| Custom emoji                        | `<:NAME:ID>`                             | `<:mmLol:216154654256398347>`         |
| Animated custom emoji               | `<a:NAME:ID>`                            | `<a:b1nzy:392938283556143104>`        |
| Unix timestamp                      | `<t:TIMESTAMP>`                          | `<t:1618953630>`                      |
| Styled unix timestamp               | `<t:TIMESTAMP:STYLE>`                    | `<t:1618953630:d>`                    |
| Guild navigation                    | `<id:TYPE>`                              | See below                             |

Using the markdown for users or roles will mention the target(s), and notify them depending on the sender’s permissions as well as the value of the `allowed_mentions` field when creating a message. Standard emoji are currently rendered using [Twemoji](https://github.com/jdecked/twemoji) for Desktop and Android while iOS devices use Apple’s native emoji set.Timestamps are expressed in **seconds** and display the given timestamp in the user’s timezone and locale.\* User mentions with an exclamation point are deprecated and should be handled like any other user mention.

**Timestamp Styles**

| Style | Example Output                   | Description             |
| ----- | -------------------------------- | ----------------------- |
| t     | 16:20                            | Short Time              |
| T     | 16:20:30                         | Medium Time             |
| d     | 20/04/2021                       | Short Date              |
| D     | April 20, 2021                   | Long Date               |
| f \*  | April 20, 2021 at 16:20          | Long Date, Short Time   |
| F     | Tuesday, April 20, 2021 at 16:20 | Full Date, Short Time   |
| s     | 20/04/2021, 16:20                | Short Date, Short Time  |
| S     | 20/04/2021, 16:20:30             | Short Date, Medium Time |
| R     | 4 years ago                      | Relative Time           |

\*default**Guild Navigation Types**Guild navigation types link to the corresponding resource in the current server.

| Full Syntax            | Linked Resource                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `<id:customize>`       | Channel & Roles tab with [Onboarding prompts](https://docs.discord.com/developers/resources/guild#guild-onboarding-object) |
| `<id:browse>`          | Browse Channels tab                                                                                                        |
| `<id:guide>`           | [Server Guide](https://support.discord.com/hc/en-us/articles/13497665141655) tab                                           |
| `<id:linked-roles>`    | [Linked Roles](https://support.discord.com/hc/en-us/articles/10388356626711) tab                                           |
| `<id:linked-roles:id>` | Specific linked role, opening the connection modal on click (the second `id` is the role id)                               |

## Image Formatting

**Image Base URL**

```
https://cdn.discordapp.com/
```

Discord uses ids and hashes to render images in the client. These hashes can be retrieved through various API requests, like [Get User](https://docs.discord.com/developers/resources/user#get-user). Below are the formats, size limitations, and CDN endpoints for images in Discord. The returned format can be changed by changing the [extension name](https://docs.discord.com/developers/reference#image-formatting-image-formats) at the end of the URL. The returned size can be changed by appending a querystring of `?size=desired_size` to the URL. Image size can be any power of two between 16 and 4096.

**Image Formats**

| Name   | Extension   |
| ------ | ----------- |
| JPEG   | .jpg, .jpeg |
| PNG    | .png        |
| WebP   | .webp       |
| GIF    | .gif        |
| Lottie | .json       |

**CDN Endpoints**

| Type                        | Path                                                                                                                                                                                                                                                                                                                                                                                                        | Supports             |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| Custom Emoji                | emojis/[emoji_id](https://docs.discord.com/developers/resources/emoji#emoji-object).png **\***                                                                                                                                                                                                                                                                                                              | PNG, JPEG, WebP, GIF |
| Guild Icon                  | icons/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/[guild_icon](https://docs.discord.com/developers/resources/guild#guild-object).png \*                                                                                                                                                                                                                                    | PNG, JPEG, WebP, GIF |
| Guild Splash                | splashes/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/[guild_splash](https://docs.discord.com/developers/resources/guild#guild-object).png                                                                                                                                                                                                                                  | PNG, JPEG, WebP      |
| Guild Discovery Splash      | discovery-splashes/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/[guild_discovery_splash](https://docs.discord.com/developers/resources/guild#guild-object).png                                                                                                                                                                                                              | PNG, JPEG, WebP      |
| Guild Banner                | banners/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/[guild_banner](https://docs.discord.com/developers/resources/guild#guild-object).png \*                                                                                                                                                                                                                                | PNG, JPEG, WebP, GIF |
| User Banner                 | banners/[user_id](https://docs.discord.com/developers/resources/user#user-object)/[user_banner](https://docs.discord.com/developers/resources/user#user-object).png \*                                                                                                                                                                                                                                      | PNG, JPEG, WebP, GIF |
| Default User Avatar         | embed/avatars/[index](https://docs.discord.com/developers/resources/user#user-object).png ** \***                                                                                                                                                                                                                                                                                                           | PNG                  |
| User Avatar                 | avatars/[user_id](https://docs.discord.com/developers/resources/user#user-object)/[user_avatar](https://docs.discord.com/developers/resources/user#user-object).png \*                                                                                                                                                                                                                                      | PNG, JPEG, WebP, GIF |
| Guild Member Avatar         | guilds/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/users/[user_id](https://docs.discord.com/developers/resources/user#user-object)/avatars/[member_avatar](https://docs.discord.com/developers/resources/guild#guild-member-object).png \*                                                                                                                                 | PNG, JPEG, WebP, GIF |
| Avatar Decoration           | avatar-decoration-presets/[avatar_decoration_data_asset](https://docs.discord.com/developers/resources/user#avatar-decoration-data-object).png                                                                                                                                                                                                                                                              | PNG                  |
| Application Icon            | app-icons/[application_id](https://docs.discord.com/developers/resources/application#application-object)/[icon](https://docs.discord.com/developers/resources/application#application-object).png                                                                                                                                                                                                           | PNG, JPEG, WebP      |
| Application Cover           | app-icons/[application_id](https://docs.discord.com/developers/resources/application#application-object)/[cover_image](https://docs.discord.com/developers/resources/application#application-object).png                                                                                                                                                                                                    | PNG, JPEG, WebP      |
| Application Asset           | app-assets/[application_id](https://docs.discord.com/developers/resources/application#application-object)/[asset_id](https://docs.discord.com/developers/events/gateway-events#activity-object-activity-assets).png                                                                                                                                                                                         | PNG, JPEG, WebP      |
| Achievement Icon            | app-assets/[application_id](https://docs.discord.com/developers/resources/application#application-object)/achievements/[achievement_id](https://github.com/discord/discord-api-docs/blob/legacy-gamesdk/docs/game_sdk/Achievements.md#user-achievement-struct)/icons/[icon_hash](https://github.com/discord/discord-api-docs/blob/legacy-gamesdk/docs/game_sdk/Achievements.md#user-achievement-struct).png | PNG, JPEG, WebP      |
| Store Page Asset            | app-assets/[application_id](https://docs.discord.com/developers/resources/application#application-object)/store/asset_id                                                                                                                                                                                                                                                                                    | PNG, JPEG, WebP      |
| Sticker Pack Banner         | app-assets/710982414301790216/store/[sticker_pack_banner_asset_id](https://docs.discord.com/developers/resources/sticker#sticker-pack-object).png                                                                                                                                                                                                                                                           | PNG, JPEG, WebP      |
| Team Icon                   | team-icons/[team_id](https://docs.discord.com/developers/topics/teams#data-models-team-object)/[team_icon](https://docs.discord.com/developers/topics/teams#data-models-team-object).png                                                                                                                                                                                                                    | PNG, JPEG, WebP      |
| Sticker                     | stickers/[sticker_id](https://docs.discord.com/developers/resources/sticker#sticker-object).png **\* \*\***                                                                                                                                                                                                                                                                                                 | PNG, Lottie, GIF     |
| Role Icon                   | role-icons/[role_id](https://docs.discord.com/developers/topics/permissions#role-object)/[role_icon](https://docs.discord.com/developers/topics/permissions#role-object).png                                                                                                                                                                                                                                | PNG, JPEG, WebP      |
| Guild Scheduled Event Cover | guild-events/[scheduled_event_id](https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object)/[scheduled_event_cover_image](https://docs.discord.com/developers/resources/guild-scheduled-event#guild-scheduled-event-object).png                                                                                                                                     | PNG, JPEG, WebP      |
| Guild Member Banner         | guilds/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/users/[user_id](https://docs.discord.com/developers/resources/user#user-object)/banners/[member_banner](https://docs.discord.com/developers/resources/guild#guild-member-object).png \*                                                                                                                                 | PNG, JPEG, WebP, GIF |
| Guild Tag Badge             | guild-tag-badges/[guild_id](https://docs.discord.com/developers/resources/guild#guild-object)/[badge_hash](https://docs.discord.com/developers/resources/user#user-object-user-primary-guild).png                                                                                                                                                                                                           | PNG, JPEG, WebP      |

- In the case of endpoints that support GIFs, the hash will begin with `a_` if it is available in an animated format (example: `a_1269e74af4df7417b13759eae50c83dc`). These images can be retrieved as animated WebP using the `.webp` file extension and `?animated=true` querystring parameter.** In the case of the Default User Avatar endpoint, the value for `index` depends on whether the user is [migrated to the new username system](https://docs.discord.com/developers/change-log#unique-usernames-on-discord). For users on the new username system, `index` will be `(user_id >> 22) % 6`. For users on the legacy username system, `index` will be `discriminator % 5`.\*** In the case of the Default User Avatar and Sticker endpoints, the size of images returned is constant with the “size” querystring parameter being ignored.\***\* In the case of the Sticker endpoint, the sticker will be available as PNG if its [`format_type`](https://docs.discord.com/developers/resources/sticker#sticker-object) is `PNG` or `APNG`, GIF if its `format_type` is `GIF`, and as [Lottie](https://airbnb.io/lottie/#/) if its `format_type` is `LOTTIE`.\*\*\*** For Custom Emoji, we highly recommend requesting emojis as WebP for maximum performance and compatibility. Emojis can be uploaded as JPEG, PNG, GIF, WebP, and AVIF formats. WebP and AVIF formats must be requested as WebP since they don’t convert well to other formats. The Discord client uses WebP for all emojis displayed in-app. See the [Emoji Resource](https://docs.discord.com/developers/resources/emoji) page for more details.

## Image Data

Image data is a [Data URI scheme](https://en.wikipedia.org/wiki/Data_URI_scheme) that supports JPG, GIF, and PNG formats. An example Data URI format is:

```
data:image/jpeg;base64,BASE64_ENCODED_JPEG_IMAGE_DATA
```

Ensure you use the proper content type (`image/jpeg`, `image/png`, `image/gif`) that matches the image data being provided.

### **Signed Attachment CDN URLs**

Attachments uploaded to Discord’s CDN (like user and bot-uploaded images) have signed URLs with a preset expiry time. Discord automatically refreshes attachment CDN URLs that appear within the client, so when your app receives a payload with a signed URL (like when you [fetch a message](https://docs.discord.com/developers/resources/message#get-channel-message)), it will be valid.When passing CDN URLs into API fields, like [`url` in an embed image object](https://docs.discord.com/developers/resources/message#embed-object-embed-image-structure) and [`avatar_url` for webhooks](https://docs.discord.com/developers/resources/webhook#execute-webhook-jsonform-params), your app can pass the CDN URL without any parameters as the value and Discord will automatically render and refresh the URL.The [standard CDN endpoints](https://docs.discord.com/developers/reference#image-formatting-cdn-endpoints) listed above are not signed, so they will not expire.

###### Example Attachment CDN URL

```
https://cdn.discordapp.com/attachments/1012345678900020080/1234567891233211234/my_image.png?ex=65d903de&is=65c68ede&hm=2481f30dd67f503f54d020ae3b5533b9987fae4e55f2b4e3926e08a3fa3ee24f&
```

###### Attachment CDN URL Parameters

| Parameter | Description                                                     |
| --------- | --------------------------------------------------------------- |
| ex        | Hex timestamp indicating when an attachment CDN URL will expire |
| is        | Hex timestamp indicating when the URL was issued                |
| hm        | Unique signature that remains valid until the URL’s expiration  |

## Uploading Files

Some endpoints support file attachments, indicated by the `files[n]` parameter. To add file(s), the standard `application/json` body must be replaced by a `multipart/form-data` body. The JSON message body can optionally be provided using the `payload_json` parameter.All `files[n]` parameters must include a valid `Content-Disposition` subpart header with a `filename` and unique `name` parameter. Each file parameter must be uniquely named in the format `files[n]` such as `files[0]`, `files[1]`, or `files[42]`. The suffixed index `n` is the snowflake placeholder that can be used in the `attachments` field, which can be passed to the `payload_json` parameter (or [Callback Data Payloads](https://docs.discord.com/developers/interactions/receiving-and-responding#interaction-response-object-interaction-callback-data-structure)).Images can also be referenced in embeds using the `attachment://filename` URL. An example payload is provided below.

### Editing Message Attachments

The `attachments` JSON parameter includes all files that will be appended to the message, including new files and their respective snowflake placeholders (referenced above). When making a `PATCH` request, only files listed in the `attachments` parameter will be appended to the message. Any previously-added files that aren’t included will be removed.**Example Request Bodies (multipart/form-data)**Note that these examples are small sections of an HTTP request to demonstrate behavior of this endpoint - client libraries will set their own form boundaries (`boundary` is just an example). For more information, refer to the [multipart/form-data spec](https://tools.ietf.org/html/rfc7578#section-4).This example demonstrates usage of the endpoint without `payload_json`.

```
--boundary
Content-Disposition: form-data; name="content"

Hello, World!
--boundary
Content-Disposition: form-data; name="tts"

true
--boundary--
```

This example demonstrates usage of the endpoint with `payload_json` and all content fields (`content`, `embeds`, `files[n]`) set.

```
--boundary
Content-Disposition: form-data; name="payload_json"
Content-Type: application/json

{
  "content": "Hello, World!",
  "embeds": [{
    "title": "Hello, Embed!",
    "description": "This is an embedded message.",
    "thumbnail": {
      "url": "attachment://myfilename.png"
    },
    "image": {
      "url": "attachment://mygif.gif"
    }
  }],
  "message_reference": {
    "message_id": "233648473390448641"
  },
  "attachments": [{
      "id": 0,
      "description": "Image of a cute little cat",
      "filename": "myfilename.png"
  }, {
      "id": 1,
      "description": "Rickroll gif",
      "filename": "mygif.gif"
  }]
}
--boundary
Content-Disposition: form-data; name="files[0]"; filename="myfilename.png"
Content-Type: image/png

[image bytes]
--boundary
Content-Disposition: form-data; name="files[1]"; filename="mygif.gif"
Content-Type: image/gif

[image bytes]
--boundary--
```

**Using Attachments within Embeds**You can upload attachments when creating a message and use those attachments within your embed. To do this, you will want to upload files as part of your `multipart/form-data` body. Make sure that you’re uploading files which contain a filename, as you will need to reference it in your payload.

Within an embed object, you can set an image to use an attachment as its URL with the attachment scheme syntax: `attachment://filename.png`For example:

```
{
  "embeds": [{
    "image": {
      "url": "attachment://screenshot.png"
    }
  }]
}
```

## Locales

| Locale | Language Name         | Native Name         |
| ------ | --------------------- | ------------------- |
| id     | Indonesian            | Bahasa Indonesia    |
| da     | Danish                | Dansk               |
| de     | German                | Deutsch             |
| en-GB  | English, UK           | English, UK         |
| en-US  | English, US           | English, US         |
| es-ES  | Spanish               | Español             |
| es-419 | Spanish, LATAM        | Español, LATAM      |
| fr     | French                | Français            |
| hr     | Croatian              | Hrvatski            |
| it     | Italian               | Italiano            |
| lt     | Lithuanian            | Lietuviškai         |
| hu     | Hungarian             | Magyar              |
| nl     | Dutch                 | Nederlands          |
| no     | Norwegian             | Norsk               |
| pl     | Polish                | Polski              |
| pt-BR  | Portuguese, Brazilian | Português do Brasil |
| ro     | Romanian, Romania     | Română              |
| fi     | Finnish               | Suomi               |
| sv-SE  | Swedish               | Svenska             |
| vi     | Vietnamese            | Tiếng Việt          |
| tr     | Turkish               | Türkçe              |
| cs     | Czech                 | Čeština             |
| el     | Greek                 | Ελληνικά            |
| bg     | Bulgarian             | български           |
| ru     | Russian               | Pусский             |
| uk     | Ukrainian             | Українська          |
| hi     | Hindi                 | हिन्दी              |
| th     | Thai                  | ไทย                 |
| zh-CN  | Chinese, China        | 中文                |
| ja     | Japanese              | 日本語              |
| zh-TW  | Chinese, Taiwan       | 繁體中文            |
| ko     | Korean                | 한국어              |
