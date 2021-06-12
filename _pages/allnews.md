---
title: "News"
layout: textlay
excerpt: "STMI Lab at Texas A&M University."
sitemap: false
permalink: /allnews/
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<b>{{ article.keyword }}</b> <em>{{ article.headline }}</em></p>
{% endfor %}
