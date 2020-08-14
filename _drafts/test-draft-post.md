---
title: 'Test Draft Post'
author: anjuan
layout: post
date: "2017-08-27"
permalink: /blog/test-draft-post/
categories:
  - Drafts
excerpt: "This is a test draft post."
comments: true
---

Dominoes for life


<html>
<head>
<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 10%;
  padding: 1px;
}

/* Clearfix (clear floats) */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
</head>
<body>

<div class="row">
  <div class="column">
    <img src="/images/6-6.png" alt="Snow" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/0-5.png" alt="Forest" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/6-6.png" alt="Mountains" style="width:100%">
  </div>
</div>

</body>
</html>

I'm testing the draft capability of Jekyll. To preview this draft on my site, I need to run `jekyll serve` or `jekyll build` with the `--drafts` switch. Each draft will be assigned the value of the last time it was modified for its date. So, currently edited drafts will be seen as the latest posts.

If you set the `date` value of the post to a day in the future, then it will not show up on the site.

<html>
<head>
<style>
* {
  box-sizing: border-box;
}

.column {
  float: left;
  width: 10%;
  padding: 1px;
}

/* Clearfix (clear floats) */
.row::after {
  content: "";
  clear: both;
  display: table;
}
</style>
</head>
<body>

<div class="row">
  <div class="column">
    <img src="/images/6-6.png" alt="Snow" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/6-6.png" alt="Forest" style="width:100%">
  </div>
  <div class="column">
    <img src="/images/6-6.png" alt="Mountains" style="width:100%">
  </div>
</div>

</body>
</html>


Gonna be a good article
