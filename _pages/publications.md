---
title: "Publications"
layout: gridlay
excerpt: "Page not found. Your pixels are in another canvas."
sitemap: false
permalink: /publications/
---

# Publications

## Highlights

(For a full list see below or go to <a href="https://scholar.google.ch/citations?user=TqxYWZsAAAAJ">Google Scholar</a>, <a href="https://www.researcherid.com/rid/D-7763-2012">ResearcherID</a>)

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{{ "row" }}
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  {{ forloop.index0 }}
 </div>
</div>

{% assign number_printed = number_printed + 1 %}
{% if even_odd == 1 %}
</div>
{{ "exit row" }}
{% endif %}

{% endif %}
{% endfor %}

<p> &nbsp; </p>





## Full List

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}

