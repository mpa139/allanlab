---
title: "Daniel Soudry Lab - Publications"
layout: gridlay
excerpt: "Daniel Soudry Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Group highlights

**For a full list [see bellow](#full-list-of-publications) or go to [Google Scholar](https://scholar.google.co.il/citations?user=AEBWEm8AAAAJ&hl=iw&oi=ao).** The sign * indicates equal contribution of the authors. 

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
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

<p> &nbsp; </p>


## Patents
<em>I. Hubara, D. Soudry, and R. El-Yaniv,</em><br />Binarized Neural Networks<br /> US Patent 10,831,444 (2020)

<em>D. Soudry, D. Di Castro, A. Gal, A. Kolodny, and S. Kvatinsky</em><br /> Analog Multiplier Using Memristor a Memristive Device and Methods for Implementing Hebbian Learning Rules Using Memristor Arrays <br /> US Patent US9754203 B2 (2016)

## Full List of publications

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}

### Refereed Proceedings

{% for publi in site.data.publist %}

{% if publi.RefPro == 1 %}


  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}
{% endfor %}

### Journal Papers

{% for publi in site.data.publist %}

{% if publi.JourPap == 1 %}


  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}
{% endfor %}

### Refereed Abstracts (Conferences, Symposia, and Workshops)

{% for publi in site.data.publist %}

{% if publi.RefAbs == 1 %}


  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}
{% endfor %}


### Notes

{% for publi in site.data.publist %}

{% if publi.Notes == 1 %}


  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endif %}
{% endfor %}

