---
title: "How Can You Contribute?¶"
source_url: "https://scs.owasp.org/contributing/1_How_Can_You_Contribute/"
host: "scs.owasp.org"
depth: 1
selector: "article,main,[role=main]"
fetched_at: "2026-10-24T02:29:39.933Z"
---
[](https://github.com/OWASP/www-project-smart-contract-security-testing-guide/edit/master/contributing/1_How_Can_You_Contribute.md "Edit this page")

# How Can You Contribute?[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#how-can-you-contribute "Permanent link")

You can directly contribute to the SCSVS or SCSTG in many different ways! First, go ahead and create a GitHub account for free on the [GitHub homepage](https://github.com/).

## Contribution Flow[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#contribution-flow "Permanent link")

```
flowchart LR
    A(Open Discussion) -->|discuss| C{qualifies?}
    C -->|Yes| D(Issue)
    C -->|No| E[Close]
    D -->|open PR| F(Pull Request)
    F -->|review| G{approved?}
    F -->|make changes| F
    G -->|Yes| H[Merge]
    G -->|No| I[Close]
```

## 💬 Participate in Discussions[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#participate-in-discussions "Permanent link")

Our GitHub [issue tracker](https://github.com/OWASP/owasp-scs/issues) is the first place to ask questions, give feedback, and propose new ideas. If a proposal belongs in the SCSTG or SCSVS, maintainers will triage it into the appropriate project workflow.

## 🎯 Create Issues[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#create-issues "Permanent link")

Before creating a PR, first create an [Issue](https://github.com/OWASP/owasp-scs/issues "SCS Issues") to be discussed for missing requirements, content or errors.

-   To avoid multiple people duplicating effort on the same issue, project leaders will assign it to only a few that will own it.
-   Explain what you think is missing in the issue, including references (if available) and suggest where it could be added.

## 📝 Open a Pull Request[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#open-a-pull-request "Permanent link")

You can contribute with content or corrections by opening a Pull Request (PR).

-   Your PR may be merged after review.
-   Be sure to follow our [style guide](https://scs.owasp.org/contributing/5_Style_Guide/) when writing content.

> Learn how to open a PR [here](https://scs.owasp.org/contributing/3_PRs_and_Reviews/#how-to-open-a-pr).

## ✅ Become a Reviewer[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#become-a-reviewer "Permanent link")

You can [Review Pull Requests (PRs)](https://github.com/OWASP/www-project-smart-contract-security-verification-standard/pulls) and also gain contributions. If you are a fluent speaker in any of the different languages that the SCSVS is available in, feel free to give feedback on any of the submitted PRs.

After your PR or issue has been submitted, we will review it as quickly as possible which typically only takes a few days. If you think we have forgotten about it, feel free to give us a nudge after 7 days have passed.

> Learn how to review a PR [here](https://scs.owasp.org/contributing/3_PRs_and_Reviews/#how-to-review-a-pr).

## 🔎 Proof-reading[¶](https://scs.owasp.org/contributing/1_How_Can_You_Contribute/#proof-reading "Permanent link")

If you do proof-reading, these are the things we’re looking for:

-   Content [cohesion & coherence](https://writing.chalmers.se/chalmers-writing-guide/writing-a-text/coherence-cohesion/)
    -   is there a good linkage of ideas?
    -   does the paragraph make sense?
    -   does it make sense with the next one? Think that hundreds of people have written in here, often without considering the surroundings of the text they were including.
-   Reducing the content to a minimum (people tend to be very verbose/wordy) and in such a document we need clear and short/concise statements
-   Optimize for *scannability* (maybe instead of a big paragraph it would be better to have a bullet point list).
-   Any passive voice sentences? Convert to active voice.
-   Does each paragraph focus on a single topic?
-   Are key points stated at the start of each section?
-   Are commas, parentheses, colons, em-dashes, and semicolons used properly?

Refer to Google Technical Writing trainings for more info:

-   [Google Technical Writing One](https://developers.google.com/tech-writing/one)
-   [Google Technical Writing Two](https://developers.google.com/tech-writing/two)
