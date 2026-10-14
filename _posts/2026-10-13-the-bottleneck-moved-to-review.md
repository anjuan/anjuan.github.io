---
title: 'The Bottleneck Moved to Review'
author: anjuan
layout: post
date: "2026-10-13"
permalink: /blog/the-bottleneck-moved-to-review/
categories:
  - Tech
  - Leadership
excerpt: "Agents made writing code faster, so the bottleneck moved to review, and leaders should plan around review capacity instead of coding capacity."
comments: false
---

{% include image.html url="/images/the-bottleneck-moved-to-review.png" alt="Graphic novel illustration of a man at a restaurant pass checking plates as dishes pile up under heat lamps." %}

In July 2026, DX's quarterly study of more than 500 organizations reported that AI wrote 52% of their code in the second quarter, up from 34% in the first. The same report found that the median pull request had nearly doubled in size. Then, in October 2026, the Stack Overflow developer survey found that 66% of developers who use AI now work with coding agents.

So, more code, in bigger chunks, arriving faster. That sounds like a win until you ask where it all goes next.

It goes to review. And review is still mostly done by people, at roughly the speed people have always read code.

Restaurant kitchens have lived with this problem forever. Most busy kitchens have someone at the pass, the counter between the cooks and the dining room, who checks every plate before it goes out. If the owner hires three more line cooks and leaves one person at the pass, the restaurant serves the same number of customers, with a growing stack of plates under the heat lamps. The cooks feel productive. The diners still wait. (And the person at the pass starts updating their resume.)

A faster machine upstream of a slow one just builds inventory. Agents made the cooks faster, and most teams haven't added anyone at the pass.

I've seen a smaller version of this long before agents. Around 2016, I was the agile project manager at a small startup, and in one retrospective I wrote, "We carry potentially done work for several days because it is locked in a large user story... We need to get better at slicing stories." The code was written. It just couldn't move, because it was tied up with work that wasn't finished. Big stories hid finished work. Big pull requests do the same thing, except an agent can now produce one in an afternoon.

On that same team, when I wrote the release plan for the months after our platform went generally available, I reserved the back half of each release's last sprint for a final acceptance test pass. I thought of that time as the plan admitting that checking work takes real capacity, and capacity has to be scheduled like anything else.

That's the shift I'd ask delivery leaders to make. Stop managing the keyboard and start managing the review queue.

Start by looking. How long do pull requests wait for a first review, and how big are they when they get there? Most teams can pull that data in an hour. When LeadDev surveyed about 600 engineering leaders for its 2026 engineering leadership report, only 21% said they track time spent reviewing AI-generated code. If you're in the other 79%, that's your first project.

Then plan sprints around review capacity instead of coding capacity. If an agent can draft three tickets overnight, the useful question in sprint planning becomes how much the team can carefully read, test, and own.

Keep the batches small. DORA has recommended small batches as a way to reduce the delivery instability that comes with AI-assisted work, and that advice is older than any agent. Ask for smaller pull requests even when the agent could happily write a bigger one. Thin slices were good advice in 2016. They're better advice now.

Finally, protect your reviewers. The people who review the most code tend to be your senior engineers, and they're also the ones you need for design work and incidents. If review has become the main job, say so out loud, and give it the time and credit it deserves.

I like the new cooks. I'd just like someone watching the pass before the food goes cold.
