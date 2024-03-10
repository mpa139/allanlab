---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- Research"
sitemap: false
permalink: /virtualHumans/
---

# AI Affective Virtual Human


RESEARCH :: See [Related papers](#paperSection) ::  Related Projects: [Publications]({{ site.url }}{{ site.baseurl }}/research)

Reseachers: Steve DiPaola, Mahdi Davoodikakhki, Andrey Goncharov, Nilay Ozge Yalcin 


**The Research**
Our open-source toolkit / cognitive research in AI 3D Virtual Human (embodied IVA : Intelligence Virtual Agents) : a real-time system that can converse with a human by sensing their emotions and conversation ( via facial emotion recognition, voice stress, semantics of the speech and words) and respond affectively, emotionally (voice, facial animation, gesture, etc) to a user in front of it via a host of gestural, motion and bio-sensor systems, with several in lab AI systems and give a coherent, personality-based conversational answers via speech, expression and gesture. The system uses Unity and SmartBody (USC) API who we have collaborated with for years. We use cognitive modeling, empathy modelling, NLP and a variety of AI-based modules in our system (see papers).


Our **affective real-time 3D AI virtual human** setup with face emotion recognition, movement recognition and data glove recognition. See overview video or specific videos or papers below

<br>
<iframe width="450" height="230" src="https://www.youtube.com/embed/RMLD7jccv_w?rel=0" frameborder="0" allowfullscreen></iframe>
<br>
<iframe width="450" height="230" src="https://www.youtube.com/embed/O_FaV-6hahM?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/vcDgqx8wlmw?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/1f-TAj79q38?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/lVMMyIuJWEQ?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/2NmsT3VgZXg?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/TOOWDdWeMQQ?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/_r1XNu4e-rg?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/I-sZEyvtsXk?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/O2SUUo55lXM?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/xPMFS10M8qk?rel=0" frameborder="0" allowfullscreen></iframe>



<div id="paperSection"></div>


<br><br>
**------  PAPERS: Virtual Humans  ------**



{% for publi in site.data.publist %}
  {% if publi.research contains 'virtualHumans' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

