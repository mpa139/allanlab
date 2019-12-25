---
title: "Allan Lab - Team"
layout: gridlay
excerpt: "Allan Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

 **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**



{% assign number_printed = 0 %}
{% for member in site.members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <a href="{{ site.baseurl }}/{{ member.url }}">
  <img src="{{ site.url }}{{ site.baseurl }}/images/member_pic/{{ member.picture }}" class="img-responsive" width="25%" style="float: left" /></a>
  <h4><a href="{{ site.baseurl }}/{{ member.url }}">{{ member.fullname }}</a></h4>
  {{ member.position }}<br><i>email: <{{ member.email }}></i><br>
  <i><a href="{{ site.baseurl }}/{{ member.url }}">> info</a></i>
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

