---
layout: page
title: Blog
permalink: /blog/
---

I blog semi-regularly about a variety of topics. Most of my blog posts are about what I'm learning in my tech career, my thoughts on engineering culture, my travels, and other things that interest me. 

Below is a list of my blog posts in chronological order. [Click here to see them grouped by category.](http://anjuansimmons.com/categories/)

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
    <p style="margin-left: 90px">{{ post.excerpt }}</p>
  </li>
{% endfor %}
</ul>
