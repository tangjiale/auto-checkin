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
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        cookies_str = constants.huke_cookie
        cookies_dict = {}
        for cookie in cookies_str.split('; '):
            cookies_dict[cookie.split('=')[0]] = cookie.split('=')[-1]
        self.cookies = cookies_dict

    # 签到
    def checkin(self):
        checkin_url = "https://huke88.com/header/sign-today"
        response = requests.post(url=checkin_url, cookies=self.cookies)
        resp_data = json.loads(response.text)
        print("%s签到响应：%s" % (TitleType.HuKe.value[0], resp_data))
        if 0 == resp_data["error"]:
            return "签到成功，增加虎课币"
            # return "签到成功，增加虎课币: %d" % (resp_data)
        else:
            return "签到失败,%s" % resp_data["err_msg"]

# hk = HuKeCheckin()
# hk_resp_checkin = hk.checkin()
# print(hk_resp_checkin)