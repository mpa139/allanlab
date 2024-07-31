---
title: "ALOHA LAB - People"
layout: gridlay
excerpt: "ALOHA LAB -- People"
sitemap: false
permalink: /team/
---

🔥 **We are looking for new students to join the team** [(see openings)]({{ site.url }}{{ site.baseurl }}/openings) **!**

# Faculty

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive avatar" width="25%" style="float: left" />
  <h3>{{ member.name }}</h3>
  <i class="lead text-muted">{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  <li style="font-size: 18px"> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  <li style="font-size: 18px"> {{ member.education3 }} </li>
  <li style="font-size: 18px"> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  <li style="font-size: 18px"> {{ member.education3 }} </li>
  <li style="font-size: 18px"> {{ member.education4 }} </li>
  <li style="font-size: 18px"> {{ member.education5 }} </li>
  {% endif %}

  </ul>
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


# Members

<!-- ## Students -->
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  {% if member.photo %}
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive avatar" width="25%" style="float: left" />
  {% endif %}
  <h4>{{ member.name }}</h4>
  <i class="lead text-muted">{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  <li style="font-size: 18px"> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  <li style="font-size: 18px"> {{ member.education3 }} </li>
  <li style="font-size: 18px"> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li style="font-size: 18px"> {{ member.education1 }} </li>
  <li style="font-size: 18px"> {{ member.education2 }} </li>
  <li style="font-size: 18px"> {{ member.education3 }} </li>
  <li style="font-size: 18px"> {{ member.education4 }} </li>
  <li style="font-size: 18px"> {{ member.education5 }} </li>
  {% endif %}

  </ul>
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

<!--

## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
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

## Former visitors, BSc/ MSc students
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

</div>


## Administrative and System Support
<a href="https://www.usf.edu/engineering/cse/people/staff.aspx">USF's Department of Computer Science and Engineering Staff</a>
-->
