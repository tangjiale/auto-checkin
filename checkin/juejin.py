#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-12-10 17:12
# @Author  : jiale
# @Site    : 掘金签到获取矿石并抽奖
# @File    : juejin.py
# @Software: PyCharm
import json

import requests

from common import constants
from common.push_message import push_message
from common.title_type import TitleType


class JueJinCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Content-Type": "text/json; charset=utf-8"
        }
        cookies_str = constants.juejin_cookie
        cookies_dict = {}
        for cookie in cookies_str.split('; '):
            cookies_dict[cookie.split('=')[0]] = cookie.split('=')[-1]
        self.cookies = cookies_dict

    # 签到
    def checkin(self):
        checkin_url = "https://api.juejin.cn/growth_api/v1/check_in"
        response = requests.post(url=checkin_url, cookies=self.cookies)
        resp_data = json.loads(response.text)
        print("%s签到响应：%s" % (TitleType.JueJin.value[0], resp_data))
        if 0 == resp_data["err_no"]:
            if resp_data["err_msg"] == 'success':
                success_msg = "签到成功，增加矿石: %dM" % (resp_data["data"]["incr_point"])
                # 推送消息
                push_message(TitleType.JueJin.value[0], success_msg)
            else:
                push_message(TitleType.JueJin.value[0], "签到失败: %s" % resp_data["err_msg"])
        else:
            push_message(TitleType.JueJin.value[0], "签到失败,%s" % resp_data["err_msg"])

    # 获取总矿石
    def get_cur_point(self):
        info_url = "https://api.juejin.cn/growth_api/v1/get_cur_point"
        response = requests.get(url=info_url, cookies=self.cookies)
        # 响应：{"err_no":0,"err_msg":"success","data":766}
        resp_data = json.loads(response.text)
        print("%s获取总矿石响应：%s" % (TitleType.JueJin.value[0], resp_data))

    # 获取抽奖信息
    def get_draw_info(self):
        info_url = "https://api.juejin.cn/growth_api/v1/lottery_config/get"
        response = requests.get(url=info_url, cookies=self.cookies)
        # 响应：{"err_no":0,"err_msg":"success","data":true}
        resp_data = json.loads(response.text)
        print("%s查询抽奖信息响应：%s" % (TitleType.JueJin.value[0], resp_data))
        return resp_data

    # 抽奖
    def draw(self):
        draw_info = self.get_draw_info()
        if draw_info["err_no"] == 0:
            if draw_info["data"]["free_count"] > 0:
                draw_url = "https://api.juejin.cn/growth_api/v1/lottery/draw"
                response = requests.post(url=draw_url, cookies=self.cookies)
                resp_data = json.loads(response.text)
                print("%s抽奖响应：%s" % (TitleType.JueJin.value[0], resp_data))
                if resp_data["err_no"] == 0:
                    if "Bug" != resp_data["data"]["lottery_name"]:
                        push_message(TitleType.JueJin.value[0], "中奖了: %s" % resp_data["data"]["lottery_name"])
                else:
                    push_message(TitleType.JueJin.value[0], "抽奖失败: %s" % resp_data["err_msg"])
        else:
            push_message(TitleType.JueJin.value[0], "获取抽奖信息失败: %s" % draw_info["err_msg"])

    # 获取用户信息
    def get_user_info(self):
        info_url = "https://api.juejin.cn/user_api/v1/user/get"
        response = requests.get(url=info_url, cookies=self.cookies)
        print(response.text)
