---
title: "biLAB | Past Project"
layout: textlay
excerpt: "Past project"
sitemap: false
permalink: /projects/delivering-accurate-and
---

{% assign prj = site.data.projects_past[1] %}
# {{ prj.title }}
{{ prj.description }}  
<br><br>

{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}