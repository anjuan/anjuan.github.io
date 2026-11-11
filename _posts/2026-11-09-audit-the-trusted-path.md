---
title: 'Audit the Trusted Path'
author: anjuan
layout: post
date: "2026-11-09"
permalink: /blog/audit-the-trusted-path/
categories:
  - Tech
excerpt: "The paths we trust most get audited least, so leaders should design systems that stay safe even when a trusted person or pipeline is compromised."
comments: false
image: "/images/audit-the-trusted-path.png"
---

{% include image.html url="/images/audit-the-trusted-path.png" alt="Graphic novel illustration of a man with a flashlight inspecting a glowing service corridor behind a vault door." %}


Attackers have always known that the fastest way into an organization runs through someone it already trusts. You don't have to pick a lock if a person with the key will open the door for you. That person might be a junior engineer, a maintainer, or a senior leader with access to everything.

What's changed is how many new doors we keep adding, and how rarely we go back to check them.

On May 11, 2026, TanStack, a popular family of JavaScript libraries, had 84 malicious versions published across 42 of its npm packages in about six minutes. According to [TanStack's own postmortem](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem), the attacker never got malicious code into the main branch. Instead, they opened a pull request from a fork that triggered a workflow with more privilege than it should have had. That workflow saved a poisoned cache. Roughly eight hours later, a legitimate release restored the cache, and the malicious code pulled a publishing token out of the build runner's memory. Because the packages came out of TanStack's real pipeline, they carried valid provenance.

The part I keep coming back to is in TanStack's list of lessons. They had no internal alerting, and they found out from an outside researcher about 26 minutes after the first publish. The risky workflows had never been audited. Nobody did anything reckless. A trusted path picked up a new exposure, and nothing was watching it.

I've seen the people version of this more than once.

Over a decade ago, I worked on the remediation plan after a large bank ran a four-day onsite security assessment of a client's application that ran on our platform. The report came back with nearly a hundred findings. Most were what you'd expect, like privileged accounts that weren't separated from everyday accounts and weren't logged and reviewed. One finding said that data loss alerts went to a single person, and "if that person goes rogue," a breach could go unnoticed. This was a critical design flaw. Any control that depends on one person staying trustworthy forever is really just hope.

A few years before that, the delivery manager on a program I was part of sent the whole engagement team a warning about emailing internal documents to personal accounts. While none of my direct reports had done this, it was eventually discovered that a few new members of another vendor's team hadn't been given company email addresses. Since their laptops had USB ports disabled, they worked around the gap by using their personal email accounts to transfer client information. This breach wasn't due to malicious intent. They were trying to get things done while dealing with a lack of essential access. 

So, how do you protect a system from exposures you haven't seen yet? Here's what I'd put on a leader's list.

**Make accountability apply upward.** The higher someone sits, the more access they tend to have and the fewer people feel comfortable questioning it. Leaders should follow the same access rules, reviews, and reporting expectations as everyone else, and they should say so out loud. If a policy has an executive exception, attackers will find it before your auditors do.

**Audit on a schedule, and again whenever something new arrives.** Annual reviews catch drift. However, new exposures show up when something changes, like a new workflow, a new vendor, a new tool with broad permissions, or a new relationship that touches sensitive work. Treat each of those as a trigger for a fresh look, not something to catch next year.

**Never let one person be the only alarm.** Alerts, approvals, and logs of privileged activity should reach more than one person, and ideally more than one team. Two-person review for the riskiest actions isn't a sign of distrust. It protects the trusted person, too.

**Make it easy to rotate and revoke.** On one of my past engineering teams, we moved our service's secrets into a team-managed vault so we could rotate them ourselves during a security incident. Before that, we would have had to find the one person with access to the shared vault. Speed matters a lot when something is compromised, and you don't want it to depend on who's awake.

**Watch your own front door.** TanStack learned about its compromise from someone else. Monitor what your pipelines publish and what your most privileged accounts do, so you're not the last to know.

**Make it safe to raise a concern.** People often notice something odd long before it becomes an incident. They need a clear, safe way to say so, especially when the concern involves someone senior. If the only way to report a problem is to go through the person involved, you don't really have a way to report it.

**Fix the process that made the workaround necessary.** When people bend a rule, ask what the system failed to give them. The team emailing documents to personal accounts needed working company accounts, not just a sternly worded warning.

None of this assumes the people around you are untrustworthy. Most of them are exactly who they seem to be. It assumes that anyone can be targeted, fooled, or pressured, including the people with the most access. Good systems are designed so that one bad day, one clever attacker, or one poisoned cache doesn't become everyone's problem.

You need to find out the last time you audited the access you trust the most.
