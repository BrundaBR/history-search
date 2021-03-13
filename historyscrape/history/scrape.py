

def scrape_fun(nam):
    from bs4 import BeautifulSoup
    import requests
    name=nam
    lis=[]
    lis_2=[]
    req=requests.get('https://en.wikipedia.org/w/index.php?search=History+of+{}&title=Special%3ASearch&fulltext=1&ns0=1'.format(name))
    soup=BeautifulSoup(req.content,features="lxml")

    all_results=soup.find_all("ul",{"class":"mw-search-results"})
    for val in all_results:
        a=val.find_all("a")
        for link in a:
            title=link['title'] 
            lin=link['href']
            lis.append(title)

    for i in lis[0:4]:

        request_agn=requests.get("https://en.wikipedia.org/w/index.php?search={}".format(i))
        soup2=BeautifulSoup(request_agn.content,features="lxml")
        x=soup2.find_all("p")
        for i in x:
            context=i.text
            lis_2.append(context)
    dicti={}
    dicti.__setitem__(lis[0],lis_2[0])
    return dicti

      
    
        

        


        
        




        