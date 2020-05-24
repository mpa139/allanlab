---
title: "METRICS Lab - Blog"
layout: gridlay
excerpt: "METRICS Lab -- Blog"
sitemap: false
permalink: /blogs/
---
# Blogs

This is a collection of blog posts written by members of the METRICS group, to improve the accessbility of our research. All feedback is welcome and can be addressed to the author of the blog. 

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
