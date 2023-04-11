<<<<<<< HEAD
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
>>>>>>> 6ed9f2b6bec7ebbe6e0b8e318425aeb0568f02ec
<br>