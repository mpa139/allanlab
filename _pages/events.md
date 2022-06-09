---
title: "BIQ - Events"
layout: gridlay
excerpt: "BIQ -- Events"
sitemap: false
permalink: /events/
---


# Events

## Next events

{% assign number_printed = 0 %}
{% for event in site.data.events %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ event.title }} [{{ event.date }}] </pubtit> 
  {{ event.headline }}
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/{{ event.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ event.description }}</p>
  <p><em>{{ event.authors }}</em></p>
  <p><strong><a href="{{ event.link.url }}">{{ event.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ event.news1 }}</strong></p>
  <p> {{ event.news2 }}</p>
 </div>
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

## Past events

{% assign number_printed = 0 %}
{% for past_event in site.data.past_events %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ past_event.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/{{ past_event.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ past_event.description }}</p>
  <p><em> {{ past_event.description_author }} <a href="{{past_event.author_page}}">{{ past_event.author }}</a></em></p>
  <p><strong><a href="{{ past_event.link.url }}">{{ past_event.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ past_event.news1 }}</strong></p>
  <p> {{ past_event.news2 }}</p>
 </div>
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