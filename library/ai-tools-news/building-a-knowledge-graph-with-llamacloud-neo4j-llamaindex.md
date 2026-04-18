---
tags:
  - library
title: "Building a Knowledge Graph with LlamaCloud & Neo4J - LlamaIndex"
url: "https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?utm_medium=email&_hsmi=376348861&utm_content=376348861&utm_source=hs_email"
company: [personal]
topics: []
created: 2025-08-20
source_type: raindrop
raindrop_id: 1306878298
source_domain: "docs.llamaindex.ai"
source_type_raindrop: article
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Building a Knowledge Graph with LlamaCloud & Neo4J

URL Source: https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861

Markdown Content:
RAG is as a powerful technique for enhancing LLMs with external knowledge, but traditional semantic similarity search often fails to capture nuanced relationships between entities, and can miss critical context that spans across multiple documents. By transforming unstructured documents into structured knowledge representations, we can perform complex graph traversals, relationship queries, and contextual reasoning that goes far beyond simple similarity matching.

Tools like LlamaParse, LlamaClassify and LlamaExtract provide robust parsing, classification and extraction capabilities to convert raw documents into structured data, while Neo4j serves as the backbone for knowledge graph representation, forming the foundation of GraphRAG architectures that can understand not just what information exists, but how it all connects together.

In this end-to-end tutorial, we will walk through an example of legal document processing that showcases the full pipeline shown below.

The pipeline contains the following steps:

