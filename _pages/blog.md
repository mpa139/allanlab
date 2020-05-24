---
title: "METRICS Lab - Blog"
layout: gridlay
excerpt: "METRICS Lab -- Blog"
sitemap: false
permalink: /blogs/
---
## Blog 

<ul class="posts">
  {% for post in site.posts %}
    <span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
  {% endfor %}
</ul>
