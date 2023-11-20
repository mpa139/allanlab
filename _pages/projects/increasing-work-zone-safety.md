---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/increasing-work-zone-safety
---

{% for project in site.data.projects_current %}
    {% if project.addr == "increasing-work-zone-safety" %}
        {% assign prj = project %}
        {% break %} <!-- Optional: use this if you only need the first match -->
    {% endif %}
{% endfor %}

# {{ prj.title }}
![](/images/pubpic/{{ prj.image }}){:class="img-responsive"}
{{ prj.description }}  
<br><br>

### Related Papers
{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}
<br>