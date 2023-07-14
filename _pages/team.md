---
title: "NeuroergoLab - Team"
layout: gridlay
excerpt: "Allan Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

 **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


<!-- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

<img src="{{ site.url }}{{ site.baseurl }}/assets/lab_2021.png" class="img-responsive" style="float: center" />

## Lab Director

<img src="{{ site.url }}{{ site.baseurl }}/assets/people/mehta.jpeg" class="img-responsive" width="25%" style="float: left" />

**Ranjana Mehta** is an Associate Professor in the Department of Industrial and Systems Engineering at Texas A&M University. She is also a graduate faculty with the Texas A&M Institute for Neuroscience at Texas A&M University, director of the NeuroErgonomics Laboratory, co-director of the Texas A&M Ergonomics Center, and a faculty fellow with the Center for Population Health and Aging and the Center for Remote Health Technologies and Systems. She received her MS and Ph.D. from Virginia Tech, MEng from University at Buffalo, and BE from Mumbai University.

She is the recipient of:
* Technical Innovation, the Institute of Industrial and Systems Engineers, 2022
* Presidential Impact Fellow, Texas A&M University, 2021
* Virginia Tech Engineering Outstanding Recent Alumni Award, Virginia Tech, 2020
* TEES Engineering Genesis Award, Texas A&M University, 2020
* TEES Faculty Fellow, Texas A&M University, 2020
* HFE WOMAN of the Year, Human Factors and Ergonomics Society, 2019
* Creativeness in Ergonomics Practitioner of the Year Award, Applied Ergonomics Society (IISE), 2019
* William C. Howell Young Investigator Award, Human Factors and Ergonomics Society, 2017
* James G. Zimmer New Investigator Research Award, American Public Health Association, 2014


## Ph.D. Students

<style>
  /* table {
    width: 100%;
  } */

  /* td {
    width: 25%;
  } */

  p {
    padding-left: 10px;
  }
</style>

<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/zhang.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-8 clearfix">
  <p>
    <strong>Yinsu Zhang</strong> has a BS in Mechanical Engineering from Rensselaer Polytechnic Institute and MS in Mechanical Engineering from Texas A&M University. His research interests are in human-automation interactions and in objective measures of dynamic driver trust in autonomous vehicles.
  </p>
</div>
</div>

<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/yadav.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-8 clearfix">
  <p>
    <strong>Aakash Yadav</strong> has a B.Tech. in Mechanical Engineering from the Indian Institute of Technology Tirupati. His research interests span robotics, human-robot interaction, human factors, cognition, neuroergonomics, and affective computing. Aakash works towards understanding the teaming between robots and humans to improve the combined system performance, efficiency, and safety. He loves to walk, bike, hike, and canoe in his free time.
  </p>
</div>
</div>

## Alumni

<h4>Ph.D.</h4>
{% for member in site.data.alumni_phd %}
<a href="{{ member.web }}">{{ member.name }}</a>, {{ member.degree }}, {{ member.info }} <br>
{% endfor %}

<h4>Masters</h4>
{% for member in site.data.alumni_masters %}
<a href="{{ member.web }}">{{ member.name }}</a>, {{ member.degree }}, {{ member.info }} <br>
{% endfor %}

<h4>Undergraduate</h4>
{% for member in site.data.alumni_ug %}
{{ member.name }}, {{ member.major }}, {{ member.time }} 
{% endfor %}

<h4>Visiting Scholars</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}, {{ member.info }}, {{ member.time }}
{% endfor %}