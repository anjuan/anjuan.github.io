---
layout: page
title: Blog
permalink: /blog/
---

I blog semi-regularly about a variety of topics. Most of my blog posts are about my career in tech, my thoughts on engineering culture, my travels, and other topics that interest me.

Below is a list of my blog posts in chronological order and grouped by year. [Click here to see them grouped by category.](/categories/)

You can also search my blog using the box below. You'll get a list of links to any posts that contain the text you enter.

<!---
Create the search box and search button.
-->

<form action="get" id="site_search">
<left>
  <input style="font-size:20px;" type="text" id="search_box">
  <input style="font-size:20px;" type="submit" value="Search">
</left>
</form>
<br>

<ul id="search_results"></ul>

<script src="/js/lunr.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="/js/search.js"></script>

<!---
List blog posts grouped by year.
-->

<ul class="listing">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <li class="listing-seperator">{{ y }}</li>
  {% endif %}
  <li class="listing-item">
    <time datetime="{{ post.date | date:"%Y-%m-%d" }}">{{ post.date | date:"%Y-%m-%d" }}</time>
    <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
    <p style="margin-left: 93px">{{ post.excerpt }}</p>
  </li>
{% endfor %}
</ul>
