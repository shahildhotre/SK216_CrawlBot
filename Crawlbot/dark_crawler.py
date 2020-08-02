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
import time
from stem import Signal
from stem.control import Controller
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from bs4.element import Comment
import pandas as pd
import sys

import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from keras.preprocessing.text import Tokenizer
from sklearn.feature_extraction.text import CountVectorizer

import mysql.connector
from mysql.connector import Error

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import wordnet as wn
#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')
#nltk.download('punkt')
#nltk.download('wordnet')

import warnings
warnings.filterwarnings("ignore")

keyword = ''
for word in sys.argv[:-1]:
    keyword += word + ' '
number = int(sys.argv[-1])
print(keyword)
'''
keyword = 'hello.py porn'
number = 1
'''
###############################################################################
'''add time delay between each request to avoid DOS attack'''
wait_time = 1

'''socks proxies required for TOR usage'''
proxies = {'http' : 'socks5h://127.0.0.1:9050', 'https' : 'socks5h://127.0.0.1:9051'}

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
        controller.authenticate(password="Mihir@1998")
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
        print("Page has found....")
        return True

###############################################################################
def link_content(mytxt):
    p_loc=0
    souplink_loc=0
    link_tag=[]
    hyperlink=[]
    countol=0
    count_anchor=0
    loc=0
    loc1 = -1
    loc2 = -1
    loc3 = -1
    loc4 = -1
    loc5=-1
    loc_link =[]
    loc_a= []
    loc_aclose= []
    local_context_link = []
    local_tag= []
    loc_p = []
    loc_pclose =[]
    newloc_link=[]
    tag_zip=[]
    range_a=[]
    link_para=[]
   # new_string = ""
    addlink=""
    souplink=""

    soup = BeautifulSoup(mytxt, 'lxml')
    string=str(soup)
    anchor = soup.findAll('a')
    p_loc=string.find('<p')
    for l in anchor:
        souplink_loc=string.find(str(l))

        if souplink_loc > p_loc:
            link_tag.append(l.text)
            hyperlink.append(l.get('href'))
            count_anchor=count_anchor+1

    for i in range(0, count_anchor):
                inner=[]
                inner.append(hyperlink[i])
                inner.append(link_tag[i])
                tag_zip.append(inner)

    para = soup.find_all('p')
    string = str(para)
    occurence=string.count('href')
    val=-1
    for i in range(0, occurence):
                val=string.find('href', val+1)

    occurence_a=string.count('</a>')

    for i in range(0, occurence_a):
                loc1=string.find('<a', loc1+1)
                loc_a.append(loc1)

    for i in range(0, occurence_a):
                loc2=string.find('</a>', loc2+1)
                loc_aclose.append(loc2)

    for i in range(0, occurence_a):
                inner=[]
                inner.append(loc_a[i])
                inner.append(loc_aclose[i])
                range_a.append(inner)
    sort_range_a=sorted(range_a, reverse=True)

    for i in tag_zip:
                if i[0] != "/" and i[0] != None and i[0] != "":
                    addlink="href="+'''"'''+i[0]+'''"'''
                    loc=string.find(addlink)
                    if loc != -1:
                        loc_link.append(loc)
                        destlink=urllib.parse.urljoin(response.url, i[0])
                        local_context_link.append(destlink)
                        local_tag.append(i[1])
                        countol=countol+1

    if countol==0:
        print('no local context is found')
    else:
        for i in range(0, countol):
                    inner=[]
                    inner.append(loc_link[i])
                    inner.append(local_context_link[i])
                    inner.append(local_tag[i])
                    link_para.append(inner)

    sort_link_para=sorted(link_para, reverse=True)

    for j in sort_range_a:
            for k in sort_link_para:
                    if j[0] < k[0] < j[1]:
                        string=(string[0:j[0]:]+'($$$)'+ string[j[1]+4::])

    occurence_p=string.count('</p>')
    for i in range(0, occurence_p):
                loc3=string.find('<p', loc3+1)
                loc_p.append(loc3)

    for i in range(0, occurence_p):
                loc4=string.find('</p>', loc4+1)
                loc_pclose.append(loc4)

    range_p = set(zip(loc_p, loc_pclose))
    sort_range_p =sorted(range_p, reverse=True)

    for i in range(0, occurence):
                loc5=string.find('($$$)', loc5+1)
                newloc_link.append(loc5)

    newlink_para=set(zip(newloc_link, local_context_link, local_tag))
    sort_newlink_para=sorted(newlink_para, reverse=True)
    l1 = []
    l2 = []
    l3 = []
    for l in sort_range_p:
            for m in sort_newlink_para:
                if l[0] < m[0] < l[1]:

                        newstring=string[l[0]:l[1]:]

                        l1.append(m[1])
                        l2.append(m[2])
                        l3.append(newstring)

    '''append rest of the links '''
    for i in tag_zip:
        l1.append(i[0])
        l2.append(i[1])
        l3.append('')

    '''craetion of dataframe'''
    d = {"link":l1, "anchor_text":l2, "local_text":l3}
    dfs = pd.DataFrame(data=d)


    '''remove whitespaces and newline characters'''
    for ind in dfs.index:
        dfs['anchor_text'][ind] = re.sub('\t', '', dfs['anchor_text'][ind])
        dfs['anchor_text'][ind] = re.sub('\n', '', dfs['anchor_text'][ind])

    return dfs

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
def ANN_FOR_ANCHOR(df_test,df_train):
    corpus=[]

    def PreprocessingOfText(input_text):
        input_text = [input_text[0].lower()]
        input_text = word_tokenize(input_text[0])
        tag_map = defaultdict(lambda : wn.NOUN)
        tag_map['J'] = wn.ADJ
        tag_map['V'] = wn.VERB
        tag_map['R'] = wn.ADV

        Final_words = []
        word_Lemmatized = WordNetLemmatizer()
        for word, tag in pos_tag(input_text):
            if word not in stopwords.words('english') and word.isalpha():
                word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
                Final_words.append(word_Final)
        Final_string = ' '.join(Final_words)
        return Final_string

    def preprocess(text):
        l_new=['jhj']
        review = [re.sub('[^a-zA-Z]', ' ', text[0])]
        l_new[0]=review
        review = PreprocessingOfText(l_new[0])
        corpus.append(review)
        return corpus

    for i in range(len(df_test)):
        pr=preprocess([df_test["anchor_text"][i]])

    x=df_train.Contents
    cv = CountVectorizer(max_features = 1500)
    X = cv.fit_transform(x).toarray()
    test=cv.transform(pr).toarray()
    print("1")
    model=load_model(r"Processed_ANN_weights.hdf5")
    print("2")
    pred=model.predict(test)
    print("3")
    df_test["Predictions"]=pred

    for i in range(len(df_test)):
        if len(df_test["anchor_text"][i]) == 0:
            df_test["Predictions"][i]=0

    return df_test

