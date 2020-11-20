#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import json, urllib
import urllib.request
from urllib.parse import urlencode
 
 
#根据城市查询天气
def query_weather(city_name):
    appkey = "90cda1bfb70a0a075d01ad66d47a8d00"
    #appkey = SECRETS['juliweather']['APPKEY']

    url = "http://op.juhe.cn/onebox/weather/query"
    params = {
        "cityname" : city_name,
        "key" : appkey,
        "dtype" : "", #返回数据的格式,xml或json，默认json
 
    }
    params = urlencode(params)
    f = urllib.request.urlopen("%s?%s" % (url, params))
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            weather_result = res['result']
            city_weather = "查询地区：{}{}" \
                           "最后更新时间：{}{}" \
                           "温度：{}{}" \
                           "天气状况：{}{}" \
                           "湿度：{}{}" \
                           "阴历：{}{}" \
                           "风向/力：{}/{}".format(weather_result['data']['realtime']['city_name'], "\n", 
                                                weather_result['data']['realtime']['time'][:-3], "\n",
                                                weather_result['data']['realtime']['weather']['temperature'], "\n",
                                                weather_result['data']['realtime']['weather']['info'], "\n",
                                                weather_result['data']['realtime']['weather']['humidity'], "\n",
                                                weather_result['data']['realtime']['moon'], "\n",
                                                weather_result['data']['realtime']['wind']['direct'], weather_result['data']['realtime']['wind']['power'])
            print(city_weather)
        else:
            print("{}:{}".format(res["error_code"], res["reason"]))
    else:
        print("request api error!!!")
 
 
 
if __name__ == '__main__':
    query_weather("广州")
