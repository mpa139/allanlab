---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI Cognitive Creativity"
sitemap: false
permalink: /aiCreativity/
---

# AI Cognitive Creativity


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [AI-based Exploration of Art and Design]({{ site.url }}{{ site.baseurl }}/aiArts) ## [AI Anonymization]({{ site.url }}{{ site.baseurl }}/aiAnon) ## [Sensing Humans (Bio/Brain/Face/Movement/VR)]({{ site.url }}{{ site.baseurl }}/bioBrainVR)<br>
 ## [Semantic Meaning & Analysis]({{ site.url }}{{ site.baseurl }}/aiMeaning) ## [AI Modeling Thought & Language]({{ site.url }}{{ site.baseurl }}/aiThought) <br>

Reseachers: Steve DiPaola, Vanessa Utz, Suk Choi, Nilay Ozge Yalcin, Nouf Abukhodair, Meehae Song  

**The Research:**
The goal of our research team is to model aspects of human creativity in AI using cognitive science as a basis for our work. Specially we are using Deep Neural Networks (and evolutionary systems) in the form of Deep Learning, CNNs, RNNs, GANs, Diffusion, LLMs and other modern techniques to attempt to replicate aspects of human expression and creativity. We are known for modelling expression semantics and generation of visual art (stills, videos, VR) but have extended our work into expressive forms of linguistic (word based) narrative.

A video of our cognitive / AI creativity work. 
<iframe width="450" height="230" src="https://www.youtube.com/embed/57zVdTMgyE4?rel=0" frameborder="0" allowfullscreen></iframe>
<br>
Called "Creativity in the Age of Artificial Intelligence: Exploring the Intersection of Technology and Human Innovation." 

Via the Royal Society of Canada and Massey Lectures - Steve DiPaola and Joelle Pineau (VP of Meta/Facebook Research) explored the impact of artificial intelligence (AI) on the human creative process, from the arts and music to scientific and medical discovery.
Called "Creativity in the Age of Artificial Intelligence: Exploring the Intersection of Technology and Human Innovation." DiPaola starts at 23:27. Then questions.
<iframe width="450" height="230" src="https://www.youtube.com/embed/vBAhI4mluSY?t=1407?rel=0" frameborder="0" allowfullscreen></iframe>

Our research into how creativity works in the human brain (cognitive science based) and model that in our AI systems. We write papers on our techniques, do studies and writing AI systems that are used by us and artists worldwide.
<img src="{{ site.url }}{{ site.baseurl }}/images/res/aiC1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/aiC2.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/aiC3.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/aiC4.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/aiC5.jpg" class="img-responsive" width="70%"/>



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