###############################################################################
def ANN_FOR_PAGE(text,df_train):
    corpus=[]

    def PreprocessingOfText(input_text):
        input_text = [input_text[0].lower()]
        input_text = word_tokenize(input_text[0])
        tag_map = defaultdict(lambda : wn.NOUN)
        tag_map['J'] = wn.ADJ
        tag_map['V'] = wn.VERB
        tag_map['R'] = wn.ADV

        Final_words = []
        word_Lemmatized = WordNetLemmatizer()
        for word, tag in pos_tag(input_text):
            if word not in stopwords.words('english') and word.isalpha():
                word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
                Final_words.append(word_Final)
        Final_string = ' '.join(Final_words)
        return Final_string

    def preprocess(text):
        l_new=['jhj']
        review = [re.sub('[^a-zA-Z]', ' ', text[0])]
        l_new[0]=review
        review = PreprocessingOfText(l_new[0])
        corpus.append(review)
        return corpus

    for i in range(len(text)):
        pr=preprocess(text)

    x=df_train.Contents
    cv = CountVectorizer(max_features = 1500)
    X = cv.fit_transform(x).toarray()
    test=cv.transform(pr).toarray()
    model=load_model("Processed_ANN_weights.hdf5")
    pred=model.predict(test)
    return float(pred)

###############################################################################
try:
    import requests.packages.urllib3
    requests.packages.urllib3.disable_warnings()
except:
    pass

