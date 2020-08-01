# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:59:35 2020

@author: Team CrawlBot
"""

import requests
from lxml import html,etree
import collections
import urllib.parse
from requests.exceptions import HTTPError
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import sys

###############################################################################

keyword = ''
for word in sys.argv[:-1]:
    keyword += word + ' '
number = int(sys.argv[-1])
print(keyword)
print(number)

###############################################################################
'''socks proxies required for TOR usage'''
proxies = { 'http' : 'socks5h://127.0.0.1:9050', 
            'https' : 'socks5h://127.0.0.1:9050'}

###############################################################################
def get_current_ip():
	try:
		r = requests.get('http://httpbin.org/ip', proxies = proxies)
	except Exception as e:
		print (str(e))
	else:
		return r.text.split(",")[-1].split('"')[3]

###############################################################################
def renew_tor_ip():
	with Controller.from_port(port = 9051) as controller:
		controller.authenticate(password="vjtifyp")
		controller.signal(Signal.NEWNYM)

###############################################################################
def is_alive(url):
    try:
        ua = UserAgent()
        user_agent = ua.random
        headers = {'User-Agent': user_agent}
        res = requests.get(url, proxies = proxies, headers = headers)
        res.raise_for_status()
    except HTTPError as http_err:
        print(" Page not found..." + url)
        return False
    except Exception as err:
        print("Page not found..." + url )
        return False
    else:
        print("Page found....")		
        return True
		
###############################################################################
def tag_visible(element):
    if element.parent.name in ['style', 'script','meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

###############################################################################
def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)  
    return u" ".join(t.strip() for t in visible_texts)

###############################################################################
    
class SeedUrlCollector():
    
    proxies = {'http' : 'socks5h://127.0.0.1:9050', 
               'https' : 'socks5h://127.0.0.1:9050'}
    
    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    
    def __init__(self, query):
        self.query = query


    def GoogleSeedCollector(self):
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        query = '+'.join(self.query.split(' '))
        url = "https://google.com/search?q={}".format(query)
        
        headers = {"user-agent": USER_AGENT}
        resp = requests.get(url, headers=headers)
        
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            seedurllist = []
            for g in soup.find_all('div', class_='r'):
                anchors = g.find_all('a')
                if anchors:
                    link = anchors[0]['href']
                    seedurllist.append(link)
        return seedurllist

###############################################################################

try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass
###############################################################################

from cfonts import render

output = render('Crawlbot', colors=['red', 'yellow'], align='center')
print(output)
print('\n\n')
###############################################################################
'''Setting up seed urls'''

query = 'child abuse'
    
# Create class object
suc = SeedUrlCollector(query)
# Call class methods
googlelinks = suc.GoogleSeedCollector()

# main URL frontier
urlq = collections.deque()
# to save all the visited urls to avoid revisiting
found = set()

for link in googlelinks:
    urlq.append(link)
    found.add(link)

###############################################################################
# number of pages to visit in one crawling session
countpage = 1

# number of total links harvested during crawling
countlink = 1

try:
    while (len(urlq) != 0 and countpage != number) :
        
        '''pop url from queue'''
        url = urlq.popleft()
                
        '''IP spoofing'''
        current_ip = get_current_ip()
        print("IP : {}".format(current_ip))
        print("{}. Crawling {}".format(str(countpage), url))
        

        '''if link is active, visit link '''
        if is_alive(url):
            
            countpage += 1
            
            '''user agent spoofing'''
            ua = UserAgent()
            user_agent = ua.random
            headers = {'User-Agent': user_agent}
            print("User Agent is : {}".format(user_agent))
                        
            '''send request to chosen site'''
            response = requests.get(url, proxies = proxies, headers = headers)
            body = html.fromstring(response.content)
            result = etree.tostring(body, pretty_print=True, method="html")
                        
            '''links availab on current web page'''
            links = [urllib.parse.urljoin(response.url, url) for url in body.xpath('//a/@href')]
            count_link = 0        
            for link in links:
                if count_link == 10:
                    break
                if link not in found:
                    urlq.append(link)
                    found.add(link)
                    
                    print (str(countlink) +"{:<5}".format(" ")+ link, end= "\n\n" )
                    countlink += 1
                    
        '''Obtain new IP using TOR'''
        renew_tor_ip()
            
    final_list = list(found)
    data = {'Links' : final_list}
    df = pd.DataFrame(final_list)
    df.to_csv('crawledlinks.csv', header= False)

    
    
except Exception as e:
	print(str(e))

###############################################################################
