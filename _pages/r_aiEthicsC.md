---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- AI Ethics: Climate"
sitemap: false
permalink: /aiEthicsC/
---

# AI Ethics: Climate


<strong> [See Related Papers](#paperSection) and Related Projects:</strong> <br>
 ## [AI Ethics: Gender]({{ site.url }}{{ site.baseurl }}/aiEthicsG)  ## [AI Anonymization]({{ site.url }}{{ site.baseurl }}/aiAnon)
 
Reseachers: Vanessa Utz, Steve DiPaola


**The Research:**

We should note that besides this area, our AI Ethics work is also wide ranging in privacy, gender, security, heath, activism, ownership, futures, and outreach. 

Climate implications of rapidly developing digital technologies, such as blockchains and the associated crypto mining and NFT minting, have been well documented and their massive GPU energy use has been identified as a cause for concern. However, we postulate that due to their more mainstream consumer appeal, the GPU use of text-prompt based diffusion AI art systems also requires thoughtful considerations. Given the recent explosion in the number of highly sophisticated generative art systems and their rapid adoption by consumers and creative professionals, the impact of these systems on the climate needs to be carefully considered. In this work, we report on the growth of diffusion-based visual AI systems, their patterns of use, growth and the implications on the climate. Our estimates show that the mass adoption of these tools potentially contributes considerably to global energy consumption.
<br> 

<br>


<div id="paperSection"></div>


**------  PAPERS: AI Ethics: Gender ------**

{% for publi in site.data.publist %}
  {% if publi.research contains 'aiEthics' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

