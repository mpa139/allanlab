---
title: "biLAB | Current project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/customized-building-operations
---

{% assign prj = site.data.projects_current[3] %}
# {{ prj.title }}
{{ prj.description }}  
<br><br>

{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}