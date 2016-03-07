import urllib

def get_page(url):
    # input as url and output as a string which is
    # the text of that page
    content=urllib.urlopen(seed_page).read()
    return content


def find_next_url(content):
    # a string as input,output the first url  and
    # end position of the url's closing quote
    start_pos=content.find("href",content.find("<a"))
    if start_pos==-1:
        return None,"no links found"
    first_quote=content.find('''"''',start_pos)
    end_quote=content.find('''"''',first_quote+1)
    url=content[first_quote+1:end_quote]
    return url,end_quote



def get_all_links(content):
    #input as string content and output as
    #all the links in a list
    links=[]
    while True:
        url,end_quote=find_next_url(content)
        if url:
            links.append(url)
            content=content[end_quote:]
        else:
            break
    return links

def crawl_web(seed_page):
    tocrawl=[seed_page]
    crawled=[]
    while len(tocrawl)>0:
        url=tocrawl.pop()
        if url not in crawled:
            crawled.append(url)
            tocrawl.extend(get_all_links(get_page(url)))
    return crawled

seed_page="http://xkcd.com/"
# seed_page="https://www.udacity.com/cs101x/index.html"
# print get_all_links(get_page(seed_page))
print crawl_web(seed_page)





























