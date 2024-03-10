---
title: "iVizLab - Research"
layout: gridlay
excerpt: "iVizLab -- Research."
sitemap: false
permalink: /allnews/
---


# Lab News

{% assign number_printed = 0 %}
{% for publi in site.data.news %}

{% assign even_odd = number_printed | modulo: 2 %}


{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  <strong> [{{ publi.date }})
  {% if publi.image %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  {% endif %}
  <p>{{ publi.headline }}</p>

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

<p> &nbsp; </p>

