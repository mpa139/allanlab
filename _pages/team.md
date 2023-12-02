---
title: "NeuroergoLab - Team"
layout: gridlay
excerpt: "NeuroergoLab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

 **We are  looking for new PhD students, Postdocs, and Master students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/vacancies) **!**


<!-- Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors). -->

<img src="{{ site.url }}{{ site.baseurl }}/assets/lab_2021.png" class="img-responsive" style="float: center" />

## Lab Director


<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/mehta2.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-10 clearfix">
  <a href="https://directory.engr.wisc.edu/ie/Faculty/Mehta_Ranjana/">Ranjana Mehta</a> is a Professor in the Department of Industrial and Systems Engineering at University of Wisconsin-Madison. She is also a graduate faculty with the Texas A&M Institute for Neuroscience at Texas A&M University, director of the NeuroErgonomics Laboratory, co-director of the Texas A&M Ergonomics Center, and a faculty fellow with the Center for Population Health and Aging and the Center for Remote Health Technologies and Systems. She received her MS and Ph.D. from Virginia Tech, MEng from University at Buffalo, and BE from Mumbai University.

She is the recipient of:
* **Fellow**, Human Factors and Ergonomics Society, 2023
* **The Human Factors Prize**, Human Factors and Ergonomics Society, 2022
* **NASA ideas* Fellow**, 2022
* **Technical Innovation**, the Institute of Industrial and Systems Engineers, 2022
* **Presidential Impact Fellow**, Texas A&M University, 2021
* **Virginia Tech Engineering Outstanding Recent Alumni Award**, Virginia Tech, 2020
* **TEES Engineering Genesis Award**, Texas A&M University, 2020
* **TEES Faculty Fellow**, Texas A&M University, 2020
* **HFE WOMAN of the Year**, Human Factors and Ergonomics Society, 2019
* **Creativeness in Ergonomics Practitioner of the Year Award**, Applied Ergonomics Society (IISE), 2019
* **William C. Howell Young Investigator Award**, Human Factors and Ergonomics Society, 2017
* **James G. Zimmer New Investigator Research Award**, American Public Health Association, 2014
</div>
</div>


## Ph.D. Students


<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/zhang.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-10 clearfix">
  <p>
    <a href="https://www.linkedin.com/in/yinsuzhang/">Yinsu Zhang</a> has a BS in Mechanical Engineering from Rensselaer Polytechnic Institute and MS in Mechanical Engineering from Texas A&M University. His research interests are in human-automation interactions and in objective measures of dynamic driver trust in autonomous vehicles.
  </p>
</div>
</div>

<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/yadav.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-10 clearfix">
  <p>
    <a href="https://www.linkedin.com/in/nimrobotics/">Aakash Yadav</a> has a B.Tech. in Mechanical Engineering from the Indian Institute of Technology Tirupati. His research interests span robotics, human-robot interaction, human factors, cognition, neuroergonomics, and affective computing. Aakash works towards understanding the teaming between robots and humans to improve the combined system performance, efficiency, and safety. He loves to walk, bike, hike, and canoe in his free time.
  </p>
</div>
</div>

<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/tiash.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-10 clearfix">
  <p>
    <a href="https://www.linkedin.com/in/tiashranamukherjee/">Tiash Rana Mukherjee</a> has a B.Tech Degree in Production Engineering from the National Institute of Technology in Agartala, India. Her research interests lie in the intersection of Mechanical Design and Cognitive Psychology. She is aiming for an Applied Research career in the Industry.
  </p>
</div>
</div>

<div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/david.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-10 clearfix">
  <p>
    <a href="https://www.linkedin.com/in/david-nartey/">David Nartey</a> has a BS in Mechanical Engineering with a minor in Chemistry from Florida Institute of Technology. He worked in the automotive industry for 3 years. His research interests include general A.I, machine learning, systems engineering, cognition, and wearable health technology. In his free time, he enjoys working out, watching animation, and traveling.
  </p>
</div>
</div>

<!-- ## Masters Students -->



<!-- ## Staff -->

<!-- <div class="row">
<div class="col-sm-2 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/assets/people/lindsey.jpeg" class="img-responsive" width="100%" style="float: center"/>
</div>
<div class="col-sm-10 clearfix">
  <p>
    <a href="https://www.linkedin.com/in/lindsey-brenner-a7a513183/">Lindsey Brenner</a> is a Project Coordinator for the NeuroErgonomics Laboratory and is the project manager for the NSF-funded Convergence-Accelerator initiative — Track B: AI and the Future of Work (LEARNER). Lindsey graduated from Texas A&M University with a bachelor’s degree in Political Science.
  </p>
</div>
</div> -->


## Alumni

<h3>Ph.D.</h3>
{% for member in site.data.alumni_phd %}
<a href="{{ member.web }}">{{ member.name }}</a>, {{ member.degree }}, {{ member.info }} <br>
{% endfor %}

<h3>Masters</h3>
{% for member in site.data.alumni_masters %}
<a href="{{ member.web }}">{{ member.name }}</a>, {{ member.degree }}, {{ member.info }} <br>
{% endfor %}

<h3>Visiting Scholars</h3>
{% for member in site.data.alumni_visitors %}
{{ member.name }}, {{ member.info }}, {{ member.time }}
{% endfor %}

<h3>Staff</h3>
{% for member in site.data.alumni_staff %}
<a href="{{ member.web }}">{{ member.name }}</a>, {{ member.info }}, {{ member.time }} <br>
{% endfor %}

<h3>Undergraduate</h3>
{% for member in site.data.alumni_ug %}
{{ member.name }}, {{ member.major }}, {{ member.time }} 
{% endfor %}

