#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/1/19 18:08
# @Author :wangqinghua
# @File : cc.py
# @Software : PyCharm


import time


res_time=int(time.time() * 10)

class Test_CC:

    def order(self):
        orders="CCGR"
        a=str(res_time)
        s=str(a[4:])
        orders=orders+s
        return orders

    def cif(self):
        r=str(res_time)
        res=str(r[3:])
        return res

    def devid(self):
        r="090s680562000"
        a=str(res_time)
        s=str(a[4:])
        res=r+s
        return res

    def ip(self):
        ipaddress="169.182.0."
        a=str(res_time)
        s=str(a[8:])
        ips=ipaddress+s
        return ips

    def lat(self):
        a = str(res_time)
        lats = str(a[8:])
        return lats

    def lon(self):
        a = str(res_time)
        lons = str(a[8:10])+str(1)
        return lons

    def email(self):
        r="sinarmas"
        com="@163.com"
        a = str(res_time)
        s=a[3:10]
        res=r+s+com
        return res

    def fullname(self):
        name="ART HKY"
        a=str(res_time)
        lat = str(a[8:])
        res=name+lat
        return res

    def phone(self):
        a=str(res_time)
        res=int(str(a[1:10]))
        return res

    def ktp(self):
        a = str(res_time)
        s=str(a[6:])
        kptnumber="42010122000"
        res=kptnumber+s
        return res

if __name__ == '__main__':
    pass
    # print(Test_Add().order())
    print(Test_CC().phone())
    # print(Test_Add().cif())
    # print(Test_Add().email())
    # print(Test_Add().fullname())
    # print(Test_Add().ktp())
    # print(Test_Add().devid())
    # print(Test_Add().ip())
    # print(Test_Add().lat())
    # print(Test_Add().lon())

