#!/usr/bin/env python3
#================================================
#
#       Filename: bing_daily_pic.py
#       Author: spookw@foxmail.com
#       Create: 2018-06-05 03:52:10 PM
#
#================================================
import requests
import json
import time

def get_pic_url():
        """docstring for get_pic_url"""
        
        url = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
        r = requests.get(url)
        r_json = (r.json())
        list_r_json = (r_json['images'])
        dict_r_json = list_r_json[0]
        str_pic_url = dict_r_json['url']
        print(str_pic_url)
        prefix = "http://s.cn.bing.net"
        full_url = prefix+str_pic_url
        filename = dict_r_json['startdate']
        res = [full_url,filename]
        return res


url_addr = get_pic_url()[0]
file_name = get_pic_url()[1]+'pic.jpg'
daily_pic = requests.get(url_addr)
if daily_pic.status_code == 200:
    with open(file_name,'wb') as f:
        f.write(daily_pic.content)
