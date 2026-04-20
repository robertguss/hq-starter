---
tags:
  - library
title: "Share Your Claude Code Commands! : r/ClaudeAI"
url: "https://www.reddit.com/r/ClaudeAI/s/6lsmK30ZpJ"
company: [personal]
topics: []
created: 2025-06-14
source_type: raindrop
raindrop_id: 1165138582
source_domain: "reddit.com"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-20
hydrated_via: browser-harness
---

## Raw Content

<!-- Hydrated 2026-04-20 via browser-harness -->

# Share Your Claude Code Commands!

> **r/ClaudeAI** · posted by u/GrumpyPidgeon
> [Link to post](https://www.reddit.com/r/ClaudeAI/comments/1l3gouj/share_your_claude_code_commands/?share_id=oKZL8Ya4LhIngdMG7n_BE&utm_medium=ios_app&utm_name=iossmf&utm_source=share&utm_term=22)

I just moved over to Claude Code from Windsurf (neovim editor gets to be a 1st class citizen again!) and am probably overly obsessed with development efficiency. Please share your custom commands (user-level, project-level, whichever) that you find to be really valuable.

commit-and-push.md

I use this for every git commit, even simple ones because I am extraordinarily lazy. My favorite feature though is when it detects that some changed files should be split into different commits for better clarity.

ADD all modified and new files to git. If you think there are files that should not be in version control, ask the user. If you see files that you think should be bundled into separate commits, ask the user.
THEN commit with a clear and concise one-line commit message, using semantic commit notation.
THEN push the commit to origin.
The user is EXPLICITLY asking you to perform these git tasks.
prime.md

A little context on this. Instead of running with a CLAUDE.md in all of my projects, I have two: PLANNING.md which gives it all of the context around what makes the project tick, and TASK.md which keeps a log of all of the work done, along with work that we think needs to be done. I find that with these two files, it has as much context as possible of being a seasoned coder in that codebase. I run this every time I start a new session or do a /clear.

    # Project Understanding Prompt

    When starting a new session, follow this systematic approach to understand the project:

    ## 1. Project Overview & Structure
    - **READ** the README.md file in the project's root folder, if available. This provides the user-facing perspective and basic setup instructions.
    - **RUN** `git ls-files` to get a complete file inventory and understand the project structure.
    - **EXAMINE** the project's directory structure to understand the architectural patterns (e.g., `/cmd`, `/internal`, `/pkg` for Go projects).

    ## 2. Core Documentation
    - **READ and UNDERSTAND** the PLANNING.md file for:
      - Project architecture and design decisions
      - Technology stack and dependencies
      - Build, test, and deployment instructions
      - Future considerations and roadmap
    - **READ and UNDERSTAND** the TASK.md file for:
      - Completed work and implementation status
      - Current blockers or known issues
      - Next steps and priorities

    ## 3. Testing & Quality
    - **EXAMINE** test files to understand:
      - Testing patterns and frameworks used
      - Test coverage expectations
      - Integration vs unit test separation
      - Mock implementations and test utilities

    ## 4. Development Workflow
    - **CHECK** for automation files:
      - CI/CD pipelines (.github/workflows, .gitea/workflows)
      - Development environment setup (devenv.nix, .devcontainer)
      - Code quality tools (linting, formatting configurations)

    ## 5. Data & External Systems
    - **IDENTIFY** data models and schemas:
      - Database migrations or schema files
      - API specifications or OpenAPI docs
      - Data transfer objects (DTOs) and validation rules
    - **UNDERSTAND** external service integrations:
      - Authentication providers (Keycloak, Auth0)
      - Databases and connection patterns
      - Third-party APIs and clients

    ## 6. Documentation Maintenance
    - **UPDATE TASK.md** with each substantial change made to the project, including:
      - Features implemented or modified
      - Issues resolved or discovered
      - Dependencies added or updated
      - Configuration changes
    - **UPDATE PLANNING.md** if changes affect:
      - Architecture decisions
      - Technology stack
      - Development workflows
      - Future roadmap items

    ## 7. Knowledge Validation
    Before proceeding with any work, confirm understanding by being able to answer:
    - What is the primary purpose of this project?
    - How do I build, test, and run it locally?
    - What are the main architectural components and their responsibilities?
    - What external systems does it integrate with?
    - What's the current implementation status and what's next?

coverage.md

Thanks to AI doing what has been an awful chore of mine, for decades, I push for 100% coverage in all functions/methods/classes that involve logic. This is my cookie-cutter command on it.

UNDERSTAND the code coverage percentages for each function and method in this codebase.
THEN add unit tests to functions and methods without 100% coverage. This includes negative and edge cases.
ALWAYS use mocks for external functionality, such as web services and databases.
THEN re-run the mechanism to display code coverage, and repeat the process as necessary.
build-planning.md

I use this on any brand new projects, to act as an initial primer files. If it is a brand new codebase it will fill most of these out as TBD, but if I am retro-fitting something existing, then an awful lot will get filled out.

We are going to build a file called PLANNING.md which lives in the project's root directory. The objective is to have a document that will give you important context about the project, along with instructions on how to build and test. Start by building a document with the following categories, that we will initially mark as TBD. Then we will discuss each of these points together and fill in the document as we go. - Project Overview - Architecture - Core components (API, Data, Service layers, configuration, etc) - Data Model, if the project has a database component - API endpoints, if the project exposes endpoints to be consumed - Technology stack (Language, frameworks, etc) - Project structure - Testing strategy, if the project uses unit or integration testing - Development commands (to build,Data Model, if the project has a database component - API endpoints, if the project exposes endpoints to be consumed - Technology stack (Language, frameworks, etc) - Project structure - Testing strategy, if the project uses unit or integration tests. - Development commands (for building, running, etc). - Environment setup (how the development environment is currently set up for the project) - Development guidelines (rules to follow when modifying the project) - Security considerations (things to keep in mind that are security-focused when modifying the project) - Future considerations (things that we may not be adding right away but would be candidates for future versions)

We will BUILD a file called TASK.md which lives in the project's root directory. The objective is to give you important context about what tasks have been accomplished, and what work is left to do. READ the PLANNING.md file, then create a list of tasks that you think should be accomplished. Categorize them appropriately (e.g. Setup, Core Functionality, etc). The last category will be "Completed Work" where we will have a log of work that has been completed, although initially this will be empty.
fix.md

This is my generic message when I have an error that I want it to fix.

READ the output from the terminal command to understand the error that is being displayed.
THEN FIX the error. Use `context7` and `brave-search` MCPs to understand the error.
THEN re-run the command in the terminal. If there is another error, repeat this debugging process.
code-review.md # Code Reviewer Assistant for Claude Code

    You are an expert code reviewer tasked with analyzing a codebase and providing actionable feedback. Your primary responsibilities are:

    ## Core Review Process

    1. **Analyze the codebase structure** - Understand the project architecture, technologies used, and coding patterns
    2. **Identify issues and improvements** across these categories:
       - **Security vulnerabilities** and potential attack vectors
       - **Performance bottlenecks** and optimization opportunities
       - **Code quality issues** (readability, maintainability, complexity)
       - **Best practices violations** for the specific language/framework
       - **Bug risks** and potential runtime errors
       - **Architecture concerns** and design pattern improvements
       - **Testing gaps** and test quality issues
       - **Documentation deficiencies**

    3. **Prioritize findings** using this severity scale:
       - 🔴 **Critical**: Security vulnerabilities, breaking bugs, major performance issues
       - 🟠 **High**: Significant code quality issues, architectural problems
       - 🟡 **Medium**: Minor bugs, style inconsistencies, missing tests
       - 🟢 **Low**: Documentation improvements, minor optimizations

    ## TASK.md Management

    Always read the existing TASK.md file first. Then update it by:

    ### Adding New Tasks
    - Append new review findings to the appropriate priority sections
    - Use clear, actionable task descriptions
    - Include file paths and line numbers where relevant
    - Reference specific code snippets when helpful

    ### Task Format
    ```markdown
    ## 🔴 Critical Priority
    - [ ] **[SECURITY]** Fix SQL injection vulnerability in `src/auth/login.js:45-52`
    - [ ] **[BUG]** Handle null pointer exception in `utils/parser.js:120`

    ## 🟠 High Priority
    - [ ] **[REFACTOR]** Extract complex validation logic from `UserController.js` into separate service
    - [ ] **[PERFORMANCE]** Optimize database queries in `reports/generator.js`

    ## 🟡 Medium Priority
    - [ ] **[TESTING]** Add unit tests for `PaymentProcessor` class
    - [ ] **[STYLE]** Consistent error handling patterns across API endpoints

    ## 🟢 Low Priority
    - [ ] **[DOCS]** Add JSDoc comments to public API methods
    - [ ] **[CLEANUP]** Remove unused imports in `components/` directory
    ```

    ### Maintaining Existing Tasks
    - Don't duplicate existing tasks
    - Mark completed items you can verify as `[x]`
    - Update or clarify existing task descriptions if needed

    ## Review Guidelines

    ### Be Specific and Actionable
    - ✅ "Extract the 50-line validation function in `UserService.js:120-170` into a separate `ValidationService` class"
    - ❌ "Code is too complex"

    ### Include Context
    - Explain *why* something needs to be changed
    - Suggest specific solutions or alternatives
    - Reference relevant documentation or best practices

    ### Focus on Impact
    - Prioritize issues that affect security, performance, or maintainability
    - Consider the effort-to-benefit ratio of suggestions

    ### Language/Framework Specific Checks
    - Apply appropriate linting rules and conventions
    - Check for framework-specific anti-patterns
    - Validate dependency usage and versions

    ## Output Format

    Provide a summary of your review findings, then show the updated TASK.md content. Structure your response as:

    1. **Review Summary** - High-level overview of findings
    2. **Key Issues Found** - Brief list of most important problems
    3. **Updated TASK.md** - The complete updated file content

    ## Commands to Execute

    When invoked, you should:
    1. Scan the entire codebase for issues
    2. Read the current TASK.md file
    3. Analyze and categorize all findings
    4. Update TASK.md with new actionable tasks
    5. Provide a comprehensive review summary

    Focus on being thorough but practical - aim for improvements that will genuinely make the codebase more secure, performant, and maintainable.

PLEASE share yours, or critique mine on how they can be better!!

## Top comments

### u/apf6 · score 23

I wrote this one that helps me find good website domain names:

Domain name search command:

You're going to generate ideas for a new domain name and use the 'whois' command
to check if they are available.

Your steps:

1. Ask the user to provide their goals or name ideas for the new domain name.
2. Generate a list of candidate ideas for their domain name. Aim to generate about 200
   ideas and write them down into ideas.md.
   - A good domain name is:
     - Not too long (less than 12 characters unless there's a very good reason to make it longer)
     - Catchy, easy to remember and say. Not too many words.
     - Your candidate ideas should have about 75% using .com suffixes and 25% using alternate suffixes
       like .net, .biz, .io, .co, etc. Alternate suffixes should only be used when they make sense for the product
       and they fit well with the name.
3. For each idea, run `whois` to check if the name is actually available. Ignore names that are not
   available.
4. Finally, compile a ranked list of the best available names. Save this to ideas.md.

Next up, ask the user for more information!

### u/Excellent_Entry6564 · score 8

Before committing, I copy the diff and paste it in a new chat then use this prompt:

Based on the above diff and reading any relevant files, pls do the following:

Review the diff to check for problems and bugs

Check if the tasks marked completed [x] and status updates in the diff for tasks.md have indeed been completed. Report any that have not been completed but were marked erroneously as completed

Check if our implementation and tests are aligned with our documentation in a.md b.md c.md

Report if any functionality/logic was removed

Check if tests are proper and complete. Report if any are placeholders or bypass assertions

Report if any test has become misaligned from what it was before

Report if functionality/coverage of tests was reduced

Raise any concerns/recommendations

### u/Worried_Clothes_8713 · score 5

For all code provided:

Code will be sent in an artifact with a unique handle, then updated rather than rewritten unless explicitly requested

Code will be sent one main controller function at a time (along with its nested components), in a unique artifact. These functions must have no placeholders or missing code, and ready to implement as written

Do not provide code unless I explicitly ask for code. Assume I want to chat about the implementation plan, unless you receive a specific command to write code

Code will always be written in Nested Model, View, Controller format:

Nested MVC:

Controller Nesting: Main Controllers contain sub-controllers, that coordinate Model and View responsibilities

Sub-task Nesting: If a function is called only one time, it should be nested inside of it's calling function. If a function needs to be called multiple times, it is not nested at all, but instead at the base level, in a group of "Shared Functions"

Non-Controllers are "Terminal": Every model or view function must be terminal (does not call other functions- if you need to call other functions, coordinate that with another layer of subcontrollers),

Semi-terminal Controllers are single layer: every controller that calls a model function directly, should only call model functions, while every controller that calls a view function directly, should only call view functions.

Here is an example of nested MVC: (Example is too long to paste here, but that’s the instructions)

### u/utherwayn · score 3

You're going to lose a lot of time fighting claude code's innate understanding of how to deal with CLAUDE.md files. It's really not that flexible. On top of that, the more complex your instructions get, the more chances you have of it ignoring parts of it, randomly. It's INCREDIBLY annoying. Outside of being really specific and detailed about what you want it to do it really isn't great and handling and breaking down high level tasks.

Ask me how I know.

### u/karandex · score 2

Simple question. Where should I put these files and make sure they are refereed. Cursor had rules folder.

### u/elelem-123 · score 2

"WORK!" This is my prompt and it does the job perfectly.

### u/sbayit · score 2

I have planned to use claude code with pro plan since it just announced with in Windsurf to save cost and avoid rate limit.

### u/zerdos · score 2

How do you go about creating a planning.md file when it’s an existing project? I want to be able to add new features to an old project and still be able to provide context to Claude.

### u/Spinozism · score 2

and also check this out https://github.com/hesreallyhim/awesome-claude-code whoa so much cool info, feel free to submit a PR even!

### u/MeButItsRandom · score 2

I'm going for a standard library of orchestration commands, using github issues, git history, and commit messages as the long term memory storage for claude

- add-claude-command.md - (bootstrapping command) creates a structured command based on my prompt
- create-gh-issue.md - (planning command) follows a study>thinking>planning>approval pattern to create new gh issues
- fix-gh-issued.md - (implementation command) follows a similar pattern to fix gh issues
- open-pr.md - instructions for opening a pr
- review-pr.md -
  etc
