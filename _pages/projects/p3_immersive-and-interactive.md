---
title: "biLAB | Past Project"
layout: textlay
excerpt: "Past project"
sitemap: false
permalink: /projects/immersive-and-interactive
---

{% assign prj = site.data.projects_past[2] %}
# {{ prj.title }}
{{ prj.description }}  
<br><br>

{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}