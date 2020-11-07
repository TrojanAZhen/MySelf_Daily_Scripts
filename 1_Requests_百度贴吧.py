#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
import random


def load_page(url, kw, pn, filename):
    headers_list = [
            "Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
            "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)",
            "Mozilla/5.0 (iPhone; U; CPU like Mac OS X) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/4A93 Safari/419.3",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; TencentTraveler 4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) )"
            ]
    headers = random.choice(headers_list)
    print headers

    response = requests.get(url, params = {"kw" : kw, "pn" : pn}, headers=headers)
    return response.content

def write_page(html, filename):
    with open(filename, "w") as f:
        f.write(html)

def start_work(url, kw, start_page, end_page):
    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        filename = "No." + str(page) + "页.html"
        html = load_page(url, kw, pn, filename)
        write_page(html, filename)
    print "[LOG]：下载完成！"


if __name__ == "__main__":
    key_word = raw_input("请输入需要爬取的贴吧名：")
    start_page = int(raw_input("请输入要爬取的起始页："))
    end_page = int(raw_input("请输入要爬取的结束页："))
    url = "http://tieba.baidu.com/f?"
    start_work(url, key_word, start_page, end_page)

