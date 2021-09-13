import requests
import lxml.html



for offset in [0,10,20,30,40,50,60,70,80]:
  url = 'http://www.dblab.postech.ac.kr/home/announcements?offset={}'.format(offset)
  r = requests.get(url)

  tree = lxml.html.fromstring(r.text)

  announcements = tree.xpath('//div[@class="announcement"]')

  for announcement in announcements:
    headline = announcement.xpath('./h4/a')[0].text_content()
    timestamp = announcement.xpath('./span/span')[0].text_content().strip()
    #Mar 16, 2017,
    ws = timestamp.replace(',','').strip().split(' ')
    print('\n- date: {}. {} {}'.format(ws[1],ws[0],ws[2]))
    print('  headline: "{}"'.format(headline))
