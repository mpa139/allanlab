---
title: "News"
layout: textlay
excerpt: "Denolle Quake Lab at UW"
sitemap: false
permalink: /allnews
---

# News
---

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
