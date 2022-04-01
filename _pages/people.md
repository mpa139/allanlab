---
title: "Bonnen Lab - People"
layout: gridlay
excerpt: "Bonnen Lab: People"
sitemap: false
permalink: /people/
---

# Group Members

 **We are  looking for new students and postdocs to join the team** [(see openings)]({{site.url}}{{site.baseurl}}/positions) **!**


<!-- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

<!-- ## Staff -->
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign mod = number_printed | modulo: 3 %}

{% if mod == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix" style="text-align:center;align:center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-rounded" width="50%" style="float:top"/>
  <h4>{{ member.name }}</h4>
  <strong>{{ member.info }} <br/> {{ member.department }}</strong>
  <ul style="overflow: hidden">
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if mod == 2 %}
</div>
{% endif %}

{% endfor %}


{% if mod != 2 %}
</div>
{% endif %}




## Former Mentees

{% assign number_printed = 0 %}

{% for member in site.data.alumni_mentees %}
{% assign mod = number_printed | modulo: 3 %}

{% if mod == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix" style="text-align:center;align:center">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-rounded" width="50%" />
  <h4>{{ member.name }}</h4>
  <strong>{{member.info}} <br/> {{ member.duration }} </strong>
  <ul style="overflow:hidden;text-align:left">
  <li>{{ member.now }} </li>
  {% if member.achievements != nil %}
  <li> {{ member.achievements }} </li>
  {% endif %}</ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if mod == 2 %}
</div>
{% endif %}

{% endfor %}

{% if mod != 2 %}
stuff </div>
{% endif %}



