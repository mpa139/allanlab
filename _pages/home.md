---
title: "Roychoudhuri Lab - Home"
layout: homelay
excerpt: "Roychoudhuri Lab at the University of Cambridge."
sitemap: false
permalink: /
---

### Immunoregulation: Uncovering the 'brakes' on immune activation 
T cells drive immune activation and promote clearance of infections and cancer. However, their function can also cause  autoimmune and allergic inflammation. The immune system therefore employs suppressive mechanisms, referred to as immunoregulatory mechanisms, to restrain excessive immune activation. While immunoregulatory mechanisms play a beneficial role in preventing inflammation, they can also suppress immune responses during chronic infections and cancer in a process known as immunosuppression. Immunoregulatory mechanisms therefore function as 'brakes' on immune activation and are important therapeutic targets. 

Our research aims to understand the molecular and cellular mechanisms underpinning host immunoregulation in infection, inflammation and cancer. We hope that this may enable development of new therapies aimed at manipulating immune function in patients with inflammation and cancer.

{% include carousel.html %}

To this end, we develop novel spectroscopic-imaging scanning tunneling microscopy (SI-STM) tools to visualize the relevant quantum mechanical degrees of freedom. We want to be able to build the perfect instruments to answer the  scientific questions we deem most important (see [Research](research)).

We are located at Leiden University, the birthplace of superconductivity and home to Kamerlingh Onnes, Lorentz, Huygens, Einstein, de Sitter, and others (see e.g. [the wall of signatures from Ehrenfest lecturers](https://www.lorentz.leidenuniv.nl/history/colloquium/muur_heel.html)). We exchange ideas and work with our neighbors from [Quantum Matter & Optics](http://www.physics.leidenuniv.nl/qo-home), as well as with the colleagues from our [world-class theory section](https://www.lorentz.leidenuniv.nl).

 **We are  looking for passionate new PhD students, Postdocs, and Master students to join the team** [(more info)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**

### Publication highlights
(For a full list see [Publications](publiations))

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

