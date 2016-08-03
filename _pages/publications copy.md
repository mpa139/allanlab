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

  {% increment nrpub %}


{% for publi in site.data.publist %}
{% if publi.highlight == 1 %}
  {% increment nrpub %}
  {{ forloop.index0 }}
{% endif %}
{% assign even_odd = nrpub | modulo: 2 %}
{{ even_odd }}
{% if even_odd == 1 %}
<div class="row">
{% endif %}
{% if publi.highlight == 1 %}
<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="/images/pubpic/{{ publi.image }}" class="img-responsive" width="25%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>
{% endif %}
{% if even_odd == 1 %}
</div>
{% endif %}{% endfor %}

## Full List

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}