---
title: "News"
layout: textlay
excerpt: "Novedades"
sitemap: false
permalink: /allnews.html
---

# Novedades

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline | markdownify}}</em></p>
{% endfor %}