*   Use [LlamaClassify](https://docs.cloud.llamaindex.ai/llamaclassify/getting_started) - a LlamaCloud tool currently in beta, to classify contracts
*   Leverage [LlamaExtract](https://www.llamaindex.ai/llamaextract) to extract different sets of relevant attributes tailored to each specific contract category based on the classification
*   Store all structured information into a Neo4j knowledge graph, creating a rich, queryable representation that captures both content and intricate relationships within legal documents

## Setting Up Requirements

[Section titled “Setting Up Requirements”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#setting-up-requirements)

`!pip install llama-index-workflows llama-cloud-services jsonschema openai neo4j llama-index-llms-openai`

`import reimport uuidfrom datetime import datefrom typing import List, Optionalfrom getpass import getpassfrom neo4j import AsyncGraphDatabasefrom openai import AsyncOpenAIfrom pydantic import BaseModel, Fieldfrom llama_cloud_services.beta.classifier.client import ClassifyClientfrom llama_cloud.types import ClassifierRulefrom llama_cloud.client import AsyncLlamaCloudfrom llama_cloud_services.extract import (    ExtractConfig,    ExtractMode,    LlamaExtract,    SourceText,)from llama_cloud_services.parse import LlamaParsefrom llama_index.llms.openai import OpenAI`

## Download Sample Contract

[Section titled “Download Sample Contract”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#download-sample-contract)

Here, we download a sample PDF from the Cuad dataset

`!wget https://raw.githubusercontent.com/tomasonjo/blog-datasets/5e3939d10216b7663687217c1646c30eb921d92f/CybergyHoldingsInc_Affliate%20Agreement.pdf`

For Neo4j, the simplest approach is to create a free [Aura database instance](https://neo4j.com/product/auradb/), and copy your credentials here.

`db_url = "your-db-url"username = "neo4j"password = "your-password"neo4j_driver = AsyncGraphDatabase.driver(    db_url,    auth=(        username,        password,    ),)`

## Parse the Contract with LlamaParse

[Section titled “Parse the Contract with LlamaParse”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#parse-the-contract-with-llamaparse)

Next, we set up LlamaParse and parse the PDF. In this case, we’re using `parse_page_without_llm` mode.

`import osos.environ["LLAMA_CLOUD_API_KEY"] = getpass("Enter your Llama API key: ")os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")`

`# Initialize parser with specified modeparser = LlamaParse(parse_mode="parse_page_without_llm")# Define the PDF file to parsepdf_path = "CybergyHoldingsInc_Affliate Agreement.pdf"# Parse the document asynchronouslyresults = await parser.aparse(pdf_path)`

`Started parsing the file under job_id 6687bc90-d4eb-48a5-b56a-f4bfe8f00d33`

`print(results.pages[0].text)`

`Exhibit 10.27    MARKETING AFFILIATE AGREEMENT                 Between:Birch First Global Investments Inc.                And    Mount Knowledge Holdings Inc.    Dated: May 8, 2014    1    Source: CYBERGY HOLDINGS, INC., 10-Q, 5/20/2014`

## Contract classification with LlamaClassify (beta)

[Section titled “Contract classification with LlamaClassify (beta)”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#contract-classification-with-llamaclassify-beta)

In this example, we want to classify incoming contracts. They can either be `Affiliate Agreements` or `Co Branding`. For this cookbook, we are going to use **[LlamaClassify](https://docs.cloud.llamaindex.ai/llamaclassify/getting_started/)**, our powerful AI-powered document classification tool that’s currently in **beta**!

### Define classification rules

[Section titled “Define classification rules”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#define-classification-rules)

`rules = [    ClassifierRule(        type="Affiliate Agreements",        description="This is a contract that outlines an affiliate agreement",    ),    ClassifierRule(        type="Co Branding",        description="This is a contract that outlines a co-branding deal/agreement",    ),]`

## Initialize the ClassifyClient and Run a Classification Job

[Section titled “Initialize the ClassifyClient and Run a Classification Job”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#initialize-the-classifyclient-and-run-a-classification-job)

`classifier = ClassifyClient(    client=AsyncLlamaCloud(        base_url="https://api.cloud.llamaindex.ai",        token=os.environ["LLAMA_CLOUD_API_KEY"],    ))`

`result = await classifier.aclassify_file_path(    rules=rules,    file_input_path="/content/CybergyHoldingsInc_Affliate Agreement.pdf",)`

`classification = result.items[0].resultprint("Classification Result: " + classification.type)print("Classification Reason: " + classification.reasoning)`

`Classification Result: affiliate_agreementsClassification Reason: The document is titled 'Marketing Affiliate Agreement' and repeatedly refers to one party as the 'Marketing Affiliate' (MA). The agreement grants the MA the right to market, advertise, and sell the company's technology, and outlines the duties and responsibilities of the affiliate in marketing, licensing, and supporting the technology. There is no mention of joint branding, shared trademarks, or collaborative marketing under both parties' brands, which would be characteristic of a co-branding agreement. The content is entirely consistent with an affiliate agreement, where one party markets and sells products or services on behalf of another, rather than a co-branding arrangement.`

Next, we define some schemas which we can use to extract relevant information from our contracts with. The fields we define are a mix of summarization and structured data extraction.

Here we define two Pydantic models: `Location` captures structured address information with optional fields for country, state, and address, while `Party` represents contract parties with a required name and optional location details. The Field descriptions help guide the extraction process by telling the LLM exactly what information to look for in each field.

`class Location(BaseModel):    """Location information with structured address components."""    country: Optional[str] = Field(None, description="Country")    state: Optional[str] = Field(None, description="State or province")    address: Optional[str] = Field(None, description="Street address or city")class Party(BaseModel):    """Party information with name and location."""    name: str = Field(description="Party name")    location: Optional[Location] = Field(        None, description="Party location details"    )`

Remember we have multiple contract types, so we need to define specific extraction schemas for each type and create a mapping system to dynamically select the appropriate schema based on our classification result.

`class BaseContract(BaseModel):    """Base contract class with common fields."""    parties: Optional[List[Party]] = Field(        None, description="All contracting parties"    )    agreement_date: Optional[str] = Field(        None, description="Contract signing date. Use YYYY-MM-DD"    )    effective_date: Optional[str] = Field(        None, description="When contract becomes effective. Use YYYY-MM-DD"    )    expiration_date: Optional[str] = Field(        None, description="Contract expiration date. Use YYYY-MM-DD"    )    governing_law: Optional[str] = Field(        None, description="Governing jurisdiction"    )    termination_for_convenience: Optional[bool] = Field(        None, description="Can terminate without cause"    )    anti_assignment: Optional[bool] = Field(        None, description="Restricts assignment to third parties"    )    cap_on_liability: Optional[str] = Field(        None, description="Liability limit amount"    )class AffiliateAgreement(BaseContract):    """Affiliate Agreement extraction."""    exclusivity: Optional[str] = Field(        None, description="Exclusive territory or market rights"    )    non_compete: Optional[str] = Field(        None, description="Non-compete restrictions"    )    revenue_profit_sharing: Optional[str] = Field(        None, description="Commission or revenue split"    )    minimum_commitment: Optional[str] = Field(        None, description="Minimum sales targets"    )class CoBrandingAgreement(BaseContract):    """Co-Branding Agreement extraction."""    exclusivity: Optional[str] = Field(        None, description="Exclusive co-branding rights"    )    ip_ownership_assignment: Optional[str] = Field(        None, description="IP ownership allocation"    )    license_grant: Optional[str] = Field(        None, description="Brand/trademark licenses"    )    revenue_profit_sharing: Optional[str] = Field(        None, description="Revenue sharing terms"    )mapping = {    "affiliate_agreements": AffiliateAgreement,    "co_branding": CoBrandingAgreement,}`

`extractor = LlamaExtract()agent = extractor.create_agent(    name=f"extraction_workflow_import_{uuid.uuid4()}",    data_schema=mapping[classification.type],    config=ExtractConfig(        extraction_mode=ExtractMode.BALANCED,    ),)result = await agent.aextract(    files=SourceText(        text_content=" ".join([el.text for el in results.pages]),        filename=pdf_path,    ),)result.data`

`Uploading files: 100%|██████████| 1/1 [00:00<00:00,  1.81it/s]Creating extraction jobs: 100%|██████████| 1/1 [00:00<00:00,  1.43it/s]Extracting files: 100%|██████████| 1/1 [00:12<00:00, 12.75s/it]{'parties': [{'name': 'Birch First Global Investments Inc.',   'location': {'country': 'U.S. Virgin Islands',    'state': None,    'address': '9100 Havensight, Port of Sale, Ste. 15/16, St. Thomas, VI 0080'}},  {'name': 'Mount Knowledge Holdings Inc.',   'location': {'country': 'United States',    'state': 'Nevada',    'address': '228 Park Avenue S. #56101 New York, NY 100031502'}}], 'agreement_date': '2014-05-08', 'effective_date': '2014-05-08', 'expiration_date': None, 'governing_law': 'State of Nevada', 'termination_for_convenience': True, 'anti_assignment': True, 'cap_on_liability': "Company's liability shall not exceed the fees that MA has paid under this Agreement.", 'exclusivity': None, 'non_compete': None, 'revenue_profit_sharing': 'MA receives a purchase discount based on annual purchase level: 15% for $0-$100,000, 20% for $100,001-$1,000,000, 25% for $1,000,001 and above. MA pays a quarterly service fee of $15,000 if no sales occur in a quarter.', 'minimum_commitment': 'MA commits to purchase a minimum of 100 Units in aggregate within the Territory within the first six months of the term of this Agreement.'}`

## Import into Neo4j

[Section titled “Import into Neo4j”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#import-into-neo4j)

The final step is to take our extracted structured information and build a knowledge graph that represents the relationships between contract entities. We need to define a graph model that specifies how our contract data should be organized as nodes and relationships in Neo4j.

Our graph model consists of three main node types:

*   **Contract nodes** store the core agreement information including dates, terms, and legal clauses
*   **Party nodes** represent the contracting entities with their names
*   **Location nodes** capture geographic information with address components.

Now we’ll import our extracted contract data into Neo4j according to our defined graph model.

`import_query = """WITH $contract AS contractMERGE (c:Contract {path: $path})SET c += apoc.map.clean(contract, ["parties", "agreement_date", "effective_date", "expiration_date"], [])// Cast to dateSET c.agreement_date = date(contract.agreement_date),    c.effective_date = date(contract.effective_date),    c.expiration_date = date(contract.expiration_date)// Create parties with their locationsWITH c, contractUNWIND coalesce(contract.parties, []) AS partyMERGE (p:Party {name: party.name})MERGE (c)-[:HAS_PARTY]->(p)// Create location nodes and link to partiesWITH p, partyWHERE party.location IS NOT NULLMERGE (p)-[:HAS_LOCATION]->(l:Location)SET l += party.location"""response = await neo4j_driver.execute_query(    import_query, contract=result.data, path=pdf_path)response.summary.counters`

`{'_contains_updates': True, 'labels_added': 5, 'relationships_created': 4, 'nodes_created': 5, 'properties_set': 16}`

## Bringing it All Together in a Workflow

[Section titled “Bringing it All Together in a Workflow”](https://docs.llamaindex.ai/en/latest/examples/cookbooks/build_knowledge_graph_with_neo4j_llamacloud/?_hsmi=376348861#bringing-it-all-together-in-a-workflow)

Finally, we can combine all of this logic into one single executable agentic workflow. Let’s make it so that the workflow can run by accepting a single PDF, adding new entries to our Neo4j graph each time.

`affiliate_extraction_agent = extractor.create_agent(    name="Affiliate_Extraction",    data_schema=AffiliateAgreement,    config=ExtractConfig(        extraction_mode=ExtractMode.BALANCED,    ),)cobranding_extraction_agent = extractor.create_agent(    name="CoBranding_Extraction",    data_schema=CoBrandingAgreement,    config=ExtractConfig(        extraction_mode=ExtractMode.BALANCED,    ),)`

`from llama_index.core.workflow import (    Workflow,    Event,    Context,    StartEvent,    StopEvent,    step,)class ClassifyDocEvent(Event):    parsed_doc: str    pdf_path: strclass ExtractAffiliate(Event):    file_path: strclass ExtractCoBranding(Event):    file_path: strclass BuildGraph(Event):    file_path: str    data: dictclass KnowledgeGraphBuilder(Workflow):    def __init__(        self,        classifier: ClassifyClient,        rules: List[ClassifierRule],        affiliate_extract_agent: LlamaExtract,        cobranding_extract_agent: LlamaExtract,        **kwargs,    ):        super().__init__(**kwargs)        self.classifier = classifier        self.rules = rules        self.affiliate_extract_agent = affiliate_extract_agent        self.cobranding_extract_agent = cobranding_extract_agent    @step    async def classify_contract(        self, ctx: Context, ev: StartEvent    ) -> ExtractAffiliate | ExtractCoBranding | StopEvent:        result = await self.classifier.aclassify_file_path(            rules=self.rules, file_input_path=ev.pdf_path        )        contract_type = result.items[0].result.type        print(contract_type)        if contract_type == "affiliate_agreements":            return ExtractAffiliate(file_path=ev.pdf_path)        elif contract_type == "co_branding":            return ExtractCoBranding(file_path=ev.pdf_path)        else:            return StopEvent()    @step    async def extract_affiliate(        self, ctx: Context, ev: ExtractAffiliate    ) -> BuildGraph:        result = await self.affiliate_extract_agent.aextract(ev.file_path)        return BuildGraph(data=result.data, file_path=ev.file_path)    @step    async def extract_co_branding(        self, ctx: Context, ev: ExtractCoBranding    ) -> BuildGraph:        result = await self.cobranding_extract_agent.aextract(ev.file_path)        return BuildGraph(data=result.data, file_path=ev.file_path)    @step    async def build_graph(self, ctx: Context, ev: BuildGraph) -> StopEvent:        import_query = """    WITH $contract AS contract    MERGE (c:Contract {path: $path})    SET c += apoc.map.clean(contract, ["parties", "agreement_date", "effective_date", "expiration_date"], [])    // Cast to date    SET c.agreement_date = date(contract.agreement_date),      c.effective_date = date(contract.effective_date),      c.expiration_date = date(contract.expiration_date)    // Create parties with their locations    WITH c, contract    UNWIND coalesce(contract.parties, []) AS party    MERGE (p:Party {name: party.name})    MERGE (c)-[:HAS_PARTY]->(p)    // Create location nodes and link to parties    WITH p, party    WHERE party.location IS NOT NULL    MERGE (p)-[:HAS_LOCATION]->(l:Location)    SET l += party.location    """        response = await neo4j_driver.execute_query(            import_query, contract=ev.data, path=ev.file_path        )        return StopEvent(response.summary.counters)`

`knowledge_graph_builder = KnowledgeGraphBuilder(    classifier=classifier,    rules=rules,    affiliate_extract_agent=affiliate_extraction_agent,    cobranding_extract_agent=cobranding_extraction_agent,    timeout=None,    verbose=True,)`

`response = await knowledge_graph_builder.run(    pdf_path="CybergyHoldingsInc_Affliate Agreement.pdf")`

`Running step classify_contractaffiliate_agreementsStep classify_contract produced event ExtractAffiliateRunning step extract_affiliateUploading files: 100%|██████████| 1/1 [00:00<00:00,  2.84it/s]Creating extraction jobs: 100%|██████████| 1/1 [00:00<00:00,  1.68it/s]Extracting files: 100%|██████████| 1/1 [00:19<00:00, 19.04s/it]Step extract_affiliate produced event StopEvent`
