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

<ul id="archive">
{% for post in site.posts %}
  {% capture y %}{{post.date | date:"%Y"}}{% endcapture %}
  {% if year != y %}
    {% assign year = y %}
    <h2 class="blogyear">{{ y}}</h2>
  {% endif %}
<li class="archiveposturl"><span><a href="{{ site.url }}{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></span><br/>
<span class = "postlower"><strong>Author:</strong> {{post.author}} 
<strong>Category:</strong>  {% if post.categories %}
 
  {% for cat in post.categories %}
  <a href="/categories/#{{ cat }}" title="{{ cat }}">{{ cat }}</a>&nbsp;
  {% endfor %}

{% endif %} <!-- {{ post.categories | first }} -->
<strong style="font-size:100%; font-family: 'Titillium Web', sans-serif; float:right">{{ post.date | date: '%d %b %Y' }}</strong> 
</span> 

</li>
{% endfor %}
</ul>

<!-- {{ post.date | date: '%m %d, %Y' }} -->
