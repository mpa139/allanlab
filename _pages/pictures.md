---
title: "(Pics)"
layout: piclay
excerpt: "Pictures."
permalink: /pictures/
---

{% assign number_printed = 0 %}
{% for pic in site.data.pictures_Leiden %}

{% assign even_odd = number_printed | modulo: 3 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
 <p>{{ pic.title }}</p>
  <img src="{{ site.url }}{{ site.baseurl }}/images/picpic/gallery/{{ pic.image }}" class="img-responsive" width="90%" style="float: left" />
 
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 2 %}
</div>
{% endif %}


{% endfor %}

{% assign even_odd = number_printed | modulo: 3 %}
{% if even_odd == 1 %}
</div>
{% endif %}

{% if even_odd == 2 %}
</div>
{% endif %}

<p> &nbsp; </p>



# Pictures
Jump to: Leiden, ETHZ, Cornell, St Andrews

## Leiden

<figure>
	<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg" width="75%">
	<figcaption2>First advertisement.</figcaption2>
</figure>


## ETHZ
<figure>
	<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/WebpageETH_red.jpg" width="75%">
	<figcaption2>From the group of Andreas Wallraff.</figcaption2>
</figure>

## Cornell
<figure>
	<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/WebpageCornell_red.jpg" width="75%">
	<figcaption2>From the group of Seamus JC Davis.</figcaption2>
</figure>

## St Andrews
<figure>
	<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/WebpageSTA_red.jpg" width="75%">
	<figcaption2>From the group of Felix Baumberger (now at University of Geneva).</figcaption2>
</figure>
