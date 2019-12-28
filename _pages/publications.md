---
title: "Roychoudhuri Lab - Publications"
layout: gridlay
excerpt: "Roychoudhuri Lab -- Publications."
sitemap: false
pubmed_searchterm: Roychoudhuri R [author]
permalink: /publications/
---

<br />
## Publication Highlights
(For a full list see [below](#full-list))

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <p style="padding-top: 0px;"><img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" /></p>
  <p style="padding-top: 0px;">{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
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

## Full publication list

{% include pubmed_gen_reflist.html pubmed_searchterm = page.pubmed_searchterm %}


