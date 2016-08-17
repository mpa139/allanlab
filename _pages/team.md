---
title: "Team"
layout: gridlay
excerpt: "Allan Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors).

## Staff
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
<p>Tjerk Benschop, Alexander Vanstone</p>

## Alumni
<p>Oliver Ostojic (Master student, 2016), Arjo Andringa (Bachelor student, 2016), Nikolaos Iliopoulos (visitor, 2016), Daniëlle van Klink (Bachelor student, 2016), Farshaad Hoeseni (Master student, 2015)</p>

## Administrative Support
<p><a href="mailto:Rijsewijk@Physics.LeidenUniv.nl">Ellie van Rijsewijk</a> is helping us (and other groups) with administration.</p>

## Lab Visitors
<p><a href="http://stanford.edu/~safavi/">Amir Safavi-Naeini</a> (Stanford), <a href="http://www.ru.nl/spm">Alexander Ako Khajetoorians</a> (Radboud University), <a href="http://www.mhamidian.com">Mohammad Hamidian</a> (Harvard->UC Davis), <a href="https://www.bnl.gov/cmpmsd/mbe/default.asp">Ivan Bozovic</a> (BNL / Yale), <a href="http://www.fmassee.nl">Freek Massee</a> (Paris)</p>
