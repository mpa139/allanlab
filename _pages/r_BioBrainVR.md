---
title: "iVizLab - Research"
layout: textlay
excerpt: "iVizLab -- Research"
sitemap: false
permalink: /bioBrainVR/
---


# Bio & Brain Sensing with VR

RESEARCH :: See [Related papers](#paperSection) ::  Related Projects: [Publications]({{ site.url }}{{ site.baseurl }}/research)

Reseachers: Steve DiPaola, Meehae Song

**About:**
Our lab has extensive experience in using different sensing technology including eye tracking and facial emotion recognition (DiPaola et al 2013), as well as gesture tracking and bio sensing heart rate and EDA (Song & DiPaola, 2015) which both affect the generative system and can be used to understand the reception to the generated graphics (still, video, VR).

**The Research:**
Emotional facial tracking using camera and AI software. Motion, gesture and body tracking using overhead cameras and MS Kinect. Hand tracking via our own data gloves and Leap Controller. Eye tracking via our Pupil eye tracker. Bio sensing ( heart rate and EDA) via our Empatica E4 watch.

**Setup and Results:**
Some examples of our tracking systems. All our 2d, 3d and VR systems have an abstraction layer with software modules to support several advanced input technologies such as emotion tracking, motion tracking, and bio-sensors.

<br>

<iframe width="450" height="230" src="https://www.youtube.com/embed/MYZDRSRadaY?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/8mWX9cWJolQ?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/JaOKbKGkwVw?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/0FaDEymjxbg?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/7I3heXUNZ8U?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/rm7iR-WvHSM?rel=0" frameborder="0" allowfullscreen></iframe>
<iframe width="450" height="230" src="https://www.youtube.com/embed/I-sZEyvtsXk?rel=0" frameborder="0" allowfullscreen></iframe>


<div id="paperSection"></div>


<br><br>
**------  PAPERS: bioBrainVR  ------**


{% for publi in site.data.publist2 %}
  {% if publi.research contains 'biobrainVR' %}
  <pubtit>{{ publi.title }}</pubtit> by
  {{ publi.authors }} --   <pubtit>{{ publi.type }}</pubtit> -- {{ publi.description }}
  <br> <a href="{{ publi.url }}">{{ publi.display }}
  {% endif %}  
{% endfor %}

