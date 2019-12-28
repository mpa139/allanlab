---
title: "Roychoudhuri Lab - Team"
layout: gridlay
excerpt: "Roychoudhuri Lab: Team members"
sitemap: false
permalink: /team/
---
<br />
# Group Members

 **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**



{% assign number_printed = 0 %}
{% assign members_sorted = site.members | sort: 'tier' %}
{% for member in members_sorted %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <a href="{{ site.baseurl }}/{{ member.url }}">
  <img src="{{ site.url }}{{ site.baseurl }}/images/member_pic/{{ member.picture }}" class="img-responsive" width="25%" style="float: left" /></a>
  <h4> <a style="text-decorations:none; color:inherit;" href="{{ site.baseurl }}/{{ member.url }}">{{ member.fullname }}</a></h4>
  {{ member.position }}<br>
  email: {{ member.email }}<br>
  <i><a style="text-decorations:none; color:inherit;" href="{{ site.baseurl }}/{{ member.url }}">>> More information</a></i>
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

### Lab photos
<br />

<div id="pixlee_container"></div><script type="text/javascript">window.PixleeAsyncInit = function() {Pixlee.init({apiKey:'CcW-ROKwr2OMysCod8OD'});Pixlee.addSimpleWidget({widgetId:'24171'});};</script><script src="//instafeed.assets.pixlee.com/assets/pixlee_widget_1_0_0.js"></script>