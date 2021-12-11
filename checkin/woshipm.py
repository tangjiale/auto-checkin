#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 用户人人都是产品经理自动签到获取成长值
# @File    : woshipm.py
# @Software: PyCharm
import json

import requests

from common import constants
from common.push_message import push_message
from common.title_type import TitleType


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

    # 签到
    # @param uid 微信用户id
    def checkin(self):
        checkin_url = "http://api.woshipm.com/user/signUp.html?sequence=1&COMMON_ACCESS_TOKEN=%s&COMMON_ACCESS_TOKEN_SECRET=%s&_cT=IOS&_cV=4.4.8&_cA=PM" % (
            self.access_token, self.access_token_secret)
        response = requests.post(url=checkin_url, headers=self.header)
        resp_data = json.loads(response.text)
        self.header["event_location"] = "PMCheckInViewController"
        self.header["event_location_pre"] = "user_home@signin"
        print("%s签到响应：%s" % (TitleType.WSPM.value[0], resp_data))
        if resp_data["CODE"] == 200:
            # 推送微信消息
            push_message(TitleType.WSPM.value[0], "签到成功")
        else:
            error_msg = "签到失败，%s" % resp_data["MESSAGE"]
            push_message(TitleType.WSPM.value[0], error_msg)

    # 登录
    # @param user_data 用户登录请求对象
    def login(self):
        login_url = "https://passport.woshipm.com/api/loginByAPI.html?_cT=IOS&_cV=4.4.8&_cA=PM"
        login_header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "woshiPM/4.4.8 (iPhone; iOS 14.3; Scale/2.00)",
            "event_location": "LoginViewController",
            "event_location_pre": "woshiPM.PMQuickSignInViewController"
        }

        # 用户登录请求参数
        req_user_data = {
            "FROMSYS": "WD",
            "account": constants.wspm_username,
            "pwd": constants.wspm_password
        }
        response = requests.post(url=login_url, data=req_user_data, headers=login_header)
        print("%s登录响应：%s" % (TitleType.WSPM.value[0], response.text))
        resp_data = json.loads(response.text)
        if resp_data["CODE"] == 200:
            self.access_token = resp_data["RESULT"]["PM-Cookie"]["COMMON_ACCESS_TOKEN"]
            self.access_token_secret = resp_data["RESULT"]["PM-Cookie"]["COMMON_ACCESS_TOKEN_SECRET"]
        else:
            print("登录失败：" + resp_data["MESSAGE"])
            error_msg = "登录失败，%s" % resp_data["MESSAGE"]
            push_message(TitleType.WSPM.value[0], error_msg)

    # 获取用户信息
    def get_user_info(self):
        info_url = "https://wen.woshipm.com/api/user1/V4/myIndex.html?COMMON_ACCESS_TOKEN=%s&COMMON_ACCESS_TOKEN_SECRET=%s&_cT=IOS&_cV=4.4.8&_cA=PM" % (
            self.access_token, self.access_token_secret)
        response = requests.get(url=info_url, headers=self.header)
        print(response.text)


# 请求数据
# note = WoShiPmCheckin()
# note.login()
# # note.get_user_info()
# note.checkin()
