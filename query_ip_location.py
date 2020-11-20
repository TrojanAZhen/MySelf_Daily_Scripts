#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import time
import requests
from lxml import etree

URL = "https://haoip.cn/ip/"

URL_Headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7,zh-TW;q=0.6,und;q=0.5,uk;q=0.4,ja;q=0.3',
    'Dnt': '1',
    'referer': 'https://haoip.cn/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}

URL_Headers['Cookie'] = 'Hm_lvt_1444d3f7de1c854cf84ea3f4691a14ff=1605848989; _pk_ref.2.b770=%5B%22%22%2C%22%22%2C1605848989%2C%22https%3A%2F%2Fwww.v2ex.com%2Ft%2F437812%22%5D; _pk_ses.2.b770=1; _pk_id.2.b770=de98df715009c6cf.1605848989.1.1605850173.1605848989.; Hm_lpvt_1444d3f7de1c854cf84ea3f4691a14ff=1605850173; XSRF-TOKEN=eyJpdiI6IlhiRk5JZWJKVGVidkpaS1FXMFMxVEE9PSIsInZhbHVlIjoiZUxGSWhPZWtTQnVwTkgyeHFWazQ3bDlsSXZBWFphSDNseno4bGdZQlVEZ1wvTktWYlFCN2UwNEdreHozU3VzeVVDNERTcnByT01WNFJDRWk5K2VhRUF3PT0iLCJtYWMiOiI0NmJlNjAzYTY5YzIyNjg2OTk3ZDBhM2M4NDcwNDRjODllMDkyMGEwYzYwMmIyMTdmMTUxMGVmYTU4YWEzMjBkIn0%3D; laravel_session=eyJpdiI6Ikw1U0ZwOGdWVlgwRmNVOHRTRmU3cnc9PSIsInZhbHVlIjoiOUlYelRvV3Vmb2VPd1grZjE4NDZxTzBCb1FNWTVUUjRSNkdcL3hVcHhPUW0rSWZsK0ZqWmdCZFRtUk1nRmVIVmJsR2lnNWJBcUwySVFobUZac0NLUDB3PT0iLCJtYWMiOiI4ZDdjYzM0MjMxNDc2Yzg0ZjZjZjk3NjAyYjdlYmNiNDAzNWZjNDVlZjk3ODA4Zjc0N2NhZDY0YjVjYjcwZjVlIn0%3D'

def req_ip(ip):
    tmp_url = URL + ip
    req = requests.get(tmp_url, headers=URL_Headers, timeout=1)
    
    source_html = req.text
    
    selector = etree.HTML(source_html)
    # xpath规则只查纯真数据
    iplocation_xpath = selector.xpath('//*[@id="chunzhen"]/span')
    print(ip, "：", iplocation_xpath[0].text, '\n')

file_location = os.getcwd() + '/' + 'ip.txt'
with open(file_location) as f:
    ip_list = f.readlines()
    for ip in ip_list:
        req_ip(ip.strip("\n"))
        time.sleep(1)

