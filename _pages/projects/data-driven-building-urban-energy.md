---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/data-driven-building-urban-energy
---

{% for project in site.data.projects_current %}
    {% if project.addr == "data-driven-building-urban-energy" %}
        {% assign prj = project %}
        {% break %}
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