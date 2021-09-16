#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 用户人人都是产品经理自动签到获取成长值
# @File    : woshipm_checkin.py
# @Software: PyCharm
import json
import requests


class WoShiPmCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "woshiPM/4.4.8 (iPhone; iOS 14.3; Scale/2.00)",
            "Content-Type": "text/html;charset=utf-8",
            "device_info": "{\"browser_version\":\"\",\"os_type\":\"iOS\",\"device_id\":\"af217904fd564a1cbf1dc3d16db71ffc93661\",\"browser_type\":\"\",\"os_version\":\"14.3\",\"client_type\":\"App\",\"network_type\":\"WiFi\",\"device_model\":\"iPhone10,1\",\"device_brand\":\"Apple\"}"
        }
        # 用户token
        self.access_token = "",
        # 用户密钥
        self.access_token_secret = ""
        # 微信用户id
        self.uid = "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"

    # 签到
    # @param uid 微信用户id
    def checkin(self, uid):
        checkin_url = "http://api.woshipm.com/user/signUp.html?sequence=1&COMMON_ACCESS_TOKEN=%s&COMMON_ACCESS_TOKEN_SECRET=%s&_cT=IOS&_cV=4.4.8&_cA=PM" % (
        self.access_token, self.access_token_secret)
        response = requests.post(url=checkin_url, headers=self.header)
        resp_data = json.loads(response.text)
        self.header["event_location"] = "PMCheckInViewController"
        self.header["event_location_pre"] = "user_home@signin"
        print(resp_data)
        msg = "人人都是产品经理：签到成功"
        if resp_data["CODE"] == 200:
            # 推送微信消息
            self.push_message(uid, msg)
        else:
            self.push_message(uid, resp_data["MESSAGE"])

    # 登录
    # @param user_data 用户登录请求对象
    def login(self, user_data):
        login_url = "https://passport.woshipm.com/api/loginByAPI.html?_cT=IOS&_cV=4.4.8&_cA=PM"
        login_header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "woshiPM/4.4.8 (iPhone; iOS 14.3; Scale/2.00)",
            "event_location": "LoginViewController",
            "event_location_pre": "woshiPM.PMQuickSignInViewController"
        }
        response = requests.post(url=login_url, data=user_data, headers=login_header)
        print(response.text)
        resp_data = json.loads(response.text)
        if resp_data["CODE"] == 200:
            self.access_token = resp_data["RESULT"]["PM-Cookie"]["COMMON_ACCESS_TOKEN"]
            self.access_token_secret = resp_data["RESULT"]["PM-Cookie"]["COMMON_ACCESS_TOKEN_SECRET"]
        else:
            print("登录失败：" + resp_data["MESSAGE"])

    # 获取用户信息
    def get_user_info(self):
        info_url = "https://wen.woshipm.com/api/user1/V4/myIndex.html?COMMON_ACCESS_TOKEN=%s&COMMON_ACCESS_TOKEN_SECRET=%s&_cT=IOS&_cV=4.4.8&_cA=PM" % (
        self.access_token, self.access_token_secret)
        response = requests.get(url=info_url, headers=self.header)
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


# 用户登录请求参数
req_user_data = {
    "FROMSYS": "WD",
    "account": "15208427173",
    "pwd": "UG1fOTExMDI2"
}

# 请求数据
note = WoShiPmCheckin()
note.login(req_user_data)
# note.get_user_info()
note.checkin(note.uid)
