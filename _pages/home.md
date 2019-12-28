---
title: "Roychoudhuri Lab - Home"
layout: homelay
excerpt: "Roychoudhuri Lab at the University of Cambridge."
sitemap: false
permalink: /
---

### Immunoregulation: Uncovering the 'brakes' on immune activation 
T cells drive immune activation and promote clearance of infections and cancer. However, their function can also provoke autoimmune and allergic inflammation. The immune system therefore employs suppressive mechanisms, referred to as immunoregulatory mechanisms, to restrain excessive immune activation. While immunoregulatory mechanisms play a beneficial role in preventing inflammation, they can also suppress immune responses during chronic infections and cancer in a process known as immunosuppression. Immunoregulatory mechanisms therefore function as 'brakes' on immune activation and are important therapeutic targets. 

Our research aims to understand the molecular and cellular mechanisms underpinning host immunoregulation in infection, inflammation and cancer. We hope that this may enable development of new therapies aimed at manipulating immune function in patients with **inflammation** and **cancer**.

{% include carousel.html %}

To this end, we utilise molecular and cellular immunology, cutting-edge mouse genetics and tumour immunity models, and functional genomics to enable the discovery and characterisation of novel host immunoregulatory mechanisms (see [Research](research)).

We are located at the Department of Pathology at the University of Cambridge. We work closely with collaborators in the Department and broader Cambridge science community and take advantage of the world-class research facilities of the University of Cambridge. 

 **We are looking for passionate new PhD students, Postdocs, and Master's students [(more info)]({{ site.url }}{{ site.baseurl }}/vacancies)!**

### Publication highlights
(For a full list see [Publications](publications))

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-4 clearfix">
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

