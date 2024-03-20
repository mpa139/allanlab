---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- Semantic Meaning & Analysis"
sitemap: false
permalink: /aiMeaning/
---

# Semantic Meaning & Analysis


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [AI-based Exploration of Art and Design]({{ site.url }}{{ site.baseurl }}/aiArts) ## [AI Anonymization]({{ site.url }}{{ site.baseurl }}/aiAnon) ## [AI Cognitive Creativity]({{ site.url }}{{ site.baseurl }}/aiCreativity)<br>
 ## [Sensing Humans (Bio/Brain/Face/Movement/VR)]({{ site.url }}{{ site.baseurl }}/bioBrainVR) ## [AI Modeling Thought & Language]({{ site.url }}{{ site.baseurl }}/aiThought) <br>

Reseachers: Steve DiPaola, Suk Choi, Meehae Song, Nouf Abukhodair, Vanessa Utz


**The Research:**
Early Deep Learning systems are trained on huge datasets including text/image pairs that while can embed simple meaning, are still mainly trained on nouns like people, things, ... Our main research area is to go beyond that to deeper Semantic Meaning & Analysis work . Which parses and models more multimodal and deeper semantic meaning to AI work. We do this by both analyzing meaning space ( cognitive science of the arts, gesture, emotion, empathy, creativity, behavior, ...) but also then build models from cognitively and rigorously mapping these spaces that we can then use in our new emerging systems (with application in health, the arts, and education.
<br><br>
Our work into a new method to understand, measure and model "aesthic emotion" (see studies and papers)
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s2.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s3.jpg" class="img-responsive" width="70%"/>
Reverse engineering generative visual Ai systems to better understand current meaning making to improve them. Here an emotionally complex prompt “an angry man punching a bag in a crowded joyful gym” and diffusion based output where we then used an advanced system to reverse detect and heatmap the meaning of every word back through the system
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s4.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s5.jpg" class="img-responsive" width="70%"/>
Deep studies with eye tracking, on how an art viewer perceives (cognitively) artwork where we AI redraw masterwork (switch left/right eye detail & lost and found edges near chin). See several papers and over 200 press articles on our findings - like this one [Magic of Rembrandt's Painting Technique Revealed](https://www.livescience.com/9920-magic-rembrandt-painting-technique-revealed.html).
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s6.jpg" class="img-responsive" width="70%"/>
Additional studies on deep meaning in aesthics, emotions, creativity, empathy, ... ( see papers).
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artsuk1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s7.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/s8.jpg" class="img-responsive" width="70%"/>

<iframe width="450" height="230" src="https://www.youtube.com/embed/N4Xr6Zm7Fes?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/O_FaV-6hahM?rel=0" frameborder="0" allowfullscreen></iframe>


<br>


<div id="paperSection"></div>


**------  PAPERS: Semantic Meaning & Analysis  ------**


{% for publi in site.data.publist %}
  {% if publi.research contains 'aiMeaning' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

