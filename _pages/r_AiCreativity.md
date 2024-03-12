---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI Cognitive Creativity"
sitemap: false
permalink: /aiCreativity/
---

# AI Cognitive Creativity


RESEARCH :: See [Related papers](#paperSection) ::  Related Projects: [Research]({{ site.url }}{{ site.baseurl }}/research)

Reseachers: Steve DiPaola, Vanessa Utz, Suk Choi, Nilay Ozge Yalcin, Nouf Abukhodair, Meehae Song  


**The Research:**
The goal of our research team is to model aspects of human creativity in AI using cognitive science as a basis for our work. Specially we are using Deep Neural Networks (and evolutionary systems) in the form of Deep Learning, CNNs, RNNs, Gans, Diffision, LLmMs and other modern techniques to attempt to replicate aspects of human expression and creativity. We are known for modelling expression semantics and generation of visual art (stills, videos, VR) but have extended our work into expressive forms of linguistic (word based) narrative.

<br>
<iframe width="450" height="230" src="https://www.youtube.com/embed/57zVdTMgyE4?rel=0" frameborder="0" allowfullscreen></iframe>
<br>
<iframe width="450" height="230" src="https://www.youtube.com/embed/O_FaV-6hahM?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/fIuvZ5S4CgU?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/8Nn-DOw_vFE?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/5WoVOiV1fdQ?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/B4F5K4AAGwU?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/cncSjzDkkEk?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/gd4Ie1aX02k?rel=0" frameborder="0" allowfullscreen></iframe>


<div id="paperSection"></div>


<br><br>
**------  PAPERS: AI Cognitive Creativity ------**


{% for publi in site.data.publist %}
  {% if publi.research contains 'AICreativity' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

