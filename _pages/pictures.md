---
title: "(Pics)"
layout: piclay
excerpt: "Pictures."
permalink: /pictures/
---

<h1>My firstt</h1>

images:
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
  title: klsjfd
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
  title: klsjfd
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
  title: klsjfd
---
<ul class="photo">
  {% for image in page.images %}
    <li><img src="{{ image.image_path }}" alt="{{image.title}}"/></li>
  {% endfor %}
<ul>

# Pictures
Jump to: Leiden, ETHZ, Cornell, St Andrews

## Leidenn

Put in 

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
