# coding:utf-8
# 用于做接口，使其他的程序能够获得这个程序的开发出来的有用的IP
from flask import Flask
import redis

__all__ = ['app']

app = Flask(__name__)

@app.route('/')
def get_proxy():
    R =redis.Redis(host='localhost',port=6379,db=2,password="")
    ip=R.rpop('IP')
    R.lpush('IP',ip)
    return  ip
app.run() # 当你运行这段代码时，在浏览器中输入localhost:5000,就会出现ip
