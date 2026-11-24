---
title: 'Every Rescue Is a Bug Report'
author: anjuan
layout: post
date: "2026-11-24"
permalink: /blog/every-rescue-is-a-bug-report/
categories:
  - Tech
excerpt: "Every heroic rescue points to a missing process, so fix the customer's problem first and then fund the fix that prevents the next one."
comments: true
image: "/images/every-rescue-is-a-bug-report.png"
---

{% include image.html url="/images/every-rescue-is-a-bug-report.png" alt="Graphic novel illustration of a man with blueprints shaking hands with a firefighter in a firehouse" %}

Nothing gets a customer's attention like the same email arriving about every ten seconds. I know because my team's code sent them.

It came from an integration with an outside partner's platform. A small change to how a background job parsed data made the job cancel and recreate the same records over and over, and every recreation sent the customer an email. The code change was tiny. The effect in people's inboxes was not.

I made stopping the emails the first priority. I then led the learning review, which is where the real work happened. We asked how a small change got that loud and what would keep the next one quiet. We put the job's behavior behind a feature flag and rate-limited the emails, so a bug like that couldn't flood an inbox the same way. We also started requiring more than one reviewer on changes that are so close to the every day lives of our customers like notifications. A second reviewer costs a few minutes per change. That's a cheap insurance policy compared with filling up a customer's inbox every ten seconds. None of those fixes would make a good war story, which is exactly they are so important to share.

I think about that learning review whenever someone gets praised for heroics.

Firefighters are heroes in the truest sense of the word. However, a city doesn't measure fire safety by how many daring rescues happen in a year. It measures safety by how few fires there are, and the reason there are fewer fires is building codes, sprinklers, and inspections. A rescue is what you need when prevention didn't happen. If your fire department is pulling people out of buildings every week, you need better building codes more than braver firefighters.

Software teams love a good rescue story. Somebody stays up late, restores the data, saves the launch, and gets a shout-out at the all-hands. I've told those stories myself. The trouble is that rescues are fun to tell and easy to reward, so organizations quietly start depending on them. I've learned that every heroic rescue is a bug report about a missing process.

Here's another rescue I'm glad we turned into a process. Some large customers changed a setting that wiped out information that was extremely important to their communities. An engineer on my team ran the restorations for those customers. One of them needed its data back before a major industry event, and that customer's leadership thanked the company for restoring the data before the deadline.

That could have been the end of it. However, customers had already made this mistake before, and nothing about the underlying problem had changed. So, I asked the engineer who restored the data to look at ways for solving this for all of our customers. They came up with a design for an automatic recovery mechanism, which was finished and rolled out to everyone . I like it when the person closest to the fix gets to write the prevention. Nobody understands the pain better.

To be clear, my role there was mostly management, oversight, and flying the flag of customer obsession. The engineer did the hard part. My job was to make sure the rescue didn't turn into a habit.

If your team gets praised for rescues, that's a great place to start. Fix the customer's problem before you fix the system. People in pain don't want to hear about your roadmap. Get them whole, then ask why it happened. Also, whenever you praise a rescue, ask the follow-up question in the same breath: what would have made this unnecessary? Fund the answer.

The firefighters in your organization deserve you thanks, but what they need are better building codes.
