#用来测试代理池里面代理IP是否可用
import redis
import requests
import time
class test:
	def test_IP(r):# 从列表的尾部取出一个ip
		while r.llen('IP') >12 :
			try:
				ip=str(r.rpop('IP'),encoding='utf-8')# redis导出的数据都是bytes类型的，所以我们必须将其str化，必须加enconding参数
				proxies = {'http': ip}# 测试ip有没有用
				try:
					html=requests.get("http://www.baidu.com",proxies=proxies,timeout=6)
					if html.status_code == 200:
						r.lpush('IP',ip)
						print('valid IP')
				except :
					print('丢弃无用的ip')
				time.sleep(3)
			except :
				print("IP池枯竭")
			#time.sleep(20)
