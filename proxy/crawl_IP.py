import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import bs4
class crawl:
	def page_kuai(page,r):
	    ua = UserAgent()
	    headers={'User-Agent':ua.random}
	    html=requests.get('https://www.kuaidaili.com/free/inha/'+str(page),headers=headers)#删除作者参数  ,verify=False
	    if html.status_code == 200:
	        Soup=BeautifulSoup(html.text,'lxml')
	        tbody=Soup.find('tbody')
	        if isinstance(tbody,bs4.element.Tag):
		        tr_list=tbody.find_all('tr')
		        for tr in tr_list:
		            try:
		                IP_adress=tr.find('td').get_text()
		                IP_port=tr.find('td',attrs={'data-title':"PORT"}).get_text()
		                IP="http://"+IP_adress+":"+IP_port
		                proxies={'http':IP}
		                #print(proxies)
		                try:
		                    response = requests.get('http://www.baidu.com', proxies=proxies,timeout=6)#########
		                    r.lpush('IP',IP)
		                    print("可yong+1"+IP)
		                except :
		                    print("false")
		            except Exception:
		                pass
	    else:
	        print('********************被墙*************************')

