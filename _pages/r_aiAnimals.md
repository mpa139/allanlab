---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI Modeling Animals"
sitemap: false
permalink: /aiAnimals/
---

# AI Modeling Animals 


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [Semantic Meaning & Analysis]({{ site.url }}{{ site.baseurl }}/aiMeaning) ## [AI Modeling Thought & Language]({{ site.url }}{{ site.baseurl }}/aiThought) <br>
 ## [AI Affective Virtual Human]({{ site.url }}{{ site.baseurl }}/virtualHumans) ## [XR Avatars; Edu, Coaches, Health]({{ site.url }}{{ site.baseurl }}/xrAvatars) ## [Sensing Humans (Bio/Brain/Face/Movement/VR)]({{ site.url }}{{ site.baseurl }}/bioBrainVR)

Reseachers: Steve DiPaola, Bill Kraus

**The Research:**
Our AI work here is in simulating complex (human and) animal behavoir using both Action Selection AI and Neural Networks (see papers). Technology is becoming increasingly incorporated into exhibit design. Both on the floor and extended online. Our AI work focuses on the design of  VR AI interactive exhibits for an aquarium gallery. The goal was to use technology to better immerse and engage the visitors in complicated educational concepts about the life of wild belugas. We were interested in encouraging deeper exploration of the content than what is typically possible via wall signage or a video display. The beluga simulation uses extremely realistic graphics and is based on an intelligent system that allows the virtual belugas to learn and alter their behaviour based on the visitor interaction. It was informed by research data from the live belugas, (e.g. voice recordings tied to mother/calf behavior) obtained from interviews with the marine mammal scientists and education staff. Observation and visitor studies determined that visitors rarely visit alone, so the interface was designed to encourage collaboration. It allows visitors and their companions to engage in “what-if” scenarios of wild beluga emergent behavior via a 3D interactive that uses artificial intelligence, physically based animation, and real-time graphics. The program could be linked to the aquarium web site to allow for an extension of the aquarium visitor experience.
<br> 
<img src="{{ site.url }}{{ site.baseurl }}/images/res/whale1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/whale2.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/whale3.jpg" class="img-responsive" width="70%"/>

<br>


<div id="paperSection"></div>


**------  PAPERS: AI Modeling Animals  ------**


{% for publi in site.data.publist %}
  {% if publi.research contains 'aiAnimals' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

