---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/increasing-work-zone-safety
---

{% assign prj = site.data.projects_current[5] %}
# {{ prj.title }}
![](/images/pubpic/{{ prj.image }}){:class="img-responsive"}
{{ prj.description }}  
<br><br>

{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}
<br>