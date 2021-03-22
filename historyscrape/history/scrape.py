

def scrape_fun(search_item):
    from bs4 import BeautifulSoup
    import requests
    name=search_item
    
    dicti={}
    req=requests.get('https://en.wikipedia.org/w/index.php?search=History+of+{}&title=Special%3ASearch&fulltext=1&ns0=1'.format(name))
    soup=BeautifulSoup(req.content,features="html.parser")

    all_results=soup.find_all("ul",{"class":"mw-search-results"})
    
    for val in all_results:
        a=val.find_all("a")
        for link in a:
            title=link['title'] 
            lin=link['href']
            dicti.__setitem__(title,lin)
    return dicti


      
def detailInfo(link):
    list_text=[]
    from bs4 import BeautifulSoup
    import requests
    
    url_link=(f"https://en.wikipedia.org{link}")
    request_agn=requests.get(url_link)
    soup2=BeautifulSoup(request_agn.content,features="html.parser")
    x=soup2.find_all("div",{"class":"mw-parser-output"})
    sel=soup2.select("p:nth-child(6)")
    for i in sel:
        first_para=i.text
        list_text.append(first_para)

    return list_text

    
    #mw-content-text > div.mw-parser-output > p:nth-child(6)
    
    
        
    
        

        


        
        




        