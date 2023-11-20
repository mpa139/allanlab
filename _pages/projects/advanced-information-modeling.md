---
title: "biLAB | Past Project"
layout: textlay
excerpt: "Past project"
sitemap: false
permalink: /projects/advanced-information-modeling
---


{% for project in site.data.projects_past %}
    {% if project.addr == "advanced-information-modeling" %}
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