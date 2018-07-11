# -*- coding:utf-8 -*-
from flask import Flask,g
from db import RedisClient

__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,'redis'):
        g.redis = RedisClient()
    return g.redis

@app.route('/')
def index():
    return '<h2>欢迎访问代理池</h2>'

@app.route('/random')
def get_proxy():
    conn = get_conn()
    return conn.random()

@app.route('/count')
def get_counts():
    conn = get_conn()
    return str(conn.count())


if __name__ == '__main__':
    app.run(host="172.17.150.130",port=5000,debug=True)