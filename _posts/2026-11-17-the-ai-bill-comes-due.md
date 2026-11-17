---
title: 'The AI Bill Comes Due'
author: anjuan
layout: post
date: "2026-11-17"
permalink: /blog/the-ai-bill-comes-due/
categories:
  - Tech
excerpt: "Budget AI spend by team and by outcome instead of per engineer, and handle spending outliers with conversations instead of hard caps."
comments: true
image: "/images/the-ai-bill-comes-due.png"
---

{% include image.html url="/images/the-ai-bill-comes-due.png" alt="Graphic novel illustration of a man talking with an engineer beside a row of glowing utility meters." %}


Uber's CTO told The Information in April 2026 that [the company had burned through its entire planned 2026 AI coding budget in four months](https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets). As Forbes reported in May 2026, agentic coding use had climbed from 32% to 84% of roughly 5,000 engineers between February and March, with average spend reported at $150 to $250 per engineer per month and heavy users near $2,000.

Uber looks less like an outlier than an early arrival. In its Q2 2026 report, DX found that [median quarterly AI spend in its sample rose from about $1,500 to about $44,000 over four quarters](https://getdx.com/report/state-of-ai-impact-in-engineering-q2-report/). In August 2026, McKinsey found about [20% of organizations say token and operating costs have constrained their AI use](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai). And the FinOps Foundation's State of FinOps 2026 report, released in February 2026, found [98% of practitioners now manage AI spend, up from 31% two years earlier](https://data.finops.org/).

If you were around for the early years of cloud computing, this will feel familiar. Teams spun up servers because they could, the bill showed up a month later, and finance found a new line item nobody had forecast. A whole discipline grew out of that surprise. Token spend in 2026 looks a lot like cloud spend did then: real value, real waste, and very little visibility into which is which.

The tempting control is a cap per engineer. Stack Overflow's 2026 developer survey, published in October 2026, found 38% of organizations already use usage limits to control AI costs. I understand the appeal, because a cap is easy to explain and easy to enforce. However, I think cost per engineer is the wrong lens, and I learned a version of that lesson long before anyone bought a token.

Around 2012, I helped an oil major's learning and development group build a business case for managing its training content. What the client expected to get out of it was vague, and earlier tools hadn't worked out: one reinforced silos, and another made content hard to find. My first deck tied the client's own questions to business risks. When the client told me the risks were the story, I rebuilt the whole thing around one process, creating and managing courses, and its three biggest risks: weak search, ineffective collaboration, and weak compliance support.

That version finally showed what the money would buy. My senior manager wrote that the client agreed he now had what he needed to sell it to his own leadership. Then the client chose a quick fix on an intranet tool they already had, so there was no follow-on work for us. I still count it as a good outcome. Once the spend was tied to one process and its risks, the client could judge a cheaper option on the same terms, and it chose that one.

That's the question I'd bring to AI spend: what does the money buy, and could something cheaper buy the same thing?

So, here's how I'm thinking about AI budgets for 2027.

**Budget by team.** Teams have workloads, and some workloads (legacy migrations, giant test suites) burn more tokens for good reasons. A per-person cap punishes whoever drew the hardest work.

**Measure what the spend buys.** Cost per merged change or per resolved ticket tells you far more than cost per seat.

**Alert early, and review outliers in conversation.** When someone's usage spikes, talk to them before you cut them off. Sometimes your biggest spender is running the experiment that will teach the whole organization something. Sometimes they left an agent running all weekend. You won't know which until you ask.

**Re-check what you inherited.** AI coding tools have been moving from seat licenses to usage-based billing, so a budget built on seat counts may already be out of date.

A business case that points to the cheaper option is still a good business case.
