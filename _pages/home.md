---
title: "Roychoudhuri Lab - Home"
layout: homelay
excerpt: "Roychoudhuri Lab at the University of Cambridge."
sitemap: false
permalink: /
---

### Immunoregulation: Uncovering the 'brakes' on immune activation 
T cells have a powerful ability to drive immune activation and promote clearance of infections and cancer. However, their function can also promote deleterious autoimmune and allergic inflammation. The immune system therefore employs a variety of suppressive mechanisms, collectively referred to as immunoregulatory mechanisms, to restrain excessive immune activation.

While immunoregulatory mechanisms play a beneficial role in preventing inflammation, they can also powerfully suppress immune responses during chronic infections and cancer in a process referred to as immunosuppression. Immunoregulatory mechanisms therefore function as 'brakes' on immune activation and are important therapeutic targets.

Our research aims to understand the molecular and cellular mechanisms of tolerance and immunosuppression in physiology, and during infection, inflammation and cancer. We hope that this will enable development of new therapies aimed at manipulating immune function in patients with inflammation and cancer.


<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="5000" data-pause="hover" >
    <!-- Menu -->
    <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
        <li data-target="#carousel" data-slide-to="6"></li>
    </ol>

    <!-- Items -->
    <div class="carousel-inner" markdown="0">
    
        <div class="item active">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/STS.jpg" alt="Slide 1" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/SaphireSTM2.jpg" alt="Slide 2" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/cake_web.jpg" alt="Slide 3" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/logos.jpg" alt="Slide 4" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/NoiseCover2.jpg" alt="Slide 5" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/SmartTipSide.jpg" alt="Slide 6" />
        </div>       
         <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider7001400/lab.jpg" alt="Slide 7" />
        </div>
    </div>
  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>




To this end, we develop novel spectroscopic-imaging scanning tunneling microscopy (SI-STM) tools to visualize the relevant quantum mechanical degrees of freedom. We want to be able to build the perfect instruments to answer the  scientific questions we deem most important (see [Research](research)).

We are located at Leiden University, the birthplace of superconductivity and home to Kamerlingh Onnes, Lorentz, Huygens, Einstein, de Sitter, and others (see e.g. [the wall of signatures from Ehrenfest lecturers](https://www.lorentz.leidenuniv.nl/history/colloquium/muur_heel.html)). We exchange ideas and work with our neighbors from [Quantum Matter & Optics](http://www.physics.leidenuniv.nl/qo-home), as well as with the colleagues from our [world-class theory section](https://www.lorentz.leidenuniv.nl).

 **We are  looking for passionate new PhD students, Postdocs, and Master students to join the team** [(more info)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


# Publications

## Highlights

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

We are grateful for funding from the University of Cambridge Department of Pathology, [NWO](www.nwo.nl) ([Vidi talent scheme](http://www.nwo.nl/en/research-and-results/programmes/Talent+Scheme) and the [Frontiers in Nanoscience program](https://www.universiteitleiden.nl/en/research/research-projects/science/frontiers-of-nanoscience-nanofront)), and from an [ERC starting grant](https://erc.europa.eu/funding/starting-grants).

<figure class="fourth">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_Leiden.jpg" style="width: 210px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_Nanofront.jpg" style="width: 110px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_NWO.jpg" style="width: 120px">
  <img src="{{ site.url }}{{ site.baseurl }}/images/logopic/Logo_ERC.jpg" style="width: 110px">
</figure>
