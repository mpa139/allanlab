---
title: "biLAB | Projects"
layout: gridlay
excerpt: "biLAB | Projects."
sitemap: false
permalink: /projects_current/
---
<!-- # Research Domains
<br>
<span style="color:blue"><b>Architecture and Neuroscience</b></span>  
*How can we quantify the impact of architectural design features on human experience? Can we use the findings to improve the design practice for better and healtier experiences in the built environment?*  

<span style="color:blue"><b>Urban Challenges for AEC/FM</b></span>  
*How can the design, construction and facilities management processes be improved to tackle with  the challenges imposed by urban settings?*  

<span style="color:blue"><b>Understanding the context under which Civil Infrastructure Systems (CIS) operate</b></span>  
*How sensors and models can be integrated to better understand system behaviors?*  

<span style="color:blue"><b>Healthier building systems</b></span>  
*How can the performance of interconnected facility systems  be determined for setting proactive management strategies?*  

<b>Testbeds utilized</b>: legacy and smart buildings, airports, highways.  

<b>Tools utilized</b>: Building information models, data driven methodologies, advanced visualization
<br><br><br> -->
# Current Projects
Click images to see more details about projects.


{% assign number_printed = 0 %}
{% for publi in site.data.projects_current %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  [![](/images/pubpic/{{ publi.image }}){:class="img-responsive"}]({{ site.url }}{{ site.baseurl }}/projects/{{ publi.addr }})
  <!-- <p>{{ publi.description }}</p> -->
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
<br>