###############################################################################
try :
    '''import word corpus of pornography'''
    df_train=pd.read_csv('fin_processed.csv')
    df_train.drop(['Unnamed: 0'],axis=1,inplace=True)

    '''obtain seed urls'''
    query = keyword

    '''ahmia search engine'''
    url = 'http://tordex7iie7z2wcg.onion/search?query=' + query[16:] + '&action=search'

    ua = UserAgent()
    user_agent = ua.random
    headers = {'User-Agent': user_agent}
    r = requests.get(url, proxies = proxies, headers = headers)
    body = html.fromstring(r.content)
    links = body.xpath('//h5/a/@href')


    '''seed urls list'''
    num_seed_urls = 10
    seed_list = links

    '''main url queue'''
    urlq = collections.deque()
    for seed_url in seed_list :
        seed_url = seed_url.split('url=')[-1]
        urlq.append(seed_url)
        print(seed_url)
        print("#"*20)
###############################################################################
    '''Database Connection'''
    connection = mysql.connector.connect(host='localhost',
                                         port=3308,
                                         database='sih',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()

###############################################################################
    found = set()
    total_links = set()
    home = set()
    crawled = set()
    count = 0
    depth = 20
    mihir = number
    countlink = 0
    countpage = 0
    '''threshold value to check relevancy'''
    threshold = 0.3
    sql_dark = """INSERT INTO dark(`link_url`, `link_status`) VALUES(%s,%s)"""
    while len(urlq):
        try:

            '''pop url from queue'''
            url = urlq.popleft()
            if url in crawled:
                continue
            crawled.add(url)
            '''IP spoofing'''
            current_ip = get_current_ip()
            print("Your IP is:  ", current_ip)
            print("You are on site " + str(countpage) +" :    "+ url)
            '''if link is active, visit link '''
            if is_alive(url):
                '''user agent spoofing'''
                ua = UserAgent()
                user_agent = ua.random
                headers = {'User-Agent': user_agent}
                print("User Agent is :   ", user_agent)

                '''send request to given site'''
                response = requests.get(url, proxies = proxies, headers = headers)
                body = html.fromstring(response.content)
                result = etree.tostring(body, pretty_print=True, method="html")

                '''links availab on current web page'''
                links = [urllib.parse.urljoin(response.url, url) for url in body.xpath('//a/@href')]

                '''extracs page text'''
                page_text = [text_from_html(response.content)]
                #print(page_text)

                '''dataframe of link, anchor text, local context'''
                dfs = link_content(response.text)

                try :
                    ''''dataframe with score of anchor text'''
                    df_a_score = ANN_FOR_ANCHOR(dfs, df_train)

                    '''page score calculation'''
                    page_score = ANN_FOR_PAGE(page_text, df_train)

                    '''total link score calculation'''
                    final_score = []
                    for ind in df_a_score.index :
                        final_score.append(0.6*df_a_score['Predictions'][ind] + 0.4*page_score)

                    df_a_score['Final Score'] = final_score

                    '''link sorting according to final score'''
                    df_a_score.sort_values(by = ['Final Score'])


                    for ind in df_a_score.index:

                        '''if final score is greater than threshold , page is relevant'''
                        if df_a_score['Final Score'][ind] > threshold :
                            '''append links according to score'''
                            urlq.append(df_a_score['link'][ind])

                            '''adds homepage of crawled sites'''
                            home.add('/'.join(df_a_score['link'][ind].split("/")[0:3]))
                            '''list will be sent to mihir'''
                            s = df_a_score['link'][ind]
                            if s.find("onion") > 0 and s not in found:
                                found.add(df_a_score['link'][ind])
                                total_links.add(df_a_score['link'][ind])
                                cursor.execute(sql_dark,(df_a_score['link'][ind],'Active',))
                                connection.commit()
                                print("count = " + str(len(found)))

                            print (str(countlink) +"{:<5}".format(" ")+ df_a_score['link'][ind], end= "\n\n" )

                            if len(found) >= mihir*10:
                                break
                            '''total number of links'''
                            countlink += 1

                    '''total number of sites visited'''
                    countpage += 1

                except Exception as e:
                    print(str(e))
                    renew_tor_ip()
                    time.sleep(wait_time)
                    countpage += 1
                    continue
            else:
                if url not in total_links:
                    total_links.add(url)
                    cursor.execute(sql_dark,(url,'Inactive'))
                    connection.commit()
                    print("Inactive:  "+url)


            if len(found) >= mihir*10:
                break
            '''Obtain new IP using TOR'''
            renew_tor_ip()
            time.sleep(wait_time)
        except:
            continue
    print(total_links)
    df_send = pd.DataFrame(data = {'links of {}'.format(query[16:]):list(found)})
    df_send.to_csv('childporn.csv')

except Exception as e:
	print(str(e))
if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

###############################################################################
