---
tags:
  - library
title: "A CSS to embellish *MultiMarkdown* rendering"
url: "https://discourse.devontechnologies.com/t/a-css-to-embellish-multimarkdown-rendering/58828"
company: [personal]
topics: []
created: 2024-12-26
source_type: raindrop
raindrop_id: 929829378
source_domain: "discourse.devontechnologies.com"
source_type_raindrop: link
collection: "Stationery & Journals"
collection_id: 69292901
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Hi all !  Many people have read, studied and enjoyed Kourosh Dini’s Taking Smart Notes with DEVONthink. He mentioned and distributed a “pre-release” CSS (Cascading Style Sheet) that I was refining for my personal use. With Kourosh’s stimulation and the knowledge that it might be appreciated by some people, I went on with the development of this style sheet.  Please, do take into account that I’m not a graphic designer nor a programmer. I copied a Brett Terpstra stylesheet that he designed for hi...

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: A CSS to embellish *MultiMarkdown* rendering - DEVONthink / Tips - DEVONtechnologies Community

URL Source: https://discourse.devontechnologies.com/t/a-css-to-embellish-multimarkdown-rendering/58828

Published Time: 2020-10-11T18:38:16+00:00

Markdown Content:
## post by OlivierPS on Oct 11, 2020

[![Image 1](https://discourse.devontechnologies.com/letter_avatar_proxy/v4/letter/o/46a35a/48.png)](https://discourse.devontechnologies.com/t/a-css-to-embellish-multimarkdown-rendering/58828)

Hi all !

Many people have read, studied and enjoyed Kourosh Dini’s _Taking Smart Notes with DEVONthink_. He mentioned and distributed a “pre-release” CSS (_Cascading Style Sheet_) that I was refining for my personal use. With Kourosh’s stimulation and the knowledge that it might be appreciated by some people, I went on with the development of this style sheet.

Please, do take into account that I’m not a graphic designer nor a programmer. I copied a [_Brett Terpstra_](https://brettterpstra.com/) stylesheet that he designed for his [_Marked_](https://marked2app.com/) software and modified it. In the process, I learnt just the minimum of CSS useful to achieve my goals. So, it may not be up to “professional standard”. But as any perfectionist should know : “Very often, functional is good enough.” So, it _just works_.

I wanted to achieve :

1.   good legibility, according to classical typographic rules ;
2.   visual clarity of the document’s structure ;
3.   compact enough layout so as to display a maximum amount of text on a _MacBook 13"_ monitor ;
4.   overall elegance.

So, in the end, the main points of this CSS are :

*   The overall look is meant to give a feeling of “pen on paper”. 
    *   Blue ink text colour, very discreet.
    *   Paper background, very discreet too.

*   Readable line length, around three alphabets — the classical rule says “around two and a half alphabet, not more than three and a half ”.
*   The text column stays centred in the window. When the window is narrow, it stays clear of the border, whatever the zoom level.
*   Links and footnote markers are discreet, but conspicuous. They are highlighted when hovered by the pointer.
*   Headers level 1 and 2 get a typographic rule, so they stand out. 
    *   It’s generally advised to use H1 as the document title and nowhere else in the document. Thus, it has a very minimal space above it in order to spare space at the top of the document.

*   Header 3 is meant as a subtitle. It’s clearly distinct from body text, but spares vertical space. Useful to introduce parts of a note.
*   Lists — both bulleted and numbered — are rather compact, but nevertheless visually breathing and logically grouped, even many levels deep.
*   Elegant, decorative ornament for HR (horizontal rule).
*   Tables : 
    *   centred horizontally ;
    *   text in heading row aligns to the bottom of the cells ;
    *   text in the rows aligns to the top of the cells ;
    *   alternating row pattern ;
    *   title is distinctive, but not overwhelming (smaller than H#) ;
    *   NB : it’s a bug of the _DEVONthink_’s rendering engine that puts the table title always _below_ the table, regardless of what is specified in the CSS. Personally, I would rather have the title _above_ the table.

*   Images : 
    *   framed with a thin line ;
    *   limited to column width ;
    *   when in “portrait mode” (i.e. taller than wide), they are vertically limited in order to preserve the proportions with the text and not fill the screen !
    *   left aligned ;
    *   the caption is visually grouped with the image.

*   Citations are in a lighter blue, serif font, in italics → intended mainly for quoting thoughts.

The graphic elements (paper background + swirl ornament) are included in the CSS, no download nor installation necessary.

Finally, I made intensive use of variables that you can find grouped at the top of the file. Thus, it’s easier for you to tweak settings to your taste ! (Edit with any “pure text” editor. The one you’re using for _Markdown_ will be just fine.)

Attached is a Zip file with the package :

*   **OpSpl.css** — the style sheet
*   **CSS OpSpl readme.md** — not only a _read me_ ; it’s also a (minimalist) “beginner’s guide” to help anyone customizing a CSS.
*   **Markdown test document.md** — a sample file for testing (use it anywhere !) and to illustrate some fine points. There are also some usage tips.

This stylesheet is not meant only for _DEVONthink_, it’s also very pleasant as a _Marked_ alternative style.

Enjoy !

Kind regards.

Olivier Spinnler

_**Post Scriptum**_ : if a talented graphic designer or a programmer feels like perfecting this modest attempt of mine into a more “professional” piece of work — maybe whith hints for different media — he/she is most welcome !

[OpSpl style sheet.zip](https://discourse.devontechnologies.com/uploads/short-url/9nFZQHqKnD4OXyXmWT2zQb5PUeb.zip) (19.2 KB)

read  8 min

## post by OlivierPS on Oct 11, 2020

## post by BLUEFROG on Oct 11, 2020

## post by brookter on Oct 12, 2020

## post by Kourosh on Oct 16, 2020

## post by korm on Oct 16, 2020

## post by EugeneChopenko on Oct 21, 2020

## post by Mitch_Wagner on Oct 21, 2020

2 months later

## post by Frederik on Dec 13, 2020

3 months later

## post by JimE on Mar 17, 2021

## post by korm on Mar 18, 2021

## post by JimE on Mar 18, 2021

## post by rmschne on Mar 18, 2021

## post by brookter on Mar 18, 2021

## post by chrillek on Mar 18, 2021

## post by chrillek on Mar 18, 2021

## post by JimE on Mar 18, 2021

## post by brookter on Mar 18, 2021

## post by Michaell on Mar 19, 2021

## post by BLUEFROG on Mar 19, 2021

## Load more posts below
