---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI-based Exploration of Art and Design"
sitemap: false
permalink: /aiArts/
---

# AI-based Exploration of Art and Design


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [AI Anonymization]({{ site.url }}{{ site.baseurl }}/aiAnon) ## [Semantic Meaning & Analysis]({{ site.url }}{{ site.baseurl }}/aiMeaning)
 ## [AI Modeling Thought & Language]({{ site.url }}{{ site.baseurl }}/aiThought) <br>
 ## [Sensing Humans (Bio/Brain/Face/Movement/VR)]({{ site.url }}{{ site.baseurl }}/bioBrainVR)
 ## [AI Cognitive Creativity]({{ site.url }}{{ site.baseurl }}/aiCreativity) ## [AI Ethics: Gender]({{ site.url }}{{ site.baseurl }}/aiEthicsG) ## [AI Ethics: Climate]({{ site.url }}{{ site.baseurl }}/aiEthicsC)
<br>

Reseachers: Steve DiPaola, Suk Choi, Meehae Song, Nouf Abukhodair, Vanessa Utz, Shannon Cuykendall
 

**The Research:**
Computational and AI techniques, combined with our research in cognitive science based work in creativity, aesthetics, sensing, movement -- heralds in new forms of art and design, including new exploration / ideation  / creation / collaboration techniques. 

Using our systems - users can journey through art and design ideation space.
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artmet1.jpg" class="img-responsive" width="50%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artmet2.jpg" class="img-responsive" width="50%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artmet3.jpg" class="img-responsive" width="50%"/>

Our system allows for moving through a space where all is logged and users can journey back and forth and on creative forks - where all parts of the journey are archived and mapped.  
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artexplor1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/arte1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/arte2.jpg" class="img-responsive" width="70%"/>

These techniques have been used by many artists including much work in video and large scale multimedia art including with dancers, and art activism. See work with:
[DANCE](https://1aha1.com/art/portfolio-items/floating-departures) .. and .. [Large Projection](https://1aha1.com/art/portfolio-items/body-as-border-traces-and-flows-of-connection/).
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artdance1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artdance2.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/arta1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artsuk1.jpg" class="img-responsive" width="70%"/>

We often exhibit the work at major museums, galleries, conferences and at talks, interviews (TV News here), panels including discussing ethical implications. See News section for talks. 
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artPress1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/artPress2.jpg" class="img-responsive" width="70%"/>



<br>


<div id="paperSection"></div>


**------  PAPERS: AI-based Exploration of Art and Design  ------**


{% for publi in site.data.publist %}
  {% if publi.research contains 'aiArts' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

