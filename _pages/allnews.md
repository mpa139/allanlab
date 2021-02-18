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
<p><em><b>- {{ article.headline }} -</b></em></p>
<p> {{ article.text}}</p>
<br>
{% endfor %}
