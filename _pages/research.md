---
title: "iVizLab - Research"
layout: gridlay
excerpt: "iVizLab -- Research."
sitemap: false
permalink: /research/
---


# Research 



**Our Research**

{% assign number_printed = 0 %}
{% for publi in site.data.research %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">

  <strong> [{{ publi.title }}]( {{ publi.page | relative_url }} )
  
  <img src="{{ site.url }}{{ site.baseurl }}/images/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>

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

<p> &nbsp; </p>


