---
title: "biLAB | Publications"
layout: gridlay
excerpt: "biLAB | Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Group highlights

(For a full list see [below](#full-list) or go to [Google Scholar](https://scholar.google.ch/citations?user=TqxYWZsAAAAJ), [ResearcherID](https://www.researcherid.com/rid/D-7763-2012))

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


## Journal and Submitted Papers

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}

## Book Chapter

{% for book in site.data.books %}

  {{ book.apa }} <br>

{% endfor %}

## Conferences

### 2019

{% for conf in site.data.conference %}

  {{ conf.conf19 }} <br>

{% endfor %}

### 2018

{% for conf in site.data.conference %}

  {{ conf.conf18 }} <br>

{% endfor %}

### 2017

{% for conf in site.data.conference %}

  {{ conf.conf17 }} <br>

{% endfor %}

### 2016

{% for conf in site.data.conference %}

  {{ conf.conf16 }} <br>

{% endfor %}

### 2015

{% for conf in site.data.conference %}

  {{ conf.conf15 }} <br>

{% endfor %}

### 2014

{% for conf in site.data.conference %}

  {{ conf.conf14 }} <br>

{% endfor %}

### 2013

{% for conf in site.data.conference %}

  {{ conf.conf13 }} <br>

{% endfor %}

### 2012

{% for conf in site.data.conference %}

  {{ conf.conf12 }} <br>

{% endfor %}

### 2010

{% for conf in site.data.conference %}

  {{ conf.conf10 }} <br>

{% endfor %}

### 2009

{% for conf in site.data.conference %}

  {{ conf.conf09 }} <br>

{% endfor %}

### 2008

{% for conf in site.data.conference %}

  {{ conf.conf08 }} <br>

{% endfor %}

### 2007

{% for conf in site.data.conference %}

  {{ conf.conf07 }} <br>

{% endfor %}

### 2006

{% for conf in site.data.conference %}

  {{ conf.conf06 }} <br>

{% endfor %}

### 2005

{% for conf in site.data.conference %}

  {{ conf.conf05 }} <br>

{% endfor %}

### 2004

{% for conf in site.data.conference %}

  {{ conf.conf04 }} <br>

{% endfor %}

### 2003

{% for conf in site.data.conference %}

  {{ conf.conf02 }} <br>

{% endfor %}

### 2002

{% for conf in site.data.conference %}

  {{ conf.conf02 }} <br>

{% endfor %}