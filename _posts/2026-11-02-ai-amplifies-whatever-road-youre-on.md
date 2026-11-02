---
title: 'AI Amplifies Whatever Road You''re On'
author: anjuan
layout: post
date: "2027-10-05"
permalink: /blog/ai-amplifies-whatever-road-youre-on/
categories:
  - Tech
excerpt: "AI amplifies whatever foundation it lands on, so fund platform work like flags, rollouts, and health scores before chasing AI speed."
comments: false
---

{% include image.html url="/images/ai-amplifies-whatever-road-youre-on.png" alt="Graphic novel illustration of a man in a safety vest directing a steamroller paving a dirt road" %}


In July 2026, Perforce released a [platform engineering report](https://www.perforce.com/press-releases/state-of-platform-engineering-2026) based on 820 respondents. Among organizations with mature internal platforms, 73% said that maturity was critical or significant to their success with AI. Among less mature organizations, 44% said the same. In May 2026, InfoQ covered a [DORA report on the return from AI-assisted development](https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/) that made a similar argument: the gains depend more on the quality of your internal platform and the clarity of your workflows than on which tools you buy.

That's vendor research, and it shows correlation rather than cause. Still, it matches what I've seen.

AI is an amplifier. Put a bigger engine in a car on a paved road and you get where you're going sooner. Put the same engine in a car on a rutted dirt road and you find the ditch sooner, and you hit it harder. The engine did its job both times. The road decided your final destination.

I've worked on both kinds of road.

There have been a few times in my more than a quarter century career building software for a living where I inherited a dirt road of software systems and services. There was no common definition of service health, and each service had its own needs. If someone had pointed a fleet of coding agents at them on day one, we'd have gotten a lot of changes very quickly and no reliable way to tell whether any of them helped. We had to grade the road first.

The best paved road I've worked on is older than any of these tools. Over a decade ago, I was on the engineering team at a construction software company, and I managed the release schedule for a major release of its flagship estimating product. The release ran on two-week sprints with gates everyone could see: feature complete, code complete, an external beta, and a go or no-go meeting. Alongside it sat a readiness plan organized by division, from six weeks before release to after it, so training, marketing, sales, support, and accounting each had their own list. I owned one database readiness handoff myself. None of that is exciting. All of it is pavement, because it made "done" something people could check instead of argue about.

The Perforce numbers carry a warning, too. Two thirds of organizations said they use AI in infrastructure workflows, but only 31% run it fully autonomously, and only 52% have fully automated audit trails. Organizations with formal governance reported trust in AI far more often (94%) than those with an ad hoc approach (51%). That tracks with my experience. Trust comes from being able to see what happened and undo it. Flags, staged rollouts, audit trails, and shared health scores are how you see and undo things.

Here are two things to consider when planning your next AI investment.

Your platform team is already an AI enablement team, whether anyone has told them or not. They own the guardrails the AI depends on. If you're spending real money on AI tools while the platform team fights for headcount, you're buying a bigger engine for a dirt road.

Before your next rollout, pick one workflow you want to speed up and ask a few plain questions. Can we see what changed? Can we roll it back quickly? Do we have a shared definition of healthy for the thing it touches? If any answer is no, start there.

Fund the road first. The engine can wait a quarter.
