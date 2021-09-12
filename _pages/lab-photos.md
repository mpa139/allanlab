---
title: "NDS Lab - Pictures"
layout: piclay
excerpt: "NDS Lab -- Pictures"
permalink: /lab-photos/
---

# NDS Lab Photos

## NDS Lab and friends end of Summer 2021 BBQ

<!-- 
#### Example youtube video:
<iframe width="560" height="315" src="https://www.youtube.com/embed/idhere......" frameborder="0" allowfullscreen></iframe>
-->

<!-- Gallery -->
{% assign number_printed = 0 %}
{% for pic in site.data.pictures_NDS %}

{% assign even_odd = number_printed | modulo: 1 %} 

<!-- 
Above was before "{% assign even_odd = number_printed | modulo: 4 %} " to have 3 per column 
-->

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/photos/{{ pic.image }}" class="img-responsive" width="95%" style="float: left" />
  <br>
  {{ pic.title }}
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd = 0 %} 
  
<!-- 
Above was before "{% if even_odd > 2 %} " 
-->
  
</div>
{% endif %}


{% endfor %}

{% assign even_odd = number_printed | modulo: 1 %} 

<!-- Above was before "{% assign even_odd = number_printed | modulo: 4 %} " to have 3 per column this below is no longer needed as we do </div> after each image 
-->

{% if even_odd == 1 %}
</div>
{% endif %}

{% if even_odd == 2 %}
</div>
{% endif %}

{% if even_odd == 3 %}
</div>
{% endif %}

<p> &nbsp; </p>

