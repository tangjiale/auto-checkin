#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-15 22:25
# @Author  : jiale
# @Site    : 用于管理圈app 自动签到获得学分
# @File    : csdn_checkin.py
# @Software: PyCharm
import json

import requests


class QuanziCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "5.0.0 (iPhone; iOS 14.3; zh_CN)",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        # 用户当前登录token
        self.token = ""
        # wx 用户id
        self.uid = "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"
        # 当前应用消息title
        self.title = "管理圈"

    # 登录
    # @param data 登录请求信息
    def login(self, data):
        login_url = "http://www.pmquanzi.com/api/user/login"

        response = requests.post(url=login_url, data=data, headers=self.header)
        # 获取requests请求返回的token
        resp_data = json.loads(response.text)
        if resp_data["status"] == 1:
            self.token = resp_data["data"]["token"]
            print("登录成功")
            print(self.token)
        else:
            print("登录失败")
            error_msg = "%s: 登录失败，%s" % (self.title, resp_data["msg"])
            self.push_message(self.uid, error_msg)

    # 签到
    # @param uid 微信用户id
    def checkin(self, uid, req_data):
        checkin_url = "http://www.pmquanzi.com/api/user/qiandao_new"
        response = requests.post(url=checkin_url, data=req_data, headers=self.header)
        resp_json = json.loads(response.text)
        print(resp_json)
        if resp_json["status"] == 1:
            # 返回的data数据
            resp_data = resp_json["data"]
            # 响应成功
            msg = "%s : %s,当月签到次数：%d,当前学分：%d" % (
                self.title, resp_json["msg"], resp_data["sign_count_month"], resp_data["score"])
            self.push_message(uid, msg)
        else:
            self.push_message(uid, "%s : %s" % (self.title, resp_json["msg"]))

    # 获取签到列表
    def get_checkin_list(self, req_data):
        checkin_list_url = "http://www.pmquanzi.com/api/user/get_qiandao"
        response = requests.post(url=checkin_list_url, data=req_data, headers=self.header)
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
req_user_data = {
    'token': '0',
    'mobile': '15208427173',
    'password': 'Pm_911026'
}
qz = QuanziCheckin()
qz.login(req_user_data)
req_data = {
    "token": qz.token
}
# qz.get_checkin_list(req_data)
qz.checkin(qz.uid, req_data)
# qz.push_message("UID_qNCI9uES2zahjmm8W3iGZAEB07sv", "签到成功")
