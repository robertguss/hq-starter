---
tags:
  - library
title: "https://garden.oxus.net/technology/obsidian-to-word/"
url: "https://garden.oxus.net/technology/obsidian-to-word/"
company: [personal]
topics: []
created: 2025-04-27
source_type: raindrop
raindrop_id: 1026565843
source_domain: "garden.oxus.net"
source_type_raindrop: link
collection: "Stationery & Journals"
collection_id: 69292901
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Obsidian to Word

URL Source: https://garden.oxus.net/technology/obsidian-to-word/

Markdown Content:
This page has instructions on how to insert citations in Obsidian that can then be exported to a Word file. The setup allows you to enter citations in Obsidian with Zotero and continue to edit those citations using the Zotero plugin in Word after export.

For a list of other plugins I use in Obsidian, see [My Obsidian Setup](https://garden.oxus.net/technology/my-obsidian-setup/). If you've already finished the steps in the quick start guide below and are looking for more advanced options, check out the page: [Customizing Obsidian to Word](https://garden.oxus.net/technology/customizing-obsidian-to-word/).

## Required tools needed for this workflow

#### Apps

*   [Obsidian](https://obsidian.md/)
*   Microsoft Word (Part of [Office 365](https://www.microsoft.com/en-us/microsoft-365/microsoft-office))
*   [Zotero](https://www.zotero.org/)
*   [Pandoc](https://pandoc.org/)
    *   This app doesn't have a normal user interface (GUI), but installing it will allow other apps to access and use its commands.

#### Zotero Plugins

*   [Better BibTex](https://retorque.re/zotero-better-bibtex/)
    *   Allows you to create a continuously updated export of your Zotero reference library that is formatted in such a way that it can "speak" to Pandoc.

#### Obsidian Plugins

*   [Pandoc Reference List](https://github.com/mgmeyers/obsidian-pandoc-reference-list)
    *   Allows you to automatically format and list all in-text citations, with autocomplete from your Zotero library via its API.

*   [Enhancing Export](https://github.com/mokeyish/obsidian-enhancing-export)
    *   Allows you to export from Obsidian to Microsoft Word (and other formats) using Pandoc. A key feature is the ability to add custom Pandoc commands that will run by default, meaning that once you have set things up the first time, it should be fairly automatic.

#### Word Plugins

*   Zotero 
    *   This plugin is bundled with Zotero and should be installed automatically when you first start Zotero. If not, here are [instructions for installing it manually](https://www.zotero.org/support/word_processor_plugin_manual_installation).

## Setup (quick start version)

The following steps only need to be completed once. After the initial setup, the workflow should be mostly automated.

Note: These instructions are written for MacOS. Some steps may differ for Windows users. (If someone would like to provide additional notes for Windows users I'd be happy to add them.)

This quick start version will get you up and running in minutes. I also have [a more advanced guide](https://garden.oxus.net/technology/customizing-obsidian-to-word/) (very much a work-in-progress) for those who want greater customization, such as specifying custom styles for the exported Word document.

#### 1 Create a dedicated export folder

Create a dedicated folder for exporting and converting your files. Use the same folder each time to ensure the workflow functions correctly. I recommend using a name that is all lower case and has no spaces. For example, I use `obsidian2word`, and the path to the folder is: `/Users/[name of your user folder]/Documents/obsidian2word`. That is, it's located in the root level of my Documents folder on my Mac.

Since each person's user folder is named differently, you will have to check yours. On a Mac you can get the full path to the folder (which you'll need later) as follows: control-click the folder in Finder and hold down the `option` key. Select the option to copy the folder's full path to your clipboard.

#### 2 Download the Lua Filter

Navigate to [this page](https://retorque.re/zotero-better-bibtex/exporting/pandoc/#from-markdown-to-zotero-live-citations) in the Better BibTeX documentation, and scroll down to the section titled "From Markdown to Zotero live citations." (The link should take you right there). Then look for the following text: "download the Pandoc filter". Right-click on it and choose "save as." Save it in the folder you chose in the first step. Mine is called `zotero.lua`.

This file is the magic sauce that will allow Pandoc to create "live" citations in Word that can be edited by the Zotero plugin. The page where you downloaded it offers more instructions if you want to modify the lua script to do other things.

#### 3 Configure Enhancing Export

Enhancing Export is an Obsidian plugin. (See above.)

Open the settings for the Enhancing Export Obsidian plugin and set the default export path to the dedicated folder from steps 1 and 2.

Under "choose template", select `Word (.docx)`. Then, in the "extra arguments" field, add the following:

```
--lua-filter=/Users/[name of your user folder]/Documents/obsidian2word
```

(See step 1 for instructions on getting the full path to your export folder.)

## Entering citations in Obsidian

In Obsidian, enter citations using the standard Pandoc format:`[@friedmanDefiningEthnographicFilm2020,29]`. There are three important elements here:

1.   Square brackets framing the reference
2.   The "@" symbol followed by the "citekey" (a unique identifier generated by Zotero, consisting of the first author's surname, a shortened version of the title, and the publication year, without spaces)
3.   An optional page number, preceded by a comma

If you aren't citing a specific page, simply omit the comma and page number, leaving just the citekey inside square brackets. Like this: `[@friedmanDefiningEthnographicFilm2020]`, which will give you (Friedman 2020).

If you are entering multiple citations at the same time, you just separate them with a semicolon, but keep them all within the same square brackets, like this: `[@friedmanCollaborationEthnographyHow2013; @friedmanEnteringMountainsRule2010; @barclayOutcastsEmpireJapan2017]`, which (if using Chicago) will output to something like this: (Friedman 2013; 2010; Barclay 2017).

And if you want to suppress the author altogether, for instance if you've already mentioned their name in the body of the text, then you add a minus sign, `-`, before the `@` symbol. Like so: `[-@friedmanDefiningEthnographicFilm2020,23]`, which will give you (2020, 23).

The Pandoc Reference List plugin provides autocomplete suggestions from your Zotero library when you start typing the "@" symbol and author name. (Remember to manually add the square brackets around the reference!) And if you aren't in "source view" the plugin will make the reference appear as if they are formatted, just like Zotero does in Word. (In "source view" you will still see the raw code as shown above.)

The plugin also displays a sidebar with fully formatted references.

## Export

To export your document, open up the Obsidian command palette by using the keyboard shortcut (`command-p` on a Mac). Then type `export`. You will see the option for "Enhancing Export: Export to..." Select that. Make sure to choose `Word (.docx)` as your export format.

Note 1: Zotero must be running during the export process

Note 2: Avoid using special characters, like quotation marks, in your document name. I've found that this can cause errors.

## Refresh

After exporting to Word, you may see code in place of the formatted Zotero citations. To fix this, simply switch to the Zotero plugin menu in Word and click "refresh". The citations should now appear as if you had originally formatted them in Word using Zotero.

(Alternatively, you can open the "Document Preferences" in Word and click OK to refresh the citations.)

## Tips and Tricks

The above quick start guide should get you going. Please make sure this is working for you before trying anything else. When you are ready, you can check out my my [Customizing Obsidian to Word](https://garden.oxus.net/technology/customizing-obsidian-to-word/) guide for some additional tricks:

*   Add a reference document telling the script how to style your Word document.
*   Add metadata to your Obsidian document to pre-fill the title, author, date, and other fields on export.
*   Merge multiple documents before export.

This is just a fraction of what is possible. Other things you can do include exporting directly to PDF with formatted citations. (That is, without first exporting to Word.) Or automatically creating a table of contents when you export. If I ever figure these things out for myself I will write them up here as well.

## Acknowledgements

*   I would like to thank the following people for their help in figuring out this workflow. Without whom I never would have figured all this out! 
    *   User parfitt.christine, in the Zotero forums, where she gave [the instructions](https://forums.zotero.org/discussion/comment/407793/#Comment_407793) that got me started.
    *   retorquere, the developer of Better BibTeX who gave some [useful advice](https://github.com/retorquere/zotero-better-bibtex/discussions/2873).
    *   And user jptownley, from the Obsidian Discord, who showed me how to use Enhancing Export and a reference document.
    *   And user FeralFlora, from the Obsidian Discord, for additional feedback and suggestions on how to deal with reference documents.
