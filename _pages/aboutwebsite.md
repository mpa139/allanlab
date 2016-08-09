---
title: "Home"
layout: textlay
excerpt: "About the website."
sitemap: false
permalink: /aboutwebsite.html
---

# Make your own Jekyll website for your academic research group

This website is powered by [Jekyll](https://jekyllrb.com) and some [Bootstrap](www.getbootstrap.com), [Bootswatch](www.bootswatch.com). We tried to make it simple yet adaptable, so that it is easy for you to re-use it for your purpose. 

All pages are written in markdown for easy editing, and [Jekyll](https://jekyllrb.com) uses Liquid for the data-driven pages. The publicaion list, news items, and group members are stored as *.yml* data sheets (plain text) in the _data folder, so that one can update the website easily. The pages are in the _pages folder. Updating and maintaining is easy using github (not worldpress-easy, but there are other advantages (see e.g. [this](https://www.taniarascia.com/make-a-static-website-with-jekyll/), or [this](http://www.webdesignerdepot.com/2015/11/jekyll-against-the-rest-of-the-world/)).

If you never used [Jekyll](https://jekyllrb.com), read the [wikipedia article](https://en.wikipedia.org/wiki/Jekyll_(software)) article and check out their website. Same for Github, which will host your first website draft. 

Next, open your github account, go to our repository (), and click 'fork'. This is now your copy of the website, and you can change and adapt it as you want. You don't have to link to us or mention us (but of course we appreciate it). Then change the name of the "branch" to "gh-pages".  Your website is automatically published under your_username.github.io/your_username/. Except that it probably still looks like our website. 

To modify the webpage, you can either do everything on on github.com (go to a file, click "edit", then "commit", "push"), without installing [Jekyll](https://jekyllrb.com) on your computer, or have a local copy on your computer to play with.  The former is much easier in the beginning, but a bit less convenient once you start rewriting everythint. To get it to work on your computer (and to learn a bit more about [Jekyll](https://jekyllrb.com)), [here](https://www.taniarascia.com/make-a-static-website-with-jekyll/) and [here](https://scotch.io/tutorials/getting-started-with-jekyll-plus-a-free-bootstrap-3-starter-theme) are tutorials on how to use it and how set it up locally. Also, consider using the Github desktop app, I found it helpful.  

Now let's make this *your* website. First, go to the news.ylm, publist.ylm, and team.ylm files in the _data folder and insert your own data into the data fields. Watch out: these [Jekyll](https://jekyllrb.com) is quite strict about extra or missing spaces etc. In the beginning, test each change: commit, push, and check the published website.

For publications, you can add a "1" in the highlight field, then it will be featured prominently. You can add important  news items (red, "news1"), and less important  news items (blue, "news2").

For the news items, just keep adding them. The first 10 will be displayed on the 'home' page.

For the team *.ylm* file

Next, change the footer appropriately (in *_include*).

You might also want to change the style or theme. I imported style files (in sass) from Bootstrap/Bootwatch, you can replace them with your own (in the _sass directory). For small changes, just work on the override stuff in the main.sass file. Or change some variables in the _variables.sass file, like the background color etc. 

In the end, either upload the files in hte _site folder (that's the website [Jekyll](https://jekyllrb.com) generated) to your server, or buy yourself a domain and check the instructions on github.

Comments welcome.

Code released under the MIT License.

