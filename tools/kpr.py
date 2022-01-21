#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time :2022/1/6 13:44
# @Author :wangqinghua
# @File : kpr.py
# @Software : PyCharm


import time


res_time=int(time.time() * 10)

class Test_Add:

    def order(self):
        orders="KPRGR"
        a=str(res_time)
        s=str(a[4:])
        orders=orders+s
        return orders

    def cif(self):
        cifs=str(res_time)
        s=str(cifs[5:])
        return s

    def devid(self):
        devids="090e687562000"
        a=str(res_time)
        s=str(a[4:])
        orders=devids+s
        return orders

    def ip(self):
        ipaddress="168.161.0."
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
        res="sinarmas"
        com="@163.com"
        a = str(res_time)
        emails=res+a+com
        return emails

    def fullname(self):
        name="JRT HWY"
        a=str(res_time)
        lat = str(a[6:])
        res=name+lat
        return res

    def phone(self):
        a=str(res_time)
        res = str(a[1:14])
        return res

    def ktp(self):
        a = str(res_time)
        lat = str(a[6:])
        kptnumber="69057122041"
        res=kptnumber+lat
        return res

if __name__ == '__main__':
    print(Test_Add().email())








