---
tags:
  - library
title: "Jules - An Asynchronous Coding Agent"
url: "https://jules.google/"
company: [personal]
topics: []
created: 2025-05-20
source_type: raindrop
raindrop_id: 1044775707
source_domain: "jules.google"
source_type_raindrop: link
collection: "AI Tools & News"
collection_id: 69284314
hydrated: true
hydrated_at: 2026-04-18
hydrated_via: jina-reader
---
## Excerpt

Jules is an asynchronous agent that gets out of your way. It lets you focus on the coding you want to do, meawnwhile picking up all the other random tasks that you rather not do.

## Raw Content

<!-- Hydrated 2026-04-18 via jina-reader -->

Title: Jules - An Autonomous Coding Agent

URL Source: https://jules.google/

Markdown Content:
# Jules - An Autonomous Coding Agent
# Jules - An Autonomous Coding Agent

[Plans](https://jules.google/#plans)[Try Jules](https://jules.google.com/)

# An Autonomous Coding Agent

![Image 1: Squid agent](https://jules.google/jules-pixelated.png)

1`// Objective: Change UserOnboarding to use a state machine for steps`

2``

3`class UserOnboarding {`

4`constructor(user) {`

5`this.user = user;`

6``

7`this.steps = ["welcome", "profile_setup", "preferences"];`

8``

9`this.currentStep = 0;`

10`}`

11``

12`async nextStep() {`

13`if (this.currentStep < this.steps.length -1) {`

14`this.currentStep++;`

15`// TODO: Trigger analytics`

16`return this.steps[this.currentStep];`

17`}`

18`return "done";`

19`}`

20``

21`// Old method - to be removed`

22`legacyNotification() {`

23`alert("Welcome aboard, " + this.user.name);`

24`}`

25`}`

26``

27`const newUser = { name: "David", id: "usr_123" };`

28`const onboardingProcess = new UserOnboarding(newUser);`

29``

30`onboardingProcess.nextStep();`

31`// onboardingProcess.legacyNotification(); // Commented out`

Jules does coding tasks you don't want to do.

Bug Fixing Version Bump Tests Fixing Jed's Code Feature Building

Jules does coding tasks you don't want to do.

Bug Fixing Version Bump Tests Fixing Jed's Code Feature Building

More time for the code you want to write, and everything else.

![Image 2: Writing software](https://jules.google/comic-computer.png)![Image 3: Bike riding](https://jules.google/comic-bike.png)![Image 4: Reading a book](https://jules.google/comic-book.png)![Image 5: Playing tennis](https://jules.google/comic-tennis.png)

Brought to life with Gemini 3 Pro and the AIDA team.

![Image 6: Squid](https://jules.google/squid.png)

**GitHub Integration**
Jules imports your repos, branches changes, and helps you create a PR.

**Test Suite**
Jules will run existing tests, or create new ones.

**Virtual Machine**
Jules clones your code in a Cloud VM and verifies the changes work.

**Available Anywhere**
Use Jules from the [CLI](https://jules.google/docs/cli/reference) or build your own workflows using the [API](https://developers.google.com/jules/api)

1

Select your GitHub repository and branch. Write a detailed prompt for Jules.

Use the "jules" label in an issue to assign a task directly in GitHub.

@kathy/flipdisc main

Can you bump the version of next.js to v15 and convert the project to use app directory?

2

Jules fetches your repository, clones it to a Cloud VM, and develops a plan utilizing the latest [Gemini 3 Pro model](https://deepmind.google/technologies/gemini/pro/).

![Image 7: Jules Avatar](https://jules.google/jules-avatar-profile.png)

Here is my plan:

I plan to update the following files to the new app directory structure.

Update 22 Files

That looks good. Continue!

![Image 8: Your Avatar](https://jules.google/you-avatar.png)

3

Jules provides a diff of the changes. Quickly browse and approve code edits.

 

9 

10`"dependencies": {`

11-`"next": "10.2.3",`

11+`"next": "15.4.5",`

12`"react": "19.1.1",`

13`"react-dom": "19.1.1"`

14`}`

4

Jules creates a PR of the changes. Approve the PR, merge it to your branch, and publish it on GitHub.

Publish Branch

Find the Jules plan that fits your workflow

Jules scales with how you build, from quick fixes to fully async, multi-agent development. Choose the plan that gives you the speed, throughput, and model access you need.

**Jules ![Image 9](https://jules.google/plan-01.png)![Image 10](https://jules.google/plan-01.png)**
Get started with real coding tasks.

*   15 tasks per day
*   3 concurrent tasks
*   Powered by Gemini 2.5 Pro

**Jules in Pro![Image 11](https://jules.google/plan-02.png)![Image 12](https://jules.google/plan-02.gif)**
For devs who ship daily and want to stay in the flow.

*   100 tasks per day, enough to run Jules throughout your coding day
*   15 concurrent tasks, so you can run multiple threads in parallel
*   Higher access to the latest models, starting with Gemini 3 Pro

**Jules in Ultra![Image 13](https://jules.google/plan-03.png)![Image 14](https://jules.google/plan-03.gif)**
For builders who run agents at scale.

*   300 tasks per day to handle the most demanding development cycles
*   60 concurrent tasks, built for massively parallel workflows
*   Priority access to the latest models, starting with Gemini 3 Pro

[Try Jules](https://jules.google.com/)[Documentation](https://jules.google/docs)

[](https://labs.google.com/)
*   [Terms of Service](https://policies.google.com/terms)
*   [Privacy Policy](https://policies.google.com/privacy)
