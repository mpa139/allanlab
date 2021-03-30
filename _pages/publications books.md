---
title: "biLAB | Publications"
layout: gridlay
excerpt: "biLAB | Publications."
sitemap: false
permalink: /publications_books/
---


# Book Chapter

{% for book in site.data.books %}
---
  {{ forloop.index }} . {{ book.apa }} <br />

{% endfor %}