---
title: "Allan Lab - Publications"
layout: gridlay
excerpt: "Allan Lab -- Publications."
sitemap: false
permalink: /publications/
---

<br />
# Publications

## Highlights

(For a full list see [below](#full-list) or go to [Google Scholar](https://scholar.google.ch/citations?user=TqxYWZsAAAAJ), [ResearcherID](https://www.researcherid.com/rid/D-7763-2012))

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

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

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


## All publications

<p id="demo" ></p>

<Script>

//From "http://www.alexhadik.com/blog/2014/6/12/create-pubmed-citations-automatically-using-pubmed-api" adapted from reply to blog post by Les Ansley

var HTMLpublication = '<b>\%title%\</b><br />%authors%<br /><b><a href="%data%"target="_blank">%journal%\</b></a> (%date%) %volume%</b> %issue%%pages%</br></br>' //Formats output

var publications, idStringList;
var pubmedSearchAPI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?";
var pubmedSummaryAPI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?";
var database = "db=pubmed";
var returnmode = "&retmode=json";
var returnmax = "&retmax=100";
var searchterm = "&term=Roychoudhuri R[Author])";
var returntype = "&rettype=abstract";
var idURL = pubmedSearchAPI + database + returnmode + returnmax + searchterm
console.log(idURL);

var getPubmed = function(url) { //passed url
    return new Promise(function(resolve, reject) {
        var xhr = new XMLHttpRequest();
        xhr.open('get', url, true);
        xhr.responseType = 'json';
        xhr.onload = function() {
            var status = xhr.status;
            if (status == 200) { //status 200 signifies OK (http://www.w3schools.com/ajax/ajax_xmlhttprequest_onreadystatechange.asp)
                resolve(xhr.response);
            } else {
                reject(status);
            }
        };
        xhr.send();
    });
};
getPubmed(idURL).then(function(data) {
    var idList = data.esearchresult.idlist;
    idStringList = idList.toString(); //converts the idlist to a string to be appended to the search url
    idStringList = '&id=' + idStringList;
    summaryURL = pubmedSummaryAPI + database + returnmode + returntype + idStringList;
    getPubmed(summaryURL).then(function(summary) {
        publications = formatReferences(summary);
        console.log(publications);	
		document.getElementById("demo").innerHTML = publications;
		
    }, function(status) {
        publications = 'Something went wrong getting the ids.';
    });
}, function(status) {
    publications = 'Something went wrong getting the ids.';
});


function formatReferences(summary) {
    var publicationList = '';
    for (refs in summary.result) {
        if (refs !== 'uids') {
            var authors = '';
            var publication = '';
            var authorCount = ((summary.result[refs].authors).length);
            var i = 0;
            while (i < authorCount - 1) {
                authors += summary.result[refs].authors[i].name + ', ';
                i++;
            }
            publication = HTMLpublication.replace('%data%', 'http://www.ncbi.nlm.nih.gov/pubmed/' + refs);
            authors += summary.result[refs].lastauthor;
            publication = publication.replace('%authors%', authors);
            publication = publication.replace('%title%', summary.result[refs].title);
            publication = publication.replace('%journal%', summary.result[refs].source);
            publication = publication.replace('%PMID%', summary.result[refs].uid);
            //Alter formatting if article is In Press
            if (summary.result[refs].volume !== '') {
                publication = publication.replace('%volume%', ' ' + summary.result[refs].volume);
                publication = publication.replace('%issue%', '(' + summary.result[refs].issue + ')');
                publication = publication.replace('%pages%', ': ' + summary.result[refs].pages + '. ');
                var date = summary.result[refs].pubdate.slice(0, 4);
                publication = publication.replace('%date%', date + '');
            } else {
                publication = publication.replace('%volume%', ' In Press');
                publication = publication.replace('%issue%', '.');
                publication = publication.replace('%pages%', '');
                publication = publication.replace('%date%', '');
            }
            publicationList = publication + publicationList;
        }
    }
    return (publicationList);
} 

</Script>

