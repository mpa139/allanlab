---
title: "STMI Lab - Home"
layout: homelay
excerpt: "STMI Lab at Texas A&M University."
sitemap: false
permalink: /
---

The STMI lab (pronounced stem-ee) was formed to develop truly integrative end-to-end solutions of smart systems to improve patient care and patient lives. This involves a deep understanding of embedded systems design to develop data collection systems to monitor and empower users, advanced data mining and machine learning modeling to understand the complex, longitudinal data collected, and clinical outcomes research to understand the long-term trajectories and risks patients have for a variety of conditions. This unique blend of multi-disciplinary research provides challenges and opportunities through our partnerships that can provide solutions that drive tangible impact on the quality of life and quality of care.

At its core, these problems require understanding the theoretical properties of the platforms as well as the data. Developing new models to interpret and improve clinical understanding and motivating the collection of new data leads to challenges in systems design, power, communication, and user interface design. In isolation, each field might provide solutions that can be adapted to the others, but by focusing on the end-to-end aspect of our designs, we explore the creation of systems that bridge theoretical gaps in each field as well as the gaps in multi-disciplinary adoption of these technologies.


<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="5000" data-pause="hover" >
    <!-- Menu -->
    <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
        <li data-target="#carousel" data-slide-to="6"></li>
    </ol>

    <!-- Items -->
    {% assign first_image = true %}
    <div class="carousel-inner" markdown="0">
        {% for image in site.static_files %}
          {% if image.path contains 'images/home_slider' %}
            {% if first_image %}
              <div class="item active">
                <img src="{{ site.url }}{{ site.baseurl }}{{ image.path }}" alt="{{ forloop.index }}" />
              </div>
              {% assign first_image = false %}
            {% else %}
              <div class="item">
                <img src="{{ site.url }}{{ site.baseurl }}{{ image.path }}" alt="{{ forloop.index }}" />
              </div>
            {% endif %}
          {% endif %}
        {% endfor %}
    </div>
  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>




At its core, these problems require understanding the theoretical properties of the platforms as well as the data. Developing new models to interpret and improve clinical understanding and motivating the collection of new data leads to challenges in systems design, power, communication, and user interface design. In isolation, each field might provide solutions that can be adapted to the others, but by focusing on the end-to-end aspect of our designs, we explore the creation of systems that bridge theoretical gaps in each field as well as the gaps in multi-disciplinary adoption of these technologies.

 **We are  looking for passionate new PhD students, Postdocs, and Master students to join the team** [(more info)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


We are grateful for funding from Leiden University, [NWO](www.nwo.nl) ([Vidi talent scheme](http://www.nwo.nl/en/research-and-results/programmes/Talent+Scheme) and the [Frontiers in Nanoscience program](https://www.universiteitleiden.nl/en/research/research-projects/science/frontiers-of-nanoscience-nanofront)), and from an [ERC starting grant](https://erc.europa.eu/funding/starting-grants).
