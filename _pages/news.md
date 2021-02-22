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

{% if article.date == YEAR %}
  <h3>{{ article.headline }}</h3><br>
{% else %}
  <em>{{ article.headline }}</em></br>
{% endif %}
</br>

{% endfor %}
-->
