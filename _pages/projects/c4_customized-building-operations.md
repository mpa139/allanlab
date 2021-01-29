---
title: "biLAB | Current project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/customized-building-operations
---

{% assign prj = site.data.projects_current[3] %}
# {{ prj.title }}
![](/images/pubpic/{{ prj.image }}){:class="img-responsive"}
{{ prj.description }}  
<br><br>

### Related Papers
{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}
<br>