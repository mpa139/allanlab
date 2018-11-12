---
title: "Lorenzo's group - Publications"
layout: gridlay
excerpt: "Lorenzo's group -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Highlights

<!--(For a full list see [below](#full-list)) or go to [Google Scholar](https://scholar.google.ch/citations?user=TqxYWZsAAAAJ), [ResearcherID](https://www.researcherid.com/rid/D-7763-2012)) -->

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well" style="height:320px;">
  <pubtit>{{ publi.title }}</pubtit>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left; margin-top: 15px; margin-bottom: 25px" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
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

<!-- <p> &nbsp; </p> -->

## Full List

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>
<button type="button" class="btn btn-success" onclick="location.href = '{{ publi.pdf }}';" style="padding: 3px 6px 3px;margin-left:8px;font-size: 10px;">
  PDF
</button>
<button type="button" class="btn btn-primary" data-toggle="modal" data-target="#{{ publi.bibid }}" style="padding: 3px 6px 3px;margin-left:8px;font-size: 10px;">
  Bibtex
</button>
<div class="modal fade" id="{{ publi.bibid }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
 <div class="modal-dialog" role="document">
  <div class="modal-content">
   <div class="modal-header">
    <h5 class="modal-title">Bibtex</h5>
    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
   </div>
   <div class="modal-body"><p>{{ publi.bibtex }}</p></div>
  </div>
 </div>
</div>

{% endfor %}

