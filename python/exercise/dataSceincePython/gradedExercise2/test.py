##### -- Imports -- #####
import requests
import re
from bs4 import BeautifulSoup

#### -- Variables -- #####
newsFront = 'https://www.bbc.com/news'
data = '''<div class="gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m"><div><a class="gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor" href="/news/world-us-canada-64740209"><h3 class="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text">US TV reporter and child killed in Florida attack</h3></a><p class="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary">Dylan Lyons is named as the journalist killed while reporting the fatal shooting of a woman in Orlando.</p></div><ul class="gs-o-list-inline gs-o-list-inline--divided gel-brevier gs-u-mt-"><li class="nw-c-promo-meta"><span class="gs-c-timestamp gs-o-bullet gs-o-bullet- nw-c-timestamp"><span class="gs-o-bullet__icon gel-icon"><svg viewbox="0 0 32 32"><polygon points="17,15.4 17,6 15,6 15,16.6 23.8,21.7 24.8,19.9"></polygon><path d="M16,4c6.6,0,12,5.4,12,12c0,6.6-5.4,12-12,12S4,22.6,4,16C4,9.4,9.4,4,16,4 M16,0C7.2,0,0,7.2,0,16c0,8.8,7.2,16,16,16 s16-7.2,16-16C32,7.2,24.8,0,16,0L16,0z"></path></svg></span><time class="gs-o-bullet__text date qa-status-date gs-u-align-middle gs-u-display-inline" data-datetime="4h" data-seconds="1677163623" datetime="2023-02-23T14:47:03.000Z"><span aria-hidden="true" class="qa-status-date-output">4h</span><span class="gs-u-vh">4 hours ago</span></time></span></li><li class="nw-c-promo-meta"><a aria-label="From US &amp; Canada" class="gs-c-section-link gs-c-section-link--truncate nw-c-section-link nw-o-link nw-o-link--no-visited-state" href="/news/world/us_and_canada"><span aria-hidden="true">US &amp; Canada</span></a></li></ul></div>'''

def getData(data):
    response = requests.get(data)
    contents = response.text
    return contents

def getSummary(m):
    m = re.search(r'<p(?:.*?)>.*<\/p>', m)
    m = m.group(0)
    return m

def Div(data):
    soup = BeautifulSoup(getData(data), 'html.parser')
    soupList = soup.find_all('div', class_='gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m') 
    lst = []
    for i in range (0, 4):
        print(getSummary(str(soupList[i])))

print(getSummary(data))
print(Div(newsFront))