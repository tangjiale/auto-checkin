#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-09 15:28
# @Author  : jiale
# @Site    : 36kr签到得积分
# @File    : 36kr.py
# @Software: PyCharm
import json

import requests


class KrCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "36kr-iOS/9.3.6 (iPhone8); Build 2; iOS 14.3; Scale/2.0;",
            "Content-Type": "application/json;charset=utf-8",
            "device": "CF2CED75-CA08-4CA7-A875-7B7FF2DA6A48",
            "sign": "4f65aedfd37e28084860bdd5ead4b3fc",
            "timestamp": 1633763954,
            "Cookie": "krtoken=Qk44XgKknDSiYIXpiUSbHF5v4FjJa2n_r4ZQLDr9AfcHDHiLWnNuuY7JSfL4wuO4PgqJPPWLV-D2wOMWBXXaAzWH69uhQ_FcGetL1SjYljU; kr_device_id=CF2CED75-CA08-4CA7-A875-7B7FF2DA6A48; kr_pinyou_device_uuid=CF2CED75-CA08-4CA7-A875-7B7FF2DA6A48; krnewsfrontcc=eyJ0eXAiOiJKV1QiLCJhbGciOiIzNmtyLWp3dCJ9.eyJpZCI6MjA1OTUyOTg3LCJzZXNzaW9uX2lkIjoiODZkMDY3NDBmZjJhZTE3ZjE5MGVmZTZiNGFiZTQwN2UiLCJleHBpcmVfdGltZSI6MTYzMzUwNjg2MSwidmVyc2lvbiI6InYxIn0=.53763e6e69f7c7dae6c656fae955172128386b111abaee9c6cc490fe514a2abd; krnewsfrontss=bfda1d4194f42b2ec29d79957d34bf52; acw_tc=2760826716337636029807485eb7d0085f61c863eca90422894ed44c3f2e82"
        }
        # 微信用户id
        self.uid = "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"
        # 当前应用消息title
        self.title = "36Kr"

    # 签到
    # @param uid 微信用户id
    def checkin(self, uid):
        checkin_url = "https://gateway.36kr.com/api/mis/user/signIn?sign=7c95f3f67d7b75e56982ceaa68d3d90b"
        response = requests.post(url=checkin_url, headers=self.header)
        resp_data = json.loads(response.text)
        self.header["event_location"] = "PMCheckInViewController"
        self.header["event_location_pre"] = "user_home@signin"
        print(resp_data)
        if resp_data["CODE"] == 200:
            success_msg = "%s：签到成功" % self.title
            # 推送微信消息
            self.push_message(uid, success_msg)
        else:
            error_msg = "%s: 签到失败，%s" % (self.title, resp_data["MESSAGE"])
            self.push_message(uid, error_msg)

    # 登录
    # @param user_data 用户登录请求对象
    def login(self, user_data):
        login_url = "https://gateway.36kr.com/api/mus/login/byMobilePassword?sign=dd366b81ab2f31a336001a52aed28e64"
        response = requests.post(url=login_url, json=user_data, headers=self.header)
        resp_data = json.loads(response.text)
        print("登录响应：%s" % resp_data)
        pass

    # 获取用户信息
    def get_user_info(self):
        pass

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
    "timestamp_period": "300",
    "device_density": "401",
    "user_agent_ad": "Mozilla\/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit\/605.1.15 (KHTML, like Gecko) Mobile\/15E148",
    "isp": "中国移动",
    "partner_id": "ios",
    "mac": "88:25:93:c5:e:b9",
    "network": "wifi",
    "device_id": "CF2CED75-CA08-4CA7-A875-7B7FF2DA6A48",
    "device_width": "1170.0",
    "idfa": "00000000-0000-0000-0000-000000000000",
    "os_version": "15.4",
    "device_orientation": "0",
    "param": {
        "countryCode": "86",
        "password": "RPd6kst2ebdB\/KOHCvuNY+6XQXNCTNxLpFW47ayhwdoJzKfpKugnmzkvEUN152R5xP3CUfmNOiGc8FF8KBfC6MJbnwyLyiXGCxLkzM0dyeRAzKb3bzC6H5DP+pfDyL0xXaRrgyp5VFp\/Sq7xDBYY1BkS+W+obThxJbGhfz6tpEA=",
        "siteId": "1",
        "platformId": "1",
        "mobileNo": "NoBMJ4VoxmIQRyFWTvFe+LbZHlx\/UgxvjuOKh2GIy0x3wVjKunh3FijZ3KAx357S4dWnGixVrY0xrVrl9YyOz+waUhMznwBmd4gMZjnENDspizMrIdpK9Y1G0JPOEeE1MnNbpXZNFU0Cu33qEzZT7nwZs1K\/TQdeoh\/p5Wa1oO8="
    },
    "partner_version": "9.5.1",
    "ip": "118.122.120.118",
    "device_model": "iPhone 13",
    "device_height": "2532.0",
    "device_brand": "Apple",
    "app": "36kr",
    "timestamp": "1652748526"
}

# 请求数据
kr = KrCheckin()
# kr.get_user_info()
# kr.checkin(kr.uid)
kr.login(req_user_data)