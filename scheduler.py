# -*- coding:utf-8 -*-
from multiprocessing import Process
from web_service import app
from getter import Getter
from tester import Tester
from setting import TESTER_CYCLE,GETTER_CYCLE,TESTER_ENABLED,GETTER_ENABLED,API_ENABLED,API_HOST,API_PORT
import time

class Scheduler():
    def scheduler_tester(self,cycle=TESTER_CYCLE):
        tester=Tester()
        while True:
            print("测试器开始运行")
            tester.run()
            time.sleep(cycle)

    def schedule_getter(self,cycle=GETTER_CYCLE):
        getter=Getter()
        while True:
            print("开始抓取代理")
            getter.run()
            time.sleep(cycle)
    def schedule_api(self):
        app.run(API_HOST,API_PORT,debug=True)

    def run(self):
        print("代理池开始运行")
        if TESTER_ENABLED:
            tester_process = Process(target=self.scheduler_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.schedule_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.schedule_api)
            api_process.start()