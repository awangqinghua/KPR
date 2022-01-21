#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/1/19 17:32
# @Author :wangqinghua
# @File : run.py
# @Software : PyCharm


from tools.test_http_requests import Dev_Login
#from tools.test_http_requests import Test_Login   #测试环境申请数据
import unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Dev_Login))
#suite.addTest(loader.loadTestsFromTestCase(Test_Login))

with open("test.report.html","wb") as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,
                                            title="KPR/CC申请接口自测",
                                            description="单元测试",
                                            tester="KPR AND CC")
    runner.run(suite)

