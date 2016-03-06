import urllib

def get_page(seed_page):
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



def get_all_links_tocrawl(content):
    #input as string content and output as
    #all the links in a list
    tocrawl=[]
    while True:
        url,end_quote=find_next_url(content)
        if url:
            tocrawl.append(url)
            content=content[end_quote:]
        else:
            break
    return tocrawl

seed_page="http://xkcd.com/"

print get_all_links_tocrawl(get_page(seed_page))
# print get_all_links_tocrawl(get_page("http://www.xuexiguangchang.com/"))








