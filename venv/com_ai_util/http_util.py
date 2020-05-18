# -*- encoding= utf-8 -*-

"""
@Author lixuejun
@Time 2020/5/18
"""

import json
import requests

class HttpUtil:

    def __init__(self):
        pass

    def post(self, url, headers):
        param = input("请输入{pageNo：1}: ")
        http_util = HttpUtil()
        new_body = json.dumps(http_util.data_init(param))
        print("最新传入的body%s" % new_body)
        print("传入的headers %s" % headers)
        response = requests.post(url, headers=headers, data=new_body)
        response.content.decode("unicode-escape")
        re = eval(response.content)
        print("返回的response.content是%s" % response.content)
        print("期望得到的响应字段值为: %s" % re["resultCode"])

    def data_init(self, appendData):
        data = {
            "applyCode": "",
            "projectName": "",
            "applyType": "",
            "status": "",
            "isBigSign": "",
            "saleSbuId": "",
            "projectSbuId": "",
            "salePersonId": "",
            "sourceType": "",
            "pageSize": 10,
        }
        if appendData is not None:
            data.update(appendData)
            print("向request_body字典数据中追加了%s" % data)
        return data


url = ""

headers = {
    "authorization": "bearer amu1nOyIiK4lxG9hHCRXPCcUTpmUjxys",
    "Content-Type": "application/json"
}

doPost = HttpUtil()
doPost.post(url, headers)
