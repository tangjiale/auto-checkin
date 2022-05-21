#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022-05-16 22:12
# @Author  : jiale
# @Site    : 虎课网签到获取虎课币
# @File    : huke.py
# @Software: PyCharm
import json

import requests

from common import constants
from common.title_type import TitleType


class HuKeCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "Referer": "https://huke88.com/quests/",
            "origin": "https://huke88.com",
            "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="101","Google Chrome";v="101"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-requested-with": "XMLHttpRequest",
            "accept": "/",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh,zh-CN;q=0.9",
            "content-length": "87",
            "cookie": constants.huke_cookie

        }

    # 签到
    def checkin(self):
        checkin_url = "https://huke88.com/header/sign-today"
        req = {
            "uid": "1849082",
            "_csrf-frontend": "cEFrSVNMX1VEKSMZIAImABMnKjoxImpnJCwsfCo0agUGMFs8MCkbGw=="
        }
        response = requests.post(url=checkin_url, data=req, headers=self.header)
        if response.status_code == 200:
            resp_data = json.loads(response.text)
            # {"error":"0","message":"当天签到成功","gold":10}
            print("%s签到响应：%s" % (TitleType.HuKe.value[0], resp_data))
            if 0 == resp_data["error"]:
                return "签到成功，增加虎课币: %d" % (resp_data["gold"])
            else:
                return "签到失败,%s" % resp_data["message"]
        else:
            return "签到请求失败"

# hk = HuKeCheckin()
# hk_resp_checkin = hk.checkin()
# print(hk_resp_checkin)
