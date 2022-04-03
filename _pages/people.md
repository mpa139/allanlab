---
title: "Vision in Action Lab - People"
layout: gridlay
excerpt: "Vision in Action Lab: People"
sitemap: false
permalink: /people/
---


<h1 align="center">Group Members</h1>

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
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-rounded" width="66%" style="float:top"/>
  {% if member.link != nil %}
  <h4><a href="{{member.link}}">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
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
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-rounded" width="66%" />
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



