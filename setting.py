# -*- coding:utf-8 -*-

#Redis数据库地址
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

#代理分数
MAX_SCORE = 5
MIN_SCORE = 0
INITIAL_SCORE = 5

VALID_STATUS_CODES = [200,302]

#代理池数量界限
POOL_UPPER_THRESHOLD = 50000

#检查周期
TESTER_CYCLE = 20
#获取周期
GETTER_CYCLE = 20

#测试API
TEST_URL = 'http://www.baidu.com'

#API配置
API_HOST = '172.17.150.130'
API_PORT = 5000

#开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

#最大批次测试量
BATCH_TEST_SIZE = 10

XUN_DAI_LI_API="http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=956cf183afa242e9a73bcf6c9e8af3f0&orderno=YZ20187121252QWFUXQ&returnType=2&count=5"