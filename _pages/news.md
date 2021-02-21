---
title: "News"
layout: textlay
excerpt: "Network and Data Science Lab at Vanderbilt University."
sitemap: false
permalink: /news.html
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
