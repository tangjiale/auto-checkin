#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-08-17 10:15
# @Author  : jiale
# @Site    : 用于stt_cloud 自动签到获得流量
# @File    : stt_checkin.py
# @Software: PyCharm
import requests
from requests import utils

from common import constants
from common.push_message import push_message
from common.title_type import TitleType


class SttCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01"
        }
        self.cookies = {}

    # 登录
    # @param data 登录请求信息
    def login(self):
        login_url = "%s/auth/login" % constants.stt_main
        data = {
            'email': constants.stt_username,
            'passwd': constants.stt_password,
        }
        response = requests.post(url=login_url, data=data, headers=self.header)
        print(response.text.encode().decode("unicode_escape"))
        # 获取requests请求返回的cookie
        self.cookies = requests.utils.dict_from_cookiejar(response.cookies)
        # print(self.cookies)

    # 签到
    # @param uid 微信用户id
    def checkin(self):
        checkin_url = "%s/user/checkin" % constants.stt_main
        response = requests.post(url=checkin_url, headers=self.header, cookies=self.cookies)
        resp_data = eval(response.text.encode().decode("unicode_escape"))
        print(resp_data)
        push_message(TitleType.STT, resp_data["msg"])

    # 获取用户信息
    def user(self):
        user_info_url = "%s/user" % constants.stt_main
        response = requests.get(url=user_info_url, headers=self.header, cookies=self.cookies)
        print(response.text)


stt = SttCheckin()
stt.login()
stt.checkin()
# stt.user()
