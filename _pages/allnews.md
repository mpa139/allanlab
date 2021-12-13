---
title: "News"
layout: textlay
excerpt: "Lobel Lab at Bar-Ilan University."
sitemap: false
permalink: /lobelnews.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline | markdownify}}</em></p>
{% endfor %}
