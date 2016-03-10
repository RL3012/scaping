# -*- coding: utf-8 -*-

import urllib

def get_page(url):
    try:
        content=urllib.urlopen(url).read()
        return content
    except:
        return ""


def find_next_url(content):
    start_link=content.find("<a")
    if start_link==-1:
        return None,0
    start_href=content.find("href",start_link)
    first_quote=content.find('''"''',start_href)
    end_quote=content.find('''"''',first_quote+1)
    url=content[first_quote+1:end_quote]
    return url,end_quote


def get_all_links(content):
    links=[]
    while True:
        url,end_quote=find_next_url(content)
        if url is not None:
            if len(url)>0:
                links.append(url)
            content=content[end_quote:]
        else:
            break
    return links

def union(p,q):
    #update list p without duplication
    for e in q:
        if e not in p:
            p.append(e)
    return q

def crawl_web(seed_page):
    tocrawl=[seed_page]
    crawled=[]
    index={}
    graph={}
    while tocrawl:
        url=tocrawl.pop()
        if url not in crawled:
            crawled.append(url)
            content=get_page(url)
            add_page_to_index(index, url, content)
            outlinks=get_all_links(content)
            graph[url]=[outlinks]
            union(tocrawl,outlinks)
    return index,graph


def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword]=[url]

def lookup(index,keyword):
    if keyword in index:
        return index[keyword]
    return None

def add_page_to_index(index,url,content):
    words=content.split()
    for word in words:
        add_to_index(index, word, url)

# myindex=[]
# add_to_index(myindex, "data", "www.data.com")
# print lookup(myindex, "data")

seed_page="https://www.udacity.com/cs101x/index.html"
myindex,mygraph=crawl_web(seed_page)
print mygraph




































