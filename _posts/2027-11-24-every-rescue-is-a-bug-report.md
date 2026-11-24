---
title: 'Every Rescue Is a Bug Report'
author: anjuan
layout: post
date: "2027-09-23"
permalink: /blog/every-rescue-is-a-bug-report/
categories:
  - Tech
excerpt: "Every heroic rescue points to a missing process, so fix the customer's problem first and then fund the fix that prevents the next one."
comments: false
image: "/images/every-rescue-is-a-bug-report.png"
---

{% include image.html url="/images/every-rescue-is-a-bug-report.png" alt="Graphic novel illustration of a man with blueprints shaking hands with a firefighter in a firehouse" %}


Nothing gets a customer's attention like the same email arriving about every ten seconds. I know because my team's code sent them.

It came from an integration with an outside partner's platform. A small change to how a background job paged through data made the job cancel and recreate the same records over and over, and every recreation sent the customer an email. The code change was tiny. The effect in people's inboxes was not.

Stopping the emails was the first job. Then I led the learning review, which is where the real work happened. We asked how a small change got that loud and what would keep the next one quiet. We put the job's behavior behind a feature flag. We rate-limited the emails, so a bug like that couldn't flood an inbox the same way. And we started requiring more than one reviewer on changes like that one. A second reviewer costs a few minutes per change. Next to a customer's inbox filling up every ten seconds, that's cheap insurance. None of those fixes would make a good war story, which is exactly why I like them.

I think about that review whenever someone gets praised for heroics.

Firefighters are heroes, and I mean that. However, a city doesn't measure fire safety by how many daring rescues happen in a year. It measures it by how few fires there are, and the reason there are fewer fires is building codes, sprinklers, and inspections. A rescue is what you need when prevention didn't happen. If your fire department is pulling people out of buildings every week, you need better building codes more than braver firefighters.

Software teams love a rescue story. Somebody stays up late, restores the data, saves the launch, and gets a shout-out at the all-hands. I've told those stories myself. The trouble is that rescues are fun to tell and easy to reward, so organizations quietly start depending on them. I've learned that every heroic rescue is a bug report about a missing process.

Here's a rescue I'm glad we turned into a process. Some large customers changed a setting and then changed it back, and in the process they lost data their communities cared about. My team ran the restorations for two groups of customers. One of them needed its data back before a major industry event, and that customer's leadership thanked the team.

That could have been the end of it. However, it had already happened twice, and nothing about the underlying problem had changed. So, I asked a senior engineer to compare the alternatives. Product chose prevention, and the engineer wrote the design document for an automatic recovery mechanism, which was finished the next year. I like it when the person closest to the fix gets to write the prevention. Nobody understands the pain better.

To be clear, my role there was mostly oversight. The engineers did the hard parts. My job was to make sure the rescue didn't turn into a habit.

If your team gets praised for rescues, start here. Fix the customer's problem before you fix the system. People in pain don't want to hear about your roadmap. Get them whole, then ask why it happened. Also, whenever you praise a rescue, ask the follow-up question in the same breath: what would have made this unnecessary? Fund the answer.

Thank the firefighters. Then go write the building code.
