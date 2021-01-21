---
title: "Research Group | biLAB"
layout: gridlay
excerpt: "Research Group biLAB"
sitemap: false
permalink: /team/
---

# About

The  Building Informatics and Visualization Lab (biLAB) is part of the [Department of Civil and Urban Engineering](https://engineering.nyu.edu/academics/departments/civil-and-urban-engineering) at the [NYU Tandon School of Engineering](https://engineering.nyu.edu/). It focuses on understanding the operational challenges associated with construction and operation of facilities and infrastructure systems in urban settings.

The research team works on information modeling and visualization to quantify the impact of architecture on human experience in the built environment, understand and improve the behaviors of existing/new facilities and civil infrastructure systems for next generation construction, maintenance, and operations. The research team takes advantage of advancements in technology in information modeling and visualization to integrate and provide information that engineers, owners, and facility operators need, at the right level of detail and visual form.

They work on developing information repositories and visualization platforms to better integrate the data captured from sensors and the context under which they operate to get a holistic view of the monitored system/infrastructure for better maintenance and operation.

## Our Research Domain:

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

<img src="/images/semiha2.jpg" width="40%"/>

#### The biLab is spearheaded by Prof. Semiha Ergan, Associate Professor of the Department of Civil and Urban Engineering.

[Prof. Ergan's NYU profile](https://engineering.nyu.edu/faculty/semiha-ergan)

[Prof. Ergan on Google Scholar](https://scholar.google.com/citations?user=WYwmI0wAAAAJ&hl=en)

[Prof. Ergan on ResearchGate](https://www.researchgate.net/profile/Semiha_Ergan)

Please check [Job Openings page](/jobopening) for openings in the research group.

# Research Group

Positions are available at [PhD](/downloads/Flier-PhD-Ergan_Oct15.pdf) and [PostDoc](/downloads/Flier-Postdoc-Darpa-Ergan.pdf) levels in BiLAB. please contact Prof. Ergan for details.  

<img src="/images/research_group.jpeg" width="65%"/>

Jump to [PhD Student](#phd-student), [Master and Bachelor students](#master-and-bachelor-students), [High school students hosted](#high-school-students-hosted), and [Alumni](#alumni).
  
  
## PhD Student
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


  
  
## Master and Bachelor Students
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
  
  
## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
  

## Former visitors, BSc/ MSc students
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

</div>
  
  
## High school students hosted

Summer 2018:  
Tina Wong, <b>Stuyvesant High School</b>  
Daniel Gomez, <b>Stuyvesant High School</b>  

Summer 2017:  
Connie Tsang, <b>Hunter College High School</b>  
Jason Cheung, <b>Stuyvesant High School</b>  
  
  


