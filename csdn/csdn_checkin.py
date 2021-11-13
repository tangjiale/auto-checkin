#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-15 22:25
# @Author  : jiale
# @Site    : 用于管理圈app 自动签到获得学分
# @File    : csdn_checkin.py
# @Software: PyCharm
import json

import requests
from requests import utils
from common.title_type import TitleType


class CsdnCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "CSDNApp/4.15.1(iPhone 8 / iOS 14.3) wToken/0.0.1",
            "Content-Type": "application/json;charset=utf-8",
            "DeviceToken": "TkVXSUQjNTIwMTE3Yjk3MWI0NTcxNjAyMDgwNTI0Mjc0ZWJmZjItaC0xNjMxOTMwMDI4OTg3LWJhMzNiOGM0ODViNDQyY2JiNDFlYjRjN2FjMTcwMjY3I3ZoeEY1ZVNxdEs2MzM2aTlSeXVvVXltVjNUeHZ6QVZqV1F1TU1XTzFtTGlqNjZKa2g1a1M2NHNHeVBBPQ==",
            "X-Accept-Language": "zh-cn",
            "X-Access-Token": "1b2042b64cd1d6a33a7582eccaf50cc2",
            "X-App-ID": "CSDN-APP",
            "X-App-Version": "4.15.1",
            "X-Ca-Key": "203792824",
            "X-Ca-Nonce": "57048a6d-d8c7-49da-b271-7dea09ddda10",
            "X-Ca-Random": "mli9LYoRvSs5Q92Xu+Gl1exYrKqQw5gOCUPMptBDnTQFxgQYQI9b9YdioN0Fl0XmMhFvNXwtg9PzVfeJyqtEaAIEEDAi82UogEH2lXHVvL4gDOqJJ6R4shrJjN6xTZUD4MZukStIFk2cMxvgYi+MPJLigtnNyCxg27KQd/acI7F88r/RoUQm3jLOmVa9QRUsqlXwQXC/6+HqePklNgImdawfZz9hrsMFNYrV3RVOS5s=",
            "X-Ca-Signature-Headers": "X-Ca-Timestamp,X-Ca-Key,X-Ca-Nonce",
            "X-Ca-Signature": "zlfuwhWF7oeU7WBie4M9gMmeGRDP7XjdJyK0mJZAIdE=",
            "X-Ca-Signed-Content-Type": "application/json",
            "X-Ca-Timestamp": "1631930110108",
            "X-Device-ID": "Ab7C3042-D96D-4D27-8713-11D3B15Ab470",
            "X-OS": "iOS",
            "X-RandomNum": "85593",
            "X-Sign": "C9888DEBE81B8FD1F14CF4D8AC6E71F7B589DB6F",
            "X-TimeStamp": "1631930110103",
            "X-Tingyun-Id": "wl4EtIR_7Is;c=2;r=1626295934;u=46986110086087f2d1461858814268ba4fc058f14ac51d210d71a7d4c3e0ebddeb7e942fb68afbd430b8fd3ebdc3bb83::93D179E1C5E0164D",
            "c_appVersion": "4.15.1",
            "isCsdnAudit": "0",
            "version": "4.15.1",
            "wToken": "e447_GC10uYGUt4b1MHOTjxEAXrRdQwToI/C7IhxKmQPTwEbvmNMEw6JAwUH337lkWtyA0w+JqVN+d1jyoEzT8dMQapwAkhv67MK5RbNt/rH+7ehNDuJ8tYYUKtYmwYEXcnjAyFoPtPe1tRz6wTJb1m+KDQD0DXU3Enyivd1VBPIFnny4cWZggmngEU1oy2bu5/VTiH90nc5X9aFxLDvOEq8lXGUXx9tA3oBfR6wcZqDaf5OAtTwQAx+mDtKjbSeXKzXEqqoOOsQQetQ8gnO/gpDRFs1eRySDpK/+TPWtBVB2sE6FKw+Pw6ouQLAvCYbPT/w27OYMmWZalvhEXh0SKwjEDcUvxBn55vUasQ8BWshuuyTA18MGipGxhWa6nXDfLctUFd+fmON1nOulrqSEvnGmcKbma7flW07UqSm4/Cl1+6ldDUJgWW3VqJYqmqaFShIpX0Qq3rGWQS5K/gY7ypC2iHNVh7x1r/wQvdl8AsR73uy1341EsKZ8RIp71WRAmXSL&ff4b_7BF69D509C918535C809454B5F4CB1080B190A214A3C180FE3"
        }
        # 用户当前登录token
        self.token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFkNGZmZWI4LTQwNTQtNGFkZC1iM2M4LTlhOWQzZjhlMjc0OSJ9.eyJzdWIiOiJ0MTM0NDAxMTY1OTEiLCJYLUFwcElEIjoiQ1NETi1BUFAiLCJYLURldmljZS1JRCI6IkFiN0MzMDQyLUQ5NkQtNEQyNy04NzEzLTExRDNCMTVBYjQ3MCIsIlgtUmlzay1Db250cm9sLU51bSI6IjAiLCJhdWQiOiJwYXNzcG9ydCIsImV4cCI6MTYzNDUyMzQxOCwiaWF0IjoxNjMxOTMxNDE4fQ.D8gLjNqRWyQ_92WK5-jLmgKpjbTRWrdqfzeCzLF01tr4CDhQmtGpKsonWLI_6Ruiiud_ISo-BkAYIGChpSR0x38B2EWnedNt5xHxpgCAEcguxg0ZYR4yZK5c8mtIMhVJducPZf_nl8DyfvnoI6AMvCXrJIy8-WSoDuXawMiOguUYinivFiJxkbh-Z2JYUvK4QGx1QGKGnn_TxFXW-BPliSIKPFd_60PvFv4k50FBt_AXFBa6WoztFFkW--N9FSnh60gKEYTJbw36OsSNFLlAGfdWNUcud8vLw4it9iN1ZTwTUKIxiG-VIGHiAhxw8VlCFbd5xEhRvrxxoPZQSyYLsg"
        # wx 用户id
        self.uid = "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"
        self.cookie = {}

    # 登录
    # @param data 登录请求信息
    def login(self, data):
        login_url = "https://passport.csdn.net/v1/api/app/login/doLogin"
        response = requests.post(url=login_url, json=data, headers=self.header)
        print(response.text)
        self.cookie = requests.utils.dict_from_cookiejar(response.cookies)
        print(self.cookie)
        # 获取requests请求返回的token
        resp_data = json.loads(response.text)
        print("登录信息: %s" % resp_data)
        if resp_data["code"] == "0":
            self.token = resp_data["data"]["token"]
            print("登录成功")
            print(self.token)
        else:
            print("登录失败")
            error_msg = "%s: 登录失败，%s" % (TitleType.CSDN.value[0], resp_data["message"])
            # self.push_message(self.uid, error_msg)

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
                TitleType.CSDN.value[0], resp_json["msg"], resp_data["sign_count_month"], resp_data["score"])
            self.push_message(uid, msg)
        else:
            self.push_message(uid, "%s : %s" % (TitleType.CSDN.value[0], resp_json["msg"]))

    # 获取签到列表
    def get_user_info(self):
        checkin_list_url = "https://app-gw.csdn.net/blog/phoenix/app/v1/homepage/user-info?username=t13440116591"
        self.header["Authorization"] = "Bearer" + self.token
        self.header["JWT-TOKEN"] = self.token
        response = requests.get(url=checkin_list_url,headers=self.header,cookies=self.cookie)
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
req_user_data = {"userIdentity": "", "userIdentification": "t13440116591", "qqUnionId": "", "identityToken": "",
                 "checkAli": "true", "loginType": "1", "code": "0086", "pwdOrVerifyCode": "tjl911026", "openId": "",
                 "openSite": "", "authorizationCode": "", "openName": ""}
qz = CsdnCheckin()
qz.login(req_user_data)
qz.get_user_info()
