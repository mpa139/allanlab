---
title: "News"
layout: textlay
excerpt: "Bonnen Lab at Indiana University."
sitemap: false
permalink: /allnews.html
---

# News

{% for article in site.data.news %}
---

<p> <span class="fa fa-calendar"></span> {{ article.date }} <br/> <em><b> {{ article.headline }} </b></em></p>
<p> {{ article.text}}</p>
<br>
{% endfor %}
