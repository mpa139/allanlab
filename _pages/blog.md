---
title: "METRICS Lab - Blogs"
layout: default
excerpt: "METRICS Lab -- Blogs"
sitemap: false
permalink: /blogs/
---

### Blogs 

  <ul class="post-list">
    {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
    {%- for post in posts -%}
      <span class="post-meta">{{ post.date | date: date_format }}</span>
      <h3>
        <a class="post-link" href="{{ post.url | relative_url }}">
          {{ post.title | escape }}
        </a>
      </h3>
      {%- if site.show_excerpts -%}
        {{ post.excerpt }}
      {%- endif -%}
      {%- endfor -%}
  </ul>

