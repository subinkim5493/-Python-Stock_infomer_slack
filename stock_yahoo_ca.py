import requests
from bs4 import BeautifulSoup
from slacker import Slacker


slack = Slacker('xoxp-1755680054612-1773354881968-1735933075271-bddbc87889c19bcc9de0a70812b8d89c')

# Send a message to #general channel
# slack.chat.post_message('#chat', 'subinkim!')



url = "https://ca.finance.yahoo.com/world-indices"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

names = soup.find_all("td", attrs = {"class" : "data-col1 Ta(start) Pend(10px)"})
symbol = soup.find("td",attrs = {"class" : "data-col0 Ta(start) Pstart(6px)"})


rank1_url = "https://ca.finance.yahoo.com/" + symbol.a["href"]
res_rank1 = requests.get(rank1_url)
res_rank1.raise_for_status()
soup_rank = BeautifulSoup(res_rank1.text,"lxml")
pre_close = soup_rank.find("tr", attrs = {"class" : "Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)"})
open_price = pre_close.find_next_sibling("tr")
volume = open_price.find_next_sibling("tr")


    


def rank1(pre_close,volume,rank1_name):
    print()
    print("--- <<<  {}  >>>---" .format(rank1_name))
    print("URL : " ,rank1_url)
    for i in pre_close:
        pre_close = print(i.get_text(), end = " ")
    print()
    for i in open_price:
        pre_close = print(i.get_text(), end = " ")
    print()
    for i in volume:
        print(i.get_text(), end = " ")    
    print()
    
    
def world():
    print("<<<  World Indices Top 10  >>>") 
    for idx,i in enumerate(names):
        name = i.get_text()
        print("Rank {} :".format(idx+1),name)
        if idx ==0 :
            rank1_name = name
        if idx == 9:
            break
    return rank1_name
    print()


rank1_name = world()
rank1(pre_close,volume,rank1_name)


slack.chat.post_message('#chat', 'About today Rank1 : ' + rank1_name + ": " +rank1_url )
