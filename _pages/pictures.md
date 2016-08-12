---
title: "(Pics)"
layout: piclay
excerpt: "Pictures."
sitemap: false
permalink: /pictures/
---
images:
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
 title: leiden
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
 title: leiden
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
 title: leiden
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
 title: leiden
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
 title: leiden
- image_path: {{ site.url }}{{ site.baseurl }}/images/picpic/WebpageLeiden_red.jpg
 title: leiden

  {% for image in page.images %}
  <figure>
    <img src="{{ image.image_path }}">
  </figure>
  {% endfor %}


---

# Pictures
Jump to: Leiden, ETHZ, Cornell, St Andrews

## Leidenn

[Put in galleries]

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
