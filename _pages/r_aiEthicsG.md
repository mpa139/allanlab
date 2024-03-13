---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI Ethics: Gender"
sitemap: false
permalink: /aiEthicsG/
---

# AI Ethics: Gender


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [AI Ethics: Climate]({{ site.url }}{{ site.baseurl }}/aiEthicsC)  ## [AI Anonymization]({{ site.url }}{{ site.baseurl }}/aiAnon)

Reseachers: Prochetta Nag, Nilay Yalcin, Steve DiPaola


**The Research:**
We should note that besides this area, our AI Ethics work is also wide ranging in privacy, climate, security, heath, activism, ownership, futures, and outreach. 

Our lab is current 70% female PhDs and Masters which brings a different perspective to our work. We participate in Women in ML and Women in STEM/STEAM outreach. As well as talks, panels and organization on ethics.  

One such work: 
Will AI embodied agents follow the same gender steriotypes of early AI voice systems. Our society is changing its notions of gender stereotypical traits and roles. Virtual agent research should follow, where the old assumptions and research need to be revisited in light of new evidence on the critical gap in gender stereotypes. This research is the first step to highlight that these changing gender stereotypes also apply to virtual agents. By careful examination of the current stereotypical traits and introducing the androgynous agents’ concept, we aimed to find an approach to reduce the stereotypical assumptions used by the virtual agent research, rather than reinforcing the bias. Our findings showed that we designed representative male, female, androgynous characters with systematical manipulation of static facial cues. Our results also mostly supported the findings of a genderbalanced view for stereotypical traits and roles from recent research on humans.
<br> 
<img src="{{ site.url }}{{ site.baseurl }}/images/res/gender1.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/gender2.jpg" class="img-responsive" width="70%"/>
<img src="{{ site.url }}{{ site.baseurl }}/images/res/gender3.jpg" class="img-responsive" width="70%"/>

<br>


<div id="paperSection"></div>


**------  PAPERS: AI Ethics: Gender ------**

[Papers](https://www.researchgate.net/profile/Procheta-Nag-2)
{% for publi in site.data.publist %}
  {% if publi.research contains 'aiEthicsG' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

