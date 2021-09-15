#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-08-17 10:15
# @Author  : jiale
# @Site    : 用于stt_cloud 自动签到
# @File    : stt_auto_checkin.py
# @Software: PyCharm
import requests
from requests import utils


class SttAutoCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01"
        }
        self.cookies = {}

    # 登录
    # @param data 登录请求信息
    def login(self, data):
        login_url = "https://sttlink.com/auth/login"

        response = requests.post(url=login_url, data=data, headers=self.header)
        print(response.text.encode().decode("unicode_escape"))
        # 获取requests请求返回的cookie
        self.cookies = requests.utils.dict_from_cookiejar(response.cookies)
        # print(self.cookies)

    # 签到
    # @param uid 微信用户id
    def checkin(self, uid):
        checkin_url = "https://sttlink.com/user/checkin"
        response = requests.post(url=checkin_url, headers=self.header, cookies=self.cookies)
        resp_data = eval(response.text.encode().decode("unicode_escape"))
        print(resp_data)
        self.push_message(uid, resp_data["msg"])

    # 获取用户信息
    def user(self):
        user_info_url = "https://sttlink.com/user"
        response = requests.get(url=user_info_url, headers=self.header, cookies=self.cookies)
        print(response.text)

    # 推送信息到微信
    # @param uid wxPusher的用户id
    # @param message 推送消息
    def push_message(self, uid, message):
        push_url = "http://wxpusher.zjiecode.com/api/send/message"
        req_json = {
            "appToken": "AT_cWSuidnpkwufJ5JgF1PverQoF0cQr3No",
            "content": message,
            "contentType": 1,
            "uids": [uid]
        }
        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(url=push_url, json=req_json, headers=header)
        print(response.text)


# 请求数据
req_data_list = [
    {
        'email': '243185722@qq.com',
        'passwd': 'yw121175',
        "uid": "UID_0Rh0jmzXf7Oi9GbfzXQijAUKALSh"
    }, {
        'email': 'jialesmile@foxmail.com',
        'passwd': 'stt_911026',
        "uid": "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"
    }
]
stt = SttAutoCheckin()
for req_data in req_data_list:
    data = {
        "email": req_data["email"],
        "passwd": req_data["passwd"]
    }
    stt.login(data)
    stt.checkin(req_data["uid"])
    # stt.user()

# stt.push_message("UID_qNCI9uES2zahjmm8W3iGZAEB07sv", "您似乎已经签到过了...")
