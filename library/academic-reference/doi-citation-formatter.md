---
tags:
  - library
title: "DOI Citation Formatter"
url: "https://citation.doi.org/docs.html"
company: [personal]
topics: []
created: 2025-05-06
source_type: raindrop
raindrop_id: 1034024761
source_domain: "citation.doi.org"
source_type_raindrop: link
collection: "Academic & Reference"
collection_id: 69292905
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: DOI Citation Formatter

URL Source: https://citation.doi.org/docs.html

Markdown Content:
## DOI Content Negotiation

DOIs provide a persistent link to content. They identify many types of work, from journal articles to research data sets. Typically, someone interacting with DOIs will be a researcher, who will resolve DOIs found in scholarly references to content using a [DOI resolver](https://doi.org/). Such researchers may not even realise they are using DOIs and a DOI resolver since they may follow links with embedded DOIs.

Yet DOIs can provide more than a permanent, indirect link to content. DOI registration agencies such as Crossref, DataCite and mEDRA collect bibliographic metadata about the works they link to. This metadata can be retrieved from a DOI resolver too, using content negotiation to request a particular representation of the metadata.

For some DOIs content negotiation can be used to retrieve different representations of a work. For example, some DataCite DOIs identify data sets that may be available in a number of data formats and container formats.

### Redirection

The DOI resolver at doi.org will normally redirect a user to the resource location of a DOI. For example, the DOI "10.1126/science.169.3946.635" redirects to a landing page describing the article, "The Structure of Ordinary Water". Content negotiated requests to doi.org that ask for a content type which isn't "text/html" will generally be redirected to a metadata service hosted by the DOI's registration agency. Most DOI registration agencies support content negotiated DOIs via their respective resolvers.

       GET "Accept: text/html"
https://doi.org/10.1126/science.169.3946.635

                    |
                    |
                    |
                    V

        Publisher landing page
https://www.sciencemag.org/content/169/3946/635
Normal browser requests or explicit requests for text/html redirect to the content's landing page.

       GET "Accept: application/rdf+xml"
https://doi.org/10.1126/science.169.3946.635

                    |
                    |
                    |
                    V

    Crossref metadata service
https://api.crossref.org/10.1126/science.169.3946.635/transform
Requests for a data type redirect to a registration agency's metadata service.

### What is Content Negotiation?

Making a content negotiated request requires the use of a HTTP header, "Accept". Content types that are acceptable to the client (those that it knows how to parse), each with an optional "quality" value indicating its relative suitability. For example, a client that wishes to receive CSL-JSON if it is available, but which can also handle RDF XML if CSL-JSON is unavailable, would make a request with an Accept header listing both "application/vnd.citationstyles.csl+json" and "application/rdf+xml":

$ curl -LH "Accept: application/rdf+xml;q=0.5, application/vnd.citationstyles.csl+json;q=1.0" https://doi.org/10.1126/science.169.3946.635

{
    "volume" : "169",
    "issue" : "3946",
    "DOI" : "10.1126/science.169.3946.635",
    "URL" : "https://doi.org/10.1126/science.169.3946.635",
    "title" : "The Structure of Ordinary Water: New data and interpretations are
            yielding new insights into this fascinating substance",
    "container-title" : "Science",
    "publisher" : "American Association for the Advancement of Science AAAS (Science)",
    "issued" : { "date-parts" : [ [ 1970,8,14 ] ] },
    "author" : [ { "family" : "Frank", "given" : "H. S."} ],
    "editor" : [],
    "page" : "635-641",
    "type" : "article-journal"
}
This request favours CSL-JSON but will accept RDF XML if CSL-JSON is unavailable. The q values are optional. The request could have been written without them. The order of content types then becomes important; more suitable content types should be placed at the front of the Accept header.

$ curl -LH "Accept: application/vnd.citationstyles.csl+json, application/rdf+xml" https://doi.org/10.1126/science.169.3946.635
#### Response Codes

| Code | Meaning |
| --- | --- |
| 200 | The request was OK. |
| 204 | The request was OK but there was no metadata available. |
| 404 | The DOI requested doesn't exist. |
| 406 | Can't serve any requested content type. |

Individual RA metadata services may utilise additional response codes but they will always use the response codes above in event of the case described.

If multiple content types specified by the client are supported by a DOI then the content type with the highest "q" value (or, if no "q" values are specified, the one that appears first in the "accept" header) will be returned.

### Supported Content Types

Most DOI registration agencies have implemented content negotation for their DOIs. They support a number of metadata content types, some of which are common to multiple RAs. For example, here are some content types supported by some of Crossref, DataCite, and mEDRA:

| Format | Content Type | Crossref | DataCite | mEDRA |
| --- | --- | --- | --- | --- |
| [RDF XML](http://www.w3.org/TR/rdf-syntax-grammar/) | application/rdf+xml | Yes | Yes | Yes |
| [RDF Turtle](http://www.w3.org/TeamSubmission/turtle/) | text/turtle | Yes | Yes | Yes |
| [CSL-JSON](https://github.com/citation-style-language/schema#csl-json-schema) | application/vnd.citationstyles.csl+json | Yes | Yes | Yes |
| [Schema.org in JSON-LD](http://schema.org/) | application/vnd.schemaorg.ld+json | No | Yes | No |
| [Formatted text citation](http://citationstyles.org/) | text/x-bibliography | Yes | Yes | Yes |
| [RIS](http://en.wikipedia.org/wiki/RIS_(file_format)) | application/x-research-info-systems | Yes | Yes | No |
| [BibTeX](http://en.wikipedia.org/wiki/BibTeX) | application/x-bibtex | Yes | Yes | Yes |
| [Crossref Unixref XML](https://support.crossref.org/hc/en-us/articles/214936283-UNIXREF-query-output-format) | application/vnd.crossref.unixref+xml | Yes | No | No |
| [Crossref UNIXSD XML](https://www.crossref.org/documentation/retrieve-metadata/xml-output-formats/unixsd-query-output-format/) | application/vnd.crossref.unixsd+xml | Yes | No | No |
| [DataCite XML](https://schema.datacite.org/) | application/vnd.datacite.datacite+xml | No | Yes | No |
| [ONIX for DOI](http://www.medra.org/en/schema.htm) | application/vnd.medra.onixdoi+xml | No | No | Yes |

Using content negotiation it is possible to make a request that favours content types specific to a particular registration agency but which will also degrade to respond with a more standard content type for other registration agencies. For example:

$ curl -LH "Accept: application/vnd.crossref.unixref+xml;q=1, application/rdf+xml;q=0.5" https://doi.org/10.1126/science.169.3946.635
This request will return Crossref XML for Crossref DOIs and RDF XML for non-Crossref DOIs, such as DataCite DOIs.

#### Formatted Citations

In order to work with the DOI Citation Formatter, a DOI needs to provide metadata in [application/vnd.citationstyles.csl+json format](https://citeproc-js.readthedocs.io/en/latest/csl-json/markup.html). The citation formatter itself will do the extra work of formatting into a particular citation style and locale according to a user's request.

Some DOI registration agencies support formatted citations via the text/bibliography content type. These are the output of the [Citation Style Language](http://citationstyles.org/) processor, citeproc-js. The content type can take two additional parameters to customise its response format. A "style" can be chosen from the list of style names found in the [CSL style repository](https://github.com/citation-style-language/styles). Many styles are supported, including common styles such as apa and harvard3:

$ curl -LH "Accept: text/x-bibliography; style=apa" https://doi.org/10.1126/science.169.3946.635

Frank, H. S. (1970). The Structure of Ordinary Water: New data and interpretations are yielding
    new insights into this fascinating substance. Science, 169(3946), 635-641. American Association
    for the Advancement of Science AAAS (Science). doi:10.1126/science.169.3946.635
A locale can also be specified. Use one of the locale names from the [CSL locales repository](https://github.com/citation-style-language/locales):

$ curl -LH "Accept: text/x-bibliography; style=harvard3; locale=fr-FR" https://doi.org/10.1126/science.169.3946.635

Frank, HS 1970, « The Structure of Ordinary Water: New data and interpretations are yielding new
    insights into this fascinating substance ». Science, vol. 169, no. 3946, p. 635-641. Consulté
    de https://doi.org/10.1126/science.169.3946.635
### Getting Help

Send questions or comments to [info@doi.org](mailto:info@doi.org).
