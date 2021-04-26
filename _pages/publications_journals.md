---
title: "biLAB | Publications"
layout: gridlay
excerpt: "biLAB | Publications."
sitemap: false
permalink: /publications_journals/
---


# Selected Journal Papers

{% for publi in site.data.publist %}
---
  {{ forloop.index }} . {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>
{% endfor %}