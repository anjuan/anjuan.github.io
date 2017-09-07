---
title: 'Why Small is the Key to Big Agile Results'
author: anjuan
layout: post
date: "2016-07-21"
permalink: /blog/why-smaill-is-the-key-to-big-agile-results/
categories:
  - Software Development
excerpt: "Software development efforts often try to quickly scale resources in order to speed the pace of development. Hoewever, taking a small approach can often yield better results."
---

{% include image.html url="/images/post-small-key-big-agile.jpeg" alt="Hummingbird" caption="Big results can come from small things. (Pexels)" width=400 align="right" %}

It’s tempting to solve software application performance problems by throwing hardware at the problem. Since machines are relatively cheap, horizontally scaling by adding more servers is a common initial remedy. However, this soon runs into diminishing results since large numbers of machines can’t optimize code.

The same principle applies to Agile software development teams. Since the market can provide nearly unlimited sources of programming talent, hiring more developers is a common remedy for solving the perception that not enough work is getting done. However, a large number of developers can’t optimize the work that flows through the Development Team simply through numeric strength.

Contrary to what most people would intuitively think, taking a small approach to software development can increase the amount of work that can be completed by an Agile software development team, especially those that practice Scrum. This requires understanding the concepts of small teams, small releases, and small vertical slices.

## Small Teams

I’ve seen Scrum Teams with 20 or more developers, and my first instinct is always to break them up into smaller Scrum Teams. Scrum recommends that the Development Team should be between 3 and 9 people. If a Development Team has less than 3 people, then it may be difficult to have all of the skills needed to complete the potentially shippable product increment by the end of the sprint. If a Development Team has more than 9 people, then coordination costs begin to dramatically rise.

Let’s say you have one Scrum Master, one Product Owner, and five Development Team members. That is a total of seven people on the Scrum Team. The number of communication channels for this seven person team can be calculated using the formula `n(n-1)/2` where n is the number of people on the team. Using this formula, we can determine that there are 21 communication channels. However, adding more people to the team dramatically increases the number of communication channels:


| Team Members | Communication Channels |
| ------------ | ---------------------- |
|  8           |       28               |
|  9           |       36               |
| 10	         |       45               | 
| 11	         |       55               |
| 12           |       66               |
| 13           |       78               |
| 14	         |       91               |
| 15	         |      105               |
| 16	         |      120               | 
| 17	         |      136               |
| 18	         |      153               |
| 19	         |      171               |
| 20	         |      190               |



For example, if three people are added to the seven person Scrum team (a 30% increase in team size), you more than double the number of communication channels. If you double the seven person Scrum Team to 14 people, you more than quadruple the number of communication channels.

Small teams are better positioned to efficiently and effectively manage Scrum events like Sprint Planning, the Daily Standups, the Sprint Review, and the Sprint Retrospective. Having a small team size increases the likelihood the team communication is focused and fast decisions can be made.

Since Agile teams thrive in an environment with co-located teams that interact through face-to-face contact and regularly reflect with each other, Development Teams with more than nine people can’t communicate effectively enough to maximize their agility.

## Small Releases

It can be tempting to drive a software development team to deliver big releases chock full of awesome features. However, small releases with a small set of features provide benefits to both the team and to customers.

When a team considers which items to pull into the Sprint Backlog from the Product Backlog during Sprint Planning, small features (we call them user stories) are essential. Small user stories are easier for the team to understand because the work is specific and granular. This simplifies the process of determining the effort needed to complete each feature by the Development Team. Small user stories reduce the difficulty of determining the complexity, risk, and size of features by lowering uncertainty. The Product Owner and Development Team can quickly obtain a shared understanding of the work and produce accurate estimates. Furthermore, smaller user stories allow Development Teams to feel an almost daily sense of progress as they finish features throughout the execution of the sprint.

When a small set of features are delivered to customers, they are better able to understand the delivered software and provide feedback. Give a user ten complicated features and they’ll delay giving you feedback for as long as possible. However, give a user three simple features, and you’ll get feedback before you return from your coffee break. The human mind can only process so much information at once, and we delay analyzing large data sets when we can get away with it. You can confirm this by simply checking the number of unread emails in your inbox.

## Small Vertical Slices

Developers often think of applications in terms of horizontal layers, and they often build software layer by layer. For example, developers will often build the entire back end database for a release, then the application logic, and then the user interface. It’s not uncommon for Development Teams that take this approach to finish a sprint with one layer “Done”. However, this is not a working product increment. How can a back end database be discussed during a Sprint Review? How can a user interface, no matter how elegant, be shown in a demo if it doesn’t work? Furthermore, delivering these layers separately from each other hinders the ability for upper layers to teach you about the lower layers. For example, if the back end database is fully developed before the user interface is started, then problems that can only be detected by the UI can result in the need to rebuild the database.

A better approach is to think of applications in terms of features composed of vertical slices that each have a data, logic, and presentation layer. Therefore, working on Feature X means creating the database tables, business logic, and user interface for Feature X. This greatly increases the chance that Feature X will be working by the time of the Sprint Review and can be verified by the Product Owner. By building out an application vertical slice by vertical slice, the Development Team can deliver features faster and learn things from early vertical slices that can be applied to future vertical slices.

## Conclusion

The next time you spin up an Agile software development team or try to improve an existing one, consider taking a small approach. Seek to create a small team that delivers small features in small vertical slices. You may be surprised by the size of the results.
