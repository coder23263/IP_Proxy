from crawl_IP import crawl
import redis
import time
from tester import test

if __name__ == '__main__':
	count_1=16
	count_2=17
	R =redis.Redis(host='localhost',port=6379,db=2,password="")
	while 1 :
		while R.llen('IP') < 15 :
			for i in range(count_1,count_2):
				crawl.page_kuai(i,R)
				time.sleep(2)
		count_1=count_2
		count_2+=1
		test.test_IP(R)

