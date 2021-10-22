---
title: "Li Lab - Publications"
layout: gridlay
excerpt: "Allan Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

(For a full list of publications and patents see [below](#full-list-of-publications) or go to [ResearchGate](https://www.researchgate.net/profile/Kexin-Li-22/research))

## Full List of publications

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}
