# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 15:10:41 2020

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


    def TordexSeedCollector(self):
        
        query = '+'.join(self.query.split(' '))
        url = 'http://tordex7iie7z2wcg.onion/search?query={}&action=search'.format(query)
        
        try:
            response = requests.get(url, proxies = SeedUrlCollector.proxies, headers = SeedUrlCollector.headers)
            body = html.fromstring(response.content)
            seedurllist = body.xpath('//h5/a/@href')
        except:
            seedurllist = []
        return seedurllist
    
    
    def AhmiaSeedCollector(self):
        
        query = '+'.join(self.query.split(' '))
        url = 'http://msydqstlz2kzerdg.onion/search/?q={}'.format(query)
    
        try:    
            response = requests.get(url, proxies = SeedUrlCollector.proxies, headers = SeedUrlCollector.headers)
            body = html.fromstring(response.content)
            seedurllist = body.xpath('//h4/a/@href')
            seedurllist = [link.split('redirect_url=')[-1] for link in seedurllist]
        except:
            seedurllist = []
        return seedurllist
    
    
    def TorchSeedCollector(self):
        
        query = '+'.join(self.query.split(' '))
        url = 'http://xmh57jrzrnw6insl.onion/4a1f6b371c/search.cgi?s=DRP&q={}&cmd=Search'.format(query)
        
        try:    
            response = requests.get(url, proxies = SeedUrlCollector.proxies, headers = SeedUrlCollector.headers)
            body = html.fromstring(response.content)
            seedurllist = body.xpath('//dl/dt/a/@href')
        except:
            seedurllist = []
        return seedurllist
    
    
    def OnionlandSeedCollector(self):
        
        query = '+'.join(self.query.split(' '))
        url = 'http://3bbaaaccczcbdddz.onion/search?q={}'.format(query)
        
        try:
            response = requests.get(url, proxies = SeedUrlCollector.proxies, headers = SeedUrlCollector.headers)
            body = html.fromstring(response.content)
            seedurllist = body.xpath('//div[@class="link"]/text()')
            seedurllist = list(filter(lambda x : x != '\n', seedurllist))
            seedurllist = [url.split('\n')[1] for url in seedurllist]
        except:
            seedurllist = []
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
ahmialinks = suc.AhmiaSeedCollector()
tordexlinks = suc.TordexSeedCollector()
ollinks = suc.OnionlandSeedCollector()
torchlinks = suc.TorchSeedCollector()

seed_list = tordexlinks + ahmialinks + ollinks + torchlinks

# main URL frontier
urlq = collections.deque()
# to save all the visited urls to avoid revisiting
found = set()

for link in seed_list:
    urlq.append(link)
    found.add(link)

###############################################################################
# number of pages to visit in one crawling session
countpage = 1

# number of total links harvested during crawling
countlink = 1

try:
    while (len(urlq) != 0 and countpage != 50) :
        
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
            
            for link in links:
                if link not in found:
                    urlq.append(link)
                    found.add(link)
                    
                    print (str(countlink) +"{:<5}".format(" ")+ link, end= "\n\n" )
                    countlink += 1
                    
        '''Obtain new IP using TOR'''
        renew_tor_ip()
        
            
except Exception as e:
	print(str(e))

###############################################################################
