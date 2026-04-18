---
tags:
  - library
title: "Telegram APIs"
url: "https://core.telegram.org/api"
company: [personal]
topics: []
created: 2025-07-18
source_type: raindrop
raindrop_id: 1257113855
source_domain: "core.telegram.org"
source_type_raindrop: link
collection: "Dev Tools & CLI"
collection_id: 69292902
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

We offer three kinds of APIs for developers. The Bot API allows you to easily create programs that use Telegram messages…

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Telegram APIs

URL Source: https://core.telegram.org/api

Markdown Content:
# Telegram APIs

*   [Twitter](https://twitter.com/telegram)

*   [Home](https://telegram.org/)
*   [FAQ](https://telegram.org/faq)
*   [Apps](https://telegram.org/apps)
*   [API](https://core.telegram.org/api)
*   [Protocol](https://core.telegram.org/mtproto)
*   [Schema](https://core.telegram.org/schema)

# Telegram APIs

We offer three kinds of APIs for developers. The [**Bot API**](https://core.telegram.org/api#bot-api) allows you to easily create programs that use Telegram messages for an interface. The [**Telegram API and TDLib**](https://core.telegram.org/api#tdlib-build-your-own-telegram) allow you to build your own customized Telegram clients. You are welcome to use both APIs free of charge. Lastly, the [**Gateway API**](https://core.telegram.org/api#gateway-api) allows any business, app or website to send verification codes through Telegram instead of traditional SMS.

You can also add [**Telegram Widgets**](https://core.telegram.org/widgets) to your website.

Designers are welcome to create [**Animated Stickers and Emoji**](https://core.telegram.org/stickers#animated-stickers-and-emoji) or [**Custom Themes**](https://core.telegram.org/themes) for Telegram.

* * *

### [](https://core.telegram.org/api#bot-api)Bot API

[![Image 1](https://core.telegram.org/file/811140934/1/tbDSLHSaijc/fdcc7b6d5fb3354adf)](https://core.telegram.org/file/811140327/1/zlN4goPTupk/9ff2f2f01c4bd1b013)

This API allows you to connect bots to our system. [**Telegram Bots**](https://core.telegram.org/bots) are special accounts that do not require an additional phone number to set up. These accounts serve as an interface for code running somewhere on your server.

To use this, you don't need to know anything about how our MTProto encryption protocol works — our intermediary server will handle all encryption and communication with the Telegram API for you. You communicate with this server via a simple HTTPS-interface that offers a simplified version of the Telegram API.

> [**Learn more about the Bot API here »**](https://core.telegram.org/bots)

Bot developers can also make use of our [**Payments API**](https://core.telegram.org/bots/payments) to accept **payments** from Telegram users around the world.

* * *

### [](https://core.telegram.org/api#tdlib-build-your-own-telegram)TDLib – build your own Telegram

Even if you're looking for maximum customization, you don't have to create your app from scratch. Try our [**Telegram Database Library**](https://core.telegram.org/tdlib) (or simply TDLib), a tool for third-party developers that makes it easy to build fast, secure and feature-rich Telegram apps.

TDLib takes care of all **network implementation** details, **encryption** and **local data storage**, so that you can dedicate more time to design, responsive interfaces and beautiful animations.

TDLib supports all Telegram features and makes developing Telegram apps a breeze on any platform. It can be used on Android, iOS, Windows, macOS, Linux and virtually any other system. The library is open source and compatible with virtually **any programming language**.

> [**Learn more about TDLib here »**](https://core.telegram.org/tdlib)

* * *

## [](https://core.telegram.org/api#gateway-api)Gateway API

The Telegram Gateway API allows any business, app or website to send authorization codes through Telegram instead of traditional SMS – offering a powerful and convenient way to **lower costs** while increasing the **security** and **delivery speed** of your codes to Telegram’s 1 billion monthly active users. Users will **instantly receive** messages with codes in a special chat inside Telegram.

> [**Telegram's Gateway API is completely free to test. Learn more here »**](https://core.telegram.org/gateway)

* * *

### [](https://core.telegram.org/api#telegram-api)Telegram API

This API allows you to build your own customized Telegram clients. It is 100% open for all developers who wish to create Telegram applications on our platform. Feel free to study the open [source code](https://telegram.org/apps#source-code) of existing Telegram applications for examples of how things work here. Don't forget to [register](https://core.telegram.org/api/obtaining_api_id) your application in our system.

*   [Getting Started](https://core.telegram.org/api#getting-started)
*   [Security](https://core.telegram.org/api#security)
*   [Optimization](https://core.telegram.org/api#optimization)
*   [API methods](https://core.telegram.org/api#api-methods)

### [](https://core.telegram.org/api#getting-started)Getting started

#### [](https://core.telegram.org/api#creating-an-application)[Creating an application](https://core.telegram.org/api/obtaining_api_id)

How to get your application identifier and create a new Telegram app.

#### [](https://core.telegram.org/api#user-authorization)[User authorization](https://core.telegram.org/api/auth)

How to register a user's phone to start using the API.

#### [](https://core.telegram.org/api#two-factor-authentication)[Two-factor authentication](https://core.telegram.org/api/srp)

How to login to a user's account if they have enabled 2FA, how to change password.

#### [](https://core.telegram.org/api#qr-code-login)[QR code login](https://core.telegram.org/api/qr-login)

[QR code](https://en.wikipedia.org/wiki/QR_code) login flow

#### [](https://core.telegram.org/api#error-handling)[Error handling](https://core.telegram.org/api/errors)

How to handle API return errors correctly.

#### [](https://core.telegram.org/api#handling-different-data-centers)[Handling different data centers](https://core.telegram.org/api/datacenter)

How to connect to the closest DC access point for faster interaction with the API, and things to watch out for when developing a client.

#### [](https://core.telegram.org/api#handling-updates)[Handling updates](https://core.telegram.org/api/updates)

How to subscribe to updates and handle them properly.

#### [](https://core.telegram.org/api#handling-push-notifications)[Handling PUSH-notifications](https://core.telegram.org/api/push-updates)

How to subscribe and handle them properly.

#### [](https://core.telegram.org/api#channels-supergroups-gigagroups-and-basic-groups)[Channels, supergroups, gigagroups and basic groups](https://core.telegram.org/api/channel)

How to handle channels, supergroups, gigagroups, basic groups, and what's the difference between them.

#### [](https://core.telegram.org/api#forums)[Forums](https://core.telegram.org/api/forum)

Telegram allows creating forums with multiple distinct topics.

#### [](https://core.telegram.org/api#direct-messages-to-channels)[Direct messages to channels](https://core.telegram.org/api/monoforum)

Telegram supports direct messages to channels, which can also be used to suggest (even paid) channel posts.

#### [](https://core.telegram.org/api#channel-statistics)[Channel statistics](https://core.telegram.org/api/stats)

Telegram offers detailed channel statistics for channels and supergroups.

#### [](https://core.telegram.org/api#calling-methods)[Calling methods](https://core.telegram.org/api/invoking)

Additional options for calling methods.

#### [](https://core.telegram.org/api#uploading-and-downloading-files)[Uploading and Downloading Files](https://core.telegram.org/api/files)

How to transfer large data batches correctly.

#### [](https://core.telegram.org/api#pagination)[Pagination](https://core.telegram.org/api/offsets)

How to fetch results from large lists of objects.

#### [](https://core.telegram.org/api#client-configuration)[Client configuration](https://core.telegram.org/api/config)

The MTProto API has multiple client configuration parameters that can be fetched with the appropriate methods.

### [](https://core.telegram.org/api#security)Security

#### [](https://core.telegram.org/api#secret-chats-end-to-end-encryption)[Secret chats, end-to-end encryption](https://core.telegram.org/api/end-to-end)

End-to-end-encrypted messaging.

#### [](https://core.telegram.org/api#security-guidelines)[Security guidelines](https://core.telegram.org/mtproto/security_guidelines)

Important checks required in your client application.

#### [](https://core.telegram.org/api#perfect-forward-secrecy)[Perfect Forward Secrecy](https://core.telegram.org/api/pfs)

Binding temporary authorization key to permanent ones.

#### [](https://core.telegram.org/api#end-to-end-encryption-in-voice-and-video-calls)[End-to-End Encryption in Voice and Video Calls](https://core.telegram.org/api/end-to-end/video-calls)

End-to-end-encrypted calls.

### [](https://core.telegram.org/api#optimization)Optimization

#### [](https://core.telegram.org/api#client-optimization)[Client optimization](https://core.telegram.org/api/optimisation)

Ways to boost API interactions.

### [](https://core.telegram.org/api#api-methods)API methods

#### [](https://core.telegram.org/api#available-method-list)[Available method list](https://core.telegram.org/methods)

A list of available high-level methods.

#### [](https://core.telegram.org/api#api-tl-schema-as-json)[API TL-schema](https://core.telegram.org/schema), [as JSON](https://core.telegram.org/schema/json)

Text and JSON-presentation of types and methods used in API.

#### [](https://core.telegram.org/api#layer-changelog)[Layer changelog](https://core.telegram.org/api/layers)

A detailed changelog of available schema versions.

### [](https://core.telegram.org/api#other-articles)Other articles

#### [](https://core.telegram.org/api#working-with-bots-using-the-mtproto-api)[Working with bots, using the MTProto API](https://core.telegram.org/api/bots)

How to work with bots using the MTProto API.

#### [](https://core.telegram.org/api#bot-api-dialog-ids)[Bot API dialog IDs](https://core.telegram.org/api/bots/ids)

A bot API dialog ID is a single, unique 64-bit peer ID sequence derived from the user, chat, channel and secret chat ID sequences, maintaining uniqueness across all of them.

[This page](https://core.telegram.org/api/bots/ids) specifies how to convert MTProto peer IDs to bot API dialog IDs and vice versa.

#### [](https://core.telegram.org/api#commands)[Commands](https://core.telegram.org/api/bots/commands)

[Bots](https://core.telegram.org/bots) offer a set of commands that can be used by users in private, or in a chat.

#### [](https://core.telegram.org/api#buttons)[Buttons](https://core.telegram.org/api/bots/buttons)

Users can interact with your bot via **buttons** or even **inline buttons**, straight from inline **messages** in **any** chat.

#### [](https://core.telegram.org/api#menu-button)[Menu button](https://core.telegram.org/api/bots/menu)

Bots can choose the behavior of the menu button shown next to the text input field.

#### [](https://core.telegram.org/api#inline-queries)[Inline queries](https://core.telegram.org/api/bots/inline)

Users can interact with your bot via **inline queries**, straight from the **text input field** in **any** chat.

#### [](https://core.telegram.org/api#games)[Games](https://core.telegram.org/api/bots/games)

Bots can offer users HTML5 games to play solo or to compete against each other in groups and one-on-one chats; how to work with games in the MTProto API.

#### [](https://core.telegram.org/api#mini-apps)[Mini apps](https://core.telegram.org/api/bots/webapps)

Bots can offer users interactive [HTML5 mini apps](https://core.telegram.org/bots/webapps) to completely replace **any website**.

#### [](https://core.telegram.org/api#affiliate-programs)[Affiliate programs](https://core.telegram.org/api/bots/referrals)

Developers can open affiliate programs for their [mini app](https://core.telegram.org/api/bots/webapps) – allowing **content creators**, other **mini app developers** and **any Telegram user** to promote it and earn commissions on purchases made by people they referred.

#### [](https://core.telegram.org/api#attachment-menu)[Attachment menu](https://core.telegram.org/api/bots/attach)

Bots can install attachment menu entries, offering conveniently accessible, versatile mini apps.

#### [](https://core.telegram.org/api#stories)[Stories](https://core.telegram.org/api/stories)

Telegram users and channels can easily post and view [stories](https://telegram.org/blog/stories) through the API.

#### [](https://core.telegram.org/api#similar-channels-and-bots)[Similar channels and bots](https://core.telegram.org/api/recommend)

The API offers a method to obtain a list of similarly themed public channels and bots, selected based on similarities in their **subscriber bases**.

#### [](https://core.telegram.org/api#accent-colors)[Accent colors](https://core.telegram.org/api/colors)

Telegram users and channels can change the accent color and background pattern of their profile page and their messages!

#### [](https://core.telegram.org/api#privacy-settings)[Privacy settings](https://core.telegram.org/api/privacy)

Telegram allows users to specify granular privacy settings, choosing which users can or can't interact with them in certain ways.

#### [](https://core.telegram.org/api#search-amp-filters)[Search & filters](https://core.telegram.org/api/search)

Telegram allows applying detailed message filters while looking for messages in chats. This allows the server to filter messages based on a text query, and even on their type, and this feature is often used by graphical clients to implement features like the chat gallery, chat profile pictures and more.

#### [](https://core.telegram.org/api#polls)[Polls](https://core.telegram.org/api/poll)

Telegram allows sending polls and quizzes, that can be voted on by thousands, if not millions of users in chats and channels.

#### [](https://core.telegram.org/api#checklists)[Checklists](https://core.telegram.org/api/todo)

Premium users can now create collaborative checklists in any chat to track tasks and coordinate teams — or manage shopping and to-do lists.

#### [](https://core.telegram.org/api#reactions)[Reactions](https://core.telegram.org/api/reactions)

Telegram allows users to react on any message using specific emojis, triggering cute lottie animations.

#### [](https://core.telegram.org/api#animated-message-effects)[Animated message effects](https://core.telegram.org/api/effects)

Telegram allows adding spectacular animated effects to messages you send.

#### [](https://core.telegram.org/api#emoji-categories)[Emoji categories](https://core.telegram.org/api/emoji-categories)

Sticker, custom emoji and GIF selection UIs should offer a list of categories to quickly filter results by a (list of) emojis, or by some other criteria.

#### [](https://core.telegram.org/api#emoji-status)[Emoji status](https://core.telegram.org/api/emoji-status)

Telegram allows users to set an emoticon or a [custom emoji](https://core.telegram.org/api/custom-emoji) as status, to show next to their name in chats and profiles.

#### [](https://core.telegram.org/api#invite-links-and-join-requests)[Invite links and join requests](https://core.telegram.org/api/invites)

Channels, basic groups and supergroups may have a public username or a private invite link: private invite links may be further enhanced with per-user join requests.

#### [](https://core.telegram.org/api#admin-banned-and-default-rights-for-channels-supergroups-and-groups)[Admin, banned and default rights for channels, supergroups and groups](https://core.telegram.org/api/rights)

How to handle admin permissions, granular bans and global permissions in channels, groups and supergroups.

#### [](https://core.telegram.org/api#discussion-groups)[Discussion groups](https://core.telegram.org/api/discussion)

[Groups](https://core.telegram.org/api/channel) can be associated to a [channel](https://core.telegram.org/api/channel) as a [discussion group](https://telegram.org/blog/privacy-discussions-web-bots), to allow users to discuss about posts.

#### [](https://core.telegram.org/api#channel-comments-and-message-threads)[Channel comments and message threads](https://core.telegram.org/api/threads)

Telegram allows commenting on a [channel post](https://core.telegram.org/api/channel) or on a generic [group message](https://core.telegram.org/api/channel), thanks to message threads.

#### [](https://core.telegram.org/api#admin-log)[Admin log](https://core.telegram.org/api/recent-actions)

Both supergroups and channels offer a so-called [admin log](https://telegram.org/blog/admin-revolution), a log of recent relevant supergroup and channel actions, like the modification of group/channel settings or information on behalf of an admin, user kicks and bans, and more.

#### [](https://core.telegram.org/api#pinned-messages)[Pinned messages](https://core.telegram.org/api/pin)

Telegram allows pinning multiple messages on top of a specific chat.

#### [](https://core.telegram.org/api#mentions)[Mentions](https://core.telegram.org/api/mentions)

Telegram allows mentioning other users in case of urgent duckling matters, and quickly navigating to those mentions in order to read them as swiftly as possible.

#### [](https://core.telegram.org/api#scheduled-messages)[Scheduled messages](https://core.telegram.org/api/scheduled-messages)

Telegram allows scheduling messages.

#### [](https://core.telegram.org/api#live-geolocations)[Live geolocations](https://core.telegram.org/api/live-location)

Telegram allows sending the live geolocation of a user in a chat, optionally setting a proximity alert.

### [](https://core.telegram.org/api#peer-database)[Peer database](https://core.telegram.org/api/peers)

How to work with peer information in the API.

#### [](https://core.telegram.org/api#min-constructors)[Min constructors](https://core.telegram.org/api/min)

Sometimes, [user](https://core.telegram.org/constructor/user) and [channel](https://core.telegram.org/constructor/channel) constructors met in group chat updates may not contain full info about the user: how to handle such constructors.

#### [](https://core.telegram.org/api#account-deletion)[Account deletion](https://core.telegram.org/api/account-deletion)

How to delete a Telegram account.

#### [](https://core.telegram.org/api#imported-messages)[Imported messages](https://core.telegram.org/api/import)

Telegram allows importing messages and media from foreign chat apps.

#### [](https://core.telegram.org/api#telegram-passport)[Telegram Passport](https://core.telegram.org/api/passport)

How to work with [Telegram Passport](https://core.telegram.org/api/passport) directly using the MTProto API.

#### [](https://core.telegram.org/api#telegram-payments)[Telegram Payments](https://core.telegram.org/api/payments)

How to work with Telegram Payments directly using the MTProto API.

#### [](https://core.telegram.org/api#third-party-verification)[Third-party verification](https://core.telegram.org/api/bots/verification)

To further improve transparency on Telegram, **official third-party services** are able to assign **extra verification icons** to user accounts and chats — in order to **prevent scams** and **reduce misinformation**.

#### [](https://core.telegram.org/api#styled-text-with-message-entities)[Styled text with message entities](https://core.telegram.org/api/entities)

How to create styled text with message entities

#### [](https://core.telegram.org/api#working-with-gifs)[Working with GIFs](https://core.telegram.org/api/gifs)

Telegram clients support displaying GIFs.

#### [](https://core.telegram.org/api#working-with-stickers)[Working with stickers](https://core.telegram.org/api/stickers)

Telegram clients support displaying animated, static and video stickers.

#### [](https://core.telegram.org/api#working-with-custom-emojis)[Working with custom emojis](https://core.telegram.org/api/custom-emoji)

Telegram allows including custom animated, static and video emojis directly inside of messages.

#### [](https://core.telegram.org/api#working-with-animated-emojis)[Working with animated emojis](https://core.telegram.org/api/animated-emojis)

Graphical telegram clients should transform emojis into their respective animated version.

#### [](https://core.telegram.org/api#working-with-animated-dice)[Working with animated dice](https://core.telegram.org/api/dice)

Telegram supports sending [animated dice](https://telegram.org/blog/folders#and-one-more-thing) emojis.

#### [](https://core.telegram.org/api#message-drafts)[Message drafts](https://core.telegram.org/api/drafts)

How to handle message drafts

#### [](https://core.telegram.org/api#folders)[Folders](https://core.telegram.org/api/folders)

Working with folders

#### [](https://core.telegram.org/api#top-peer-rating)[Top peer rating](https://core.telegram.org/api/top-rating)

If [enabled](https://core.telegram.org/method/contacts.toggleTopPeers), the rating of [top peers](https://core.telegram.org/constructor/topPeer) indicates the relevance of a frequently used peer in a certain [category](https://core.telegram.org/type/TopPeerCategory) (frequently messaged users, frequently used bots, inline bots, frequently visited channels and so on).

#### [](https://core.telegram.org/api#handling-file-references)[Handling file references](https://core.telegram.org/api/file-references)

How to handle file references.

#### [](https://core.telegram.org/api#seamless-telegram-login)[Seamless Telegram Login](https://core.telegram.org/api/url-authorization)

Handle Seamless Telegram Login URL authorization requests.

#### [](https://core.telegram.org/api#wallpapers)[Wallpapers](https://core.telegram.org/api/wallpapers)

How to work with chat backgrounds.

#### [](https://core.telegram.org/api#notification-sounds)[Notification sounds](https://core.telegram.org/api/ringtones)

How to work with chat notification sounds.

#### [](https://core.telegram.org/api#message-transcription)[Message transcription](https://core.telegram.org/api/transcribe)

How to transcribe voice messages.

#### [](https://core.telegram.org/api#message-translation)[Message translation](https://core.telegram.org/api/translation)

Telegram allows translating chat messages, and [Telegram Premium](https://core.telegram.org/api/premium) users may even enable real-time chat translation.

#### [](https://core.telegram.org/api#native-antispam-system)[Native antispam system](https://core.telegram.org/api/antispam)

Admins of supergroups with a certain number of members can choose to unleash the full proactive power of Telegram's own antispam algorithms – turning on the new Aggressive mode for the automated spam filters.

#### [](https://core.telegram.org/api#collectibles)[Collectibles](https://core.telegram.org/api/fragment)

Telegram users can make it easy for others to contact them or find their public groups and channels via [usernames](https://telegram.org/faq#usernames-and-t-me): clients can also assign multiple [Fragment»](https://fragment.com/)**collectible usernames** to accounts, supergroups and channels they own; [Fragment»](https://fragment.com/) also allows purchasing phone number collectibles that can be used to register Telegram accounts.

#### [](https://core.telegram.org/api#telegram-premium)[Telegram Premium](https://core.telegram.org/api/premium)

Telegram Premium is an optional subscription service that unlocks additional exclusive client-side and API-side features, while helping support the development of the app. It is a part of Telegram’s **sustainable monetization** – driven by our users, rather than advertisers or shareholders. This way, Telegram can remain independent and prioritize its users first.

#### [](https://core.telegram.org/api#telegram-business)[Telegram Business](https://core.telegram.org/api/business)

Users can turn their Telegram account into a **business account**, gaining access to business features such as opening hours, location, quick replies, automated messages, custom start page, chatbot support, and more.

For the moment, all Telegram Business features are available for free to [Telegram Premium](https://core.telegram.org/api/premium) subscribers.

#### [](https://core.telegram.org/api#telegram-stars)[Telegram Stars](https://core.telegram.org/api/stars)

Telegram Stars are virtual items that allow users to purchase digital goods and services from bots and mini apps inside the Telegram ecosystem, send gifts to content creators on the Telegram platform, and more.

#### [](https://core.telegram.org/api#subscriptions)[Subscriptions](https://core.telegram.org/api/subscriptions)

Bots and channels may create subscriptions, periodically charging users a certain amount of [Telegram Stars](https://core.telegram.org/api/stars) in exchange for content and services.

#### [](https://core.telegram.org/api#gifts)[Gifts](https://core.telegram.org/api/gifts)

Users can send **Gifts** to their friends. The recipients of gifts can display them on their profile pages or turn them into [Telegram Stars »](https://core.telegram.org/api/stars). Telegram Stars can be used for many things, including supporting creators and buying services in mini apps.

#### [](https://core.telegram.org/api#paid-media)[Paid media](https://core.telegram.org/api/paid-media)

Content creators can accept [Stars](https://core.telegram.org/api/stars) by publishing **paid photos or videos** on their channels. Subscribers will be allowed to view such posts only after paying the author to unlock them.

#### [](https://core.telegram.org/api#paid-messages)[Paid messages](https://core.telegram.org/api/paid-messages)

Telegram Stars can be used to pay for sending messages to users, supergroups and channels that have configured [Star Messages »](https://telegram.org/blog/star-messages-gateway-2-0-and-more#stay-in-control-of-your-inbox-with-star-messages), requiring a payment for every message sent to them.

#### [](https://core.telegram.org/api#suggested-posts)[Suggested posts](https://core.telegram.org/api/suggested-posts)

Telegram offers a powerful monetization feature to channel administrators: **suggested posts**.

#### [](https://core.telegram.org/api#channel-and-supergroup-boosts)[Channel and supergroup boosts](https://core.telegram.org/api/boost)

[Telegram Premium](https://core.telegram.org/api/premium) users can grant their favorite channels additional features like the ability to post [stories](https://core.telegram.org/api/stories) by giving them **boosts**.

#### [](https://core.telegram.org/api#giveaways-amp-gifts)[Giveaways & gifts](https://core.telegram.org/api/giveaways)

Telegram [channel](https://core.telegram.org/api/channel) administrators may launch giveaways to randomly distribute [Telegram Premium](https://core.telegram.org/api/premium) subscriptions and other gifts among their followers, in exchange for [boosts](https://core.telegram.org/api/boost).

#### [](https://core.telegram.org/api#action-bar)[Action bar](https://core.telegram.org/api/action-bar)

Sometimes, when interacting with Telegram users via private or secret chats, an action bar must be shown on top of the chat, offering convenient action buttons or notices regarding the user.

#### [](https://core.telegram.org/api#saved-messages)[Saved messages](https://core.telegram.org/api/saved-messages)

The Saved Messages chat allows users to bookmark messages and media: it's a personal cloud storage for any messages or media you may want to send or forward there.

#### [](https://core.telegram.org/api#profile)[Profile](https://core.telegram.org/api/profile)

Telegram offers many customization options for your profile!

#### [](https://core.telegram.org/api#themes)[Themes](https://core.telegram.org/api/themes)

Telegram apps support generating, sharing and synchronizing app themes.

### [](https://core.telegram.org/api#sponsored-messages)[Sponsored messages](https://core.telegram.org/api/sponsored-messages)

If your app allows accessing content from Telegram [channels](https://telegram.org/tour/channels), you must include support for [official sponsored messages](https://core.telegram.org/api/sponsored-messages) in Telegram channels.

### [](https://core.telegram.org/api#channel-and-bot-ad-revenue)[Channel and bot ad revenue](https://core.telegram.org/api/revenue)

Telegram has one of the **most generous reward systems** in the history of social media. Telegram channel and bot owners can now receive **50%** of the revenue from ads displayed in their channels and bots.

This page describes the methods used to withdraw channel and bot ad revenue, as well as view detailed revenue stats.

### [](https://core.telegram.org/api#fact-checks)[Fact-checks](https://core.telegram.org/api/factcheck)

Telegram clients support displaying fact-checks added to messages by independent fact-checkers.

### [](https://core.telegram.org/api#contacts)[Contacts](https://core.telegram.org/api/contacts)

Working with contacts in the API.

### [](https://core.telegram.org/api#blocklist)[Blocklist](https://core.telegram.org/api/block)

Working with the blocklist.

### [](https://core.telegram.org/api#nearby-usersampchats)[Nearby users&chats](https://core.telegram.org/api/nearby)

How to work with geolocation-based features like geochats and the nearby users feature.

### [](https://core.telegram.org/api#age-verification)[Age verification](https://core.telegram.org/api/age-verification)

Some legislations require age verification to view restricted content: Telegram implements this through the [Main Mini App](https://core.telegram.org/api/bots/webapps#main-mini-apps) of a special bot.

#### [](https://core.telegram.org/api#web-events)[Web events](https://core.telegram.org/api/web-events)

When interacting with HTML5 games and the websites of payment gateways, Telegram apps should expose the following JS APIs.

#### [](https://core.telegram.org/api#deep-links)[Deep links](https://core.telegram.org/api/links)

Telegram clients must handle special `tg://` and `t.me` deep links encountered in messages, link entities and in other apps by registering OS handlers.

#### [](https://core.telegram.org/api#takeout)[Takeout](https://core.telegram.org/api/takeout)

Telegram's API allows users to export all of their information through the takeout API.

##### Telegram

 Telegram is a cloud-based mobile and desktop messaging app with a focus on security and speed. 

##### [About](https://telegram.org/faq)

*   [FAQ](https://telegram.org/faq)
*   [Privacy](https://telegram.org/privacy)
*   [Press](https://telegram.org/press)

##### [Mobile Apps](https://telegram.org/apps#mobile-apps)

*   [iPhone/iPad](https://telegram.org/dl/ios)
*   [Android](https://telegram.org/android)
*   [Mobile Web](https://telegram.org/dl/web)

##### [Desktop Apps](https://telegram.org/apps#desktop-apps)

*   [PC/Mac/Linux](https://desktop.telegram.org/)
*   [macOS](https://macos.telegram.org/)
*   [Web-browser](https://telegram.org/dl/web)

##### [Platform](https://core.telegram.org/)

*   [API](https://core.telegram.org/api)
*   [Translations](https://translations.telegram.org/)
*   [Instant View](https://instantview.telegram.org/)

##### [About](https://telegram.org/faq)

##### [Blog](https://telegram.org/blog)

##### [Press](https://telegram.org/press)

##### [Moderation](https://telegram.org/moderation)
