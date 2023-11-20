---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/cv-facade-inspection
---

{% assign permalink_parts = page.permalink | split: '/' %}
{% assign last_part = permalink_parts | last %}

{% for project in site.data.projects_current %}
    {% if project.addr == { last_part } %}
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
=======
---
title: "biLAB | Current Project"
layout: textlay
excerpt: "Current project"
sitemap: false
permalink: /projects/cv-facade-inspection
---

{% assign prj = site.data.projects_current[9] %}
# {{ prj.title }}
![](/images/pubpic/{{ prj.image }}){:class="img-responsive"}
{{ prj.description }}  
<br><br>

### Related Papers
{% for paper in prj.pp %}
* {{ paper[1] }}
{% endfor %}