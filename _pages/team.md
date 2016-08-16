---
title: "Team"
layout: gridlay
excerpt: "Allan Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

Jump to [staff](#staff), [master and bachelor students](#master-and-bachelor-students), [alumni](#alumni), [administrative support](#administrative-support), [lab visitors](#lab-visitors).


{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Staff
<div class="row">
<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/Milan.png" class="img-responsive" width="25%" style="float: left" />
<h4>Milan P Allan</h4>
<p><em>Assistant Professor, started Jan 2015 
<br> email: <milan.allan@gmail.com></em></p>
    
<ul style="overflow: hidden">
<li>Master ETHZ, Diplomarbeit with <a href="http://www.physik.uzh.ch/groups/osterwalder/">J Osterwalder</a>, University of Zurich</li>
<li>PhD St Andrews (and Cornell University) with <a href="http://dpmc.unige.ch/gr_baumberger/index.html">Felix Baumberger</a> and <a href="http://davisgroup.lassp.cornell.edu/">JC Davis</a></li>
<li>Postdoc Cornell</li>
<li><a href="http://www.ethfellows.ethz.ch/">ETH fellow</a> at ETHZ with Andreas Wallraff</li>
</ul>
  </div>

  <div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/irene.jpg" class="img-responsive" width="25%" style="float: left" />
<h4>Irene Battisti</h4>
<p><em>PhD student, started Jan 2015 <br> email: <Battisti@Physics.LeidenUniv.nl></em></p>
<ul style="overflow: hidden">
<li>Master Padova University</li>
<li>Master thesis at Leiden University with <a href="https://www.physics.leidenuniv.nl/vanruitenbeek">Jan van Ruitenbeek</a></li>
</ul>
</div>
</div>

<div class="row">
<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/Koen.jpg" class="img-responsive" width="25%" style="float: left" />
<h4>Koen M Bastiaans</h4>
<p><em>PhD Student, started Sep 2015 <br> email: <Bastiaans@Physics.LeidenUniv.nl></em></p>
<ul style="overflow: hidden">
<li>Master Leiden University with Milan Allan</li>
</ul>
</div>

<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/Vitaly.JPG" class="img-responsive" width="25%" style="float: left" />
<h4>Vitaly Fedoseev</h4>
<p><em>PhD Student, started Jan 2016 <br> email: <VFedoseev@Physics.LeidenUniv.nl></em></p>
<ul style="overflow: hidden">
<li>Master Cambridge University</li>
<li>BSc Moscow Institute of Physics and Technology</li>
</ul>
</div>
</div>

<div class="row">
<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/Maarten.png" class="img-responsive" width="25%" style="float: left" />
<h4>Maarten Leeuwenhoek</h4>
<p><em>PhD Student, shared with the <a href="http://www.groeblacherlab.tudelft.nl">Groeblacher lab</a> at TU Delft under a NanoFront grant. Maarten currently works in the cleanroom in Delft. <br> email: <M.Leeuwenhoek@tudelft.nl></em></p>
<ul style="overflow: hidden">
<li>Master Leiden University with Milan Allan</li>
</ul>
</div>

<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/verdoes.jpg" class="img-responsive" width="25%" style="float: left" />
<h4>Gijsbert Verdoes</h4>
<p><em>Fine mechanical engineer associated with the FMD, currently working in our group</em></p>
<ul style="overflow: hidden">
<li>Leidse instrumentmakers School</li>
</ul>
</div>
</div>

<div class="row">
<div class="col-sm-6 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/Kees.jpg" class="img-responsive" width="25%" style="float: left" />
<h4>Kees van Oosten</h4>
<p><em>Fine mechanical engineer associated with the FMD, currently working in our group</em></p>
<ul style="overflow: hidden">
<li>Leidse instrumentmakers School</li>
<li>Associate degree Mechanical Engineering, Hogeschool Arnhem Nijmegen</li>
</ul>
</div>
</div>

## Master and Bachelor Students 
<p>Tjerk Benschop, Alexander Vanstone</p>

## Alumni
<p>Oliver Ostojic (Master student, 2016), Arjo Andringa (Bachelor student, 2016), Nikolaos Iliopoulos (visitor, 2016), Daniëlle van Klink (Bachelor student, 2016), Farshaad Hoeseni (Master student, 2015)</p>

## Administrative Support
<p><a href="mailto:Rijsewijk@Physics.LeidenUniv.nl">Ellie van Rijsewijk</a> is helping us (and other groups) with administration.</p>

## Lab Visitors
<p><a href="http://stanford.edu/~safavi/">Amir Safavi-Naeini</a> (Stanford), <a href="http://www.ru.nl/spm">Alexander Ako Khajetoorians</a> (Radboud University), <a href="http://www.mhamidian.com">Mohammad Hamidian</a> (Harvard->UC Davis), <a href="https://www.bnl.gov/cmpmsd/mbe/default.asp">Ivan Bozovic</a> (BNL / Yale), <a href="http://www.fmassee.nl">Freek Massee</a> (Paris)</p>
