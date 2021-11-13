#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-15 22:25
# @Author  : jiale
# @Site    : 用于管理圈app 自动签到获得学分
# @File    : csdn_checkin.py
# @Software: PyCharm
import json

import requests

from common import constants
from common.push_message import push_message
from common.title_type import TitleType


class QuanziCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "5.0.0 (iPhone; iOS 14.3; zh_CN)",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        # 用户token请求对象
        self.req_data = {
            "token": ""
        }

    # 登录
    # @param data 登录请求信息
    def login(self):
        login_url = "http://www.pmquanzi.com/api/user/login"
        # 请求数据
        data = {
            'token': '0',
            'mobile': constants.pmqz_username,
            'password': constants.pmqz_password
        }
        response = requests.post(url=login_url, data=data, headers=self.header)
        # 获取requests请求返回的token
        resp_data = json.loads(response.text)
        if resp_data["status"] == 1:
            self.req_data["token"] = resp_data["data"]["token"]
            print("登录成功")
            print(self.req_data)
        else:
            print("登录失败")
            error_msg = "登录失败，%s" % resp_data["msg"]
            push_message(TitleType.PMQZ, error_msg)

    # 签到
    def checkin(self):
        checkin_url = "http://www.pmquanzi.com/api/user/qiandao_new"
        response = requests.post(url=checkin_url, data=self.req_data, headers=self.header)
        resp_json = json.loads(response.text)
        print(resp_json)
        if resp_json["status"] == 1:
            # 返回的data数据
            resp_data = resp_json["data"]
            # 响应成功
            msg = "%s,当月签到次数：%d,当前学分：%d" % (
                resp_json["msg"], resp_data["sign_count_month"], resp_data["score"])
            push_message(TitleType.PMQZ, msg)
        else:
            push_message(TitleType.PMQZ, "%s" % resp_json["msg"])

    # 获取签到列表
    def get_checkin_list(self):
        checkin_list_url = "http://www.pmquanzi.com/api/user/get_qiandao"
        response = requests.post(url=checkin_list_url, data=self.req_data, headers=self.header)
        print(response.text)


qz = QuanziCheckin()
qz.login()
# qz.get_checkin_list(req_data)
qz.checkin()
