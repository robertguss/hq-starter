---
tags:
  - library
title: "Create Beautiful PDFs From Your Tinderbox Documents"
url: "https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068"
company: [personal]
topics: []
created: 2024-12-26
source_type: raindrop
raindrop_id: 929826017
source_domain: "forum.eastgate.com"
source_type_raindrop: link
collection: "Stationery & Journals"
collection_id: 69292901
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

I want to use Tinderbox to create structured documents, and then export them to beautiful PDFs.  tinderbox-to-pdf_v0_1_0.tbx (102.4 KB) is a document I created to do this. Here is the generated PDF.  It uses Pandoc to convert Tinderbox’s exported HTML to a PDF via LaTeX. Setup instructions are explained in the Tinderbox document.   I’ll push small updates to the GitHub project and update this post whenever I release a new version.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Create Beautiful PDFs From Your Tinderbox Documents - Exporting from Tinderbox - Tinderbox Forum

URL Source: https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068

Published Time: 2017-12-10T08:17:45+00:00

Markdown Content:
## post by pat on Dec 10, 2017

[![Image 1](https://forum.eastgate.com/user_avatar/forum.eastgate.com/pat/48/90_2.png)](https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068)

I want to use Tinderbox to create structured documents, and then export them to beautiful PDFs.

[tinderbox-to-pdf_v0_1_0.tbx](https://forum.eastgate.com/uploads/db7136/original/1X/8c1863eb246c1601e9c96fc659b098d1b9fc1f33.tbx) (102.4 KB) is a document I created to do this. [Here is the generated PDF.](https://drive.google.com/file/d/1PvhBzXwGGazS8Cjc5-6OGo1k_8aHCMAg/view?usp=sharing)

It uses Pandoc to convert Tinderbox’s exported HTML to a PDF via LaTeX. Setup instructions are explained in the Tinderbox document.

* * *

_I’ll push small updates to the [GitHub project](https://github.com/patmaddox/tinderbox-to-pdf) and update this post whenever I release a new version._

read  11 min

## post by PaulWalters on Dec 10, 2017

[![Image 2](https://forum.eastgate.com/user_avatar/forum.eastgate.com/paulwalters/48/2967_2.png)](https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068)

Nice work [@Pat](https://forum.eastgate.com/u/pat). Clever, well conceived and executed – and definitely worth the significant effort you obviously put into it. For longer, complex documents your approach will help a lot of readers.

Thank you!!! ![Image 3: :raised_hands:](https://forum.eastgate.com/images/emoji/apple/raised_hands.png?v=12)![Image 4: :raised_hands:](https://forum.eastgate.com/images/emoji/apple/raised_hands.png?v=12)![Image 5: :raised_hands:](https://forum.eastgate.com/images/emoji/apple/raised_hands.png?v=12)

I didn’t test this – but since you are using LaTeX for its PDF parser, would your export technique render LaTeX code when our notes contain it?

I would suggest for ease of maintenance and readability, that you consider using a code note and the techniques that Mark Anderson [explains here](http://www.acrobatfaq.com/atbref7/index/ActionsRules/Usinglongsectionsofcode.html) rather than putting the whole text of your Big Rule into the **$Rule** box in the Action Inspector. That control does not scroll, and reading a rule whose size exceeds the text box is cumbersome.

An alternative to [@Pat](https://forum.eastgate.com/u/pat)’s process is to use the Marked 2 application. Pat’s example TBX can be exported to HTML and that .html export document can be dragged into Marked 2 for rendering and saving as PDF. Just another approach for those less technically inclined.

For anyone interested in Tinderbox history, a trip to the [legacy forum](http://www.eastgate.com/Tinderbox/forum/) will reveal some earlier approaches to PDF exporting. YMMV, since that forum covers versions of Tinderbox that might operate differently than v7.

## post by pat on Dec 10, 2017

[![Image 6](https://forum.eastgate.com/user_avatar/forum.eastgate.com/pat/48/90_2.png)](https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068)

Pandoc seems to ignore LaTeX commands in the exported HTML. I suspect there’s some way to get them to work, I just haven’t explored it yet.

Cool, I haven’t used code notes yet, so I’ll check that out ![Image 7: :+1:](https://forum.eastgate.com/images/emoji/apple/+1.png?v=12)

Sort of. One feature that’s important to me is a table of contents. I want a clickable table of contents at the beginning of the PDF, and I want Preview.app to correctly show a structured table of contents as well. [Marked 2 does not support intra-document links](http://support.markedapp.com/kb/frequently-asked-questions/intra-document-links-in-exported-pdfs), so the clickable table of contents is a no-go with that.

You’re absolutely right though, there are a number of programs to convert Markdown to PDF that are a lot simpler than this setup. If I find one that does what I want, I’ll probably ditch this ![Image 8: :slight_smile:](https://forum.eastgate.com/images/emoji/apple/slight_smile.png?v=12)

(plus I know that this approach has its own tradeoffs that I’ll have to deal with)

## post by mwra on Dec 10, 2017

[![Image 9](https://forum.eastgate.com/user_avatar/forum.eastgate.com/mwra/48/4_2.png)](https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068)

FWIW, the PDF version of the Tinderbox Help that I help create uses export of styles CSS (including print media CSS) and wkhtmltopdf to generate a PDF with a ToC from the HTML. As the source TBX’s primary role is to generate the HTML needed for the app’s Help, the export to HTML for PDF use is done as a parallel and separate process.

## post by dominiquerenauld on Dec 10, 2017

[![Image 10](https://forum.eastgate.com/user_avatar/forum.eastgate.com/dominiquerenauld/48/8_2.png)](https://forum.eastgate.com/t/create-beautiful-pdfs-from-your-tinderbox-documents/1068)

For my part, I insert Latex code directly into my notes, copy and paste it into a Latex editor and Bob’s your uncle (Le tour est joué, in French)!

[![Image 11](https://forum.eastgate.com/uploads/db7136/optimized/1X/082be22e4fb7703545d0bad8fdaf5c7c58f367ed_2_690x421.jpg)](https://forum.eastgate.com/uploads/db7136/original/1X/082be22e4fb7703545d0bad8fdaf5c7c58f367ed.jpg "preamb.jpg")

## post by pat on Dec 13, 2017

## post by mwra on Dec 13, 2017

## post by pat on Dec 13, 2017

## post by mwra on Dec 13, 2017

## post by pat on Dec 14, 2017

## post by WAKAMATSU on Dec 17, 2017

## post by mwra on Dec 17, 2017

## post by WAKAMATSU on Dec 18, 2017

## post by WAKAMATSU on Dec 18, 2017

## post by mwra on Dec 18, 2017

## post by pat on Dec 22, 2017

## post by mwra on Dec 23, 2017

1 year later

## post by mwra on Feb 21, 2019

2 months later

## post by andreas on Apr 17, 2019

## post by mwra on Apr 17, 2019

## Load more posts below
