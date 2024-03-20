---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI Modeling Thought & Langauge"
sitemap: false
permalink: /aiThought/
---

# AI Modeling Thought & Langauge


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [Semantic Meaning & Analysis]({{ site.url }}{{ site.baseurl }}/aiMeaning) ## [AI-based Exploration of Art and Design]({{ site.url }}{{ site.baseurl }}/aiArts) ## [AI Cognitive Creativity]({{ site.url }}{{ site.baseurl }}/aiCreativity)<br>
 ## [Sensing Humans (Bio/Brain/Face/Movement/VR)]({{ site.url }}{{ site.baseurl }}/bioBrainVR)  <br>

Reseachers: Steve DiPaola, Rafael Arias Gonzalez, Nilay Yalcin, Maryam Ahmadzadeh


**The Research:**
Our AI work in cognitive modelling of thought, expression and language using advanced AI systems like AI Knowledge Graphs of thought and chained RAG based LLMs. Here allowing the public to talk faithfully (as possible) to inspiring historical figures like our Picasso and Van Gogh. With Van Gogh, we used our specific AI pre-processing of times of his life, historical events/people and the 700 letters he wrote in his own words to his brother Theo into a knowledge system that then goes through additional 3D facial expression, body gesture, talking, voice AI systems.
<br> 
<img src="{{ site.url }}{{ site.baseurl }}/images/res/vg1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/vg2.jpg" class="img-responsive" width="70%"/>

Our VR talking, expressing animated character even dynamically morph into painted form based on his emotional state.
<img src="{{ site.url }}{{ site.baseurl }}/images/res/vg3.jpg" class="img-responsive" width="70%"/>

Talking with our Virtual AI Picasso live (created with ivizlab research and [Virtro](https://www.virtro.ca/))
<iframe width="550" height="330" src="https://www.youtube.com/embed/Up7rLNkDkRo?rel=0" frameborder="0" allowfullscreen></iframe>
<br>


<div id="paperSection"></div>


**------  PAPERS: AI Modeling Thought & Langauge  ------**


{% for publi in site.data.publist %}
  {% if publi.research contains 'aiThought' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

