#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/1/19 14:49
# @Author :wangqinghua
# @File : test_http_requests.py
# @Software : PyCharm


from tools import tools_config
import unittest
import requests

#dev环境数据
KPR_DEV_URL=tools_config.dev_kpr_url
KPR_DEV_DATA=tools_config.dev_kpr_data
CC_DEV_URL=tools_config.dev_cc_url
CC_DEV_DATA=tools_config.dev_cc_data

#测试环境数据
KPR_TEST_URL=tools_config.test_kpr_url
KPR_TEST_DATA=tools_config.test_kpr_data
CC_TEST_URL=tools_config.test_cc_url
CC_TEST_DATA=tools_config.test_cc_data





#dev环境测试申请
class Dev_Login(unittest.TestCase):

     def test_apikpr(self):
       res=requests.post(KPR_DEV_URL,json=KPR_DEV_DATA)
       print("开发环境KPR申请的请求是{}".format(res.json()))
       return res.json()


     def test_apicc(self):
       res = requests.post(CC_DEV_URL, json=CC_DEV_DATA)
       print("开发环境CC申请的请求是{}".format(res.json()))
       return res.json()

#test环境测试申请
class Test_Login(unittest.TestCase):

     def test_apikpr(self):
       res=requests.post(KPR_TEST_URL,json=KPR_TEST_DATA)
       print("测试环境KPR申请的请求是{}".format(res.json()))
       return res.json()


     def test_apicc(self):
       res = requests.post(CC_TEST_URL, json=CC_TEST_DATA)
       print("测试环境CC申请的请求是{}".format(res.json()))
       return res.json()
if __name__ == '__main__':
    pass
    # res=requests.post(ccurl,json=ccdata)
    # print(res.json())