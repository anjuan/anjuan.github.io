---
title: 'Setting Up a Custom Google Domain for GitHub Pages'
author: anjuan
layout: post
date: "2017-09-05"
permalink: /blog/setting-up-a-custom-google-domain-for-github-pages/
categories:
  - Site Log
excerpt: "Setting up a custom Google domain to use with GitHub Pages is straightforward, but there are a frew tricky steps. Here is how I did it for this site."
---

https://help.github.com/articles/setting-up-an-apex-domain-and-www-subdomain/

I have understood the importance of owning your own space on the internet for a long time, and I registered *AnjuanSimmons.com* many years ago. This domain has changed domain registrars a few times from [Yahoo Small Business](https://smallbusiness.yahoo.com/) in the early days to several years with [GoDaddy](https://www.godaddy.com/) and now with [Google Domains](https://domains.google/#/). I use several Google products and services, and the company also has an image that I'm comfortable using as the provider of URL that holds my name. I was also confident that Google Domains would be reliable, easy to use, and cost effective. This turned out to be true, by the way.

Just as *AnjuanSimmons.com* has changed registrars over the years, it has also changed hosts. I used Yahoo Small Business as my host when I used their domain service, but, when I moved over to GoDaddy, I decided to change my host, too. Actually, I changed my host several times. I initially used a [self-hosted WordPress](https://wordpress.org/download/) installation, then moved to [Squarespace](https://www.squarespace.com/), and then I tried [Google Sites](https://sites.google.com). I really liked Google Sites because it was very simple to use. However, I eventually began to want more control over my site, and, I began looking a other alternatives. I was a speaker at [GitHub Universe 2016](https://githubuniverse.com), and I really liked what I learned about [Jekyll](https://jekyllrb.com/) and [GitHub Pages](https://pages.github.com/) at the conference. So, I decided to move from Google Sites to GitHub Pages.

However, I wanted to keep my URL registred with Google Domains. Years can go by between changes in my hosting, and I usually stumple through pointing my domain to a new host. So, I'm writing this post to remind myself of how I did it and, hopefully, provide another person with an easy set of instructions for doing it.


## Register with Google Domains

Since this guide assumes you're using Google Domains as your registrar, you need to be registered with that provider. 

## Configure GitHub Pages - CNAME

TBD

## Configure Google Domains - Create Apex Domain

TBD

## Configure Google Domains - Create Subdomain

I then went into "edit mode" and modified the fork to suit my need. I modifed the `menu.yml` file in the `_data` folder to match my preferred names for the menu items. I then modified the referenced folders and files and began changing the template to represent the pages that I wanted. 

## Confirm Custom Domain Configuration in GitHub Pages

TBD
