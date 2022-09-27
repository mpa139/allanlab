---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/arm4mod
---

{% assign prj = site.data.projects_current[7] %}
# {{ prj.title }}
![](/images/pubpic/{{ prj.image }}){:class="img-responsive"}
{{ prj.description }}  
<br><br>

### Related Papers
{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}
<br>