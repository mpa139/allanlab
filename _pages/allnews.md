---
title: "News"
layout: textlay
excerpt: "biLAB at New York University."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
---
<p><em style="font-size: 20px; color: black; font-weight: bold;">{{ article.headline }}</em></p>
<p> {{ article.text}}</p>
<br>
{% endfor %}
