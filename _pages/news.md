---
title: "News"
layout: textlay
excerpt: "Network and Data Science Lab at Vanderbilt University."
sitemap: false
permalink: /news.html
---

# News

<!--
{% for article in site.data.news %}
<p>{{ article.date }} <br>
<em>{{ article.headline }}</em></p>
{% endfor %}
-->

{% for article in site.data.news %}

{% if article.headline == "YEAR" %}
  <h3><b>{{ article.date }}</b></h3>
{% else %}
  {{ article.date }}<br>
  <em>{{ article.headline }}</em><br style="line-height: 20px" />
{% endif %}

{% endfor %}
-->
