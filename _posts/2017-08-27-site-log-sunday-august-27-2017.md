---
title: 'Site Log - Sunday, August 27, 2017'
author: anjuan
layout: post
date: "2017-08-27"
permalink:
categories:
  - Site Log
excerpt: "This is a high-level log of what I've done with the site as of Sunday, August 27, 2017."
---

This is the first post in an irregularly scheduled series of the work I'm doing building out this site. This site is my personal repository of my content on the internet, but it's also an expression of what I've learned using Jeklyll to create a website. That includes learning more about GitHub, Markdown, HTML, CSS, and other tech topics.

Here is what I've done to bring the site it's current version.

## Choosing a Template

I had an idea of what I wanted based on the layout I personally like when viewing websites. Generally, I like a top navigation scheme with a lightweight design. I did a google search for `jekyll themes` and found the descriptively named [Jekyll Themes](http://jekyllthemes.org/) site.

I browsed several pages of this site until I settled on two options: [Moon](http://jekyllthemes.org/themes/moon/) by Taylan Tati and [Steve's NGVB (No-Good-Very-Bad) Theme](http://jekyllthemes.org/themes/svm-ngvb/) by Steven V. Miller. The Jekyll Themes site lets you look at the source of the templates in GitHub as well as demo a working version. The Moon theme had a very snazzy design, but I liked the straight-forward design of Steven's theme. Steven's theme was also structured simiarly to the version of my site hosted on Google Sites. 

## Fork

Steven's theme also had the benefit of being laid out from a directory perspective in a way that I could understand. Unlike a lot of Jekyll based sites hosted on GitHub, I was able to easily understand his folder names and the conventions he used for his Markdown files. I forked Steven's [template](https://github.com/svmiller/steve-ngvb-jekyll-template) into my own GitHub repository.

## Edit

I then went into "edit mode" and modified the fork to suit my need. I modifed the `menu.yml` file in the `_data` folder to match my preferred names for the menu items. I then modified the referenced folders and files and began changing the template to represent the pages that I wanted. 

## Detach

I eventually realized that the commits I made on my repository weren't showing up as GitHub contributions. I looked at how [GitHub counts contributions](https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile/) and saw the following conditons must **all** be true for my commits to count:

> * The email address used for the commits is associated with your GitHub account.
> * The commits were made in a standalone repository, not a fork.
> * The commits were made:
>   * In the repository's default branch (usually master)
>   * In the gh-pages branch (for repositories with Project Pages sites)

Since I was making my commits in a forked repository, they weren't being counted. A quick Google search revealed that I could have the forked repository detached by sending an email to GitHub Support. So, I sent this message:

> Hello, I forked from svmiller/svmiller.github.io to use it as a template for my Jekyll powered site in my anjuan.github.io repository. I have started making changes to this fork to align it with the design and content I want for my site, and I will never push any changes to svmiller.github.io. Please turn my fork into a standalone repository.
> 
> Thank you,
> 
> Anjuan  

## Edit

TBD

## Next Steps

Create local Jekyll site and push up to server.
