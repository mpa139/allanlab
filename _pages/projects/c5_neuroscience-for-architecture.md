---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/neuroscience-for-architecture
---

{% assign prj = site.data.projects_current[4] %}
# {{ prj.title }}
{{ prj.description }}  
<br><br>

{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}