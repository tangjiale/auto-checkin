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
                return "签到成功，增加矿石: %dM" % (resp_data["data"]["incr_point"])
            else:
                return "签到失败: %s" % resp_data["err_msg"]
        else:
            return "签到失败,%s" % resp_data["err_msg"]

    # 获取总矿石
    def get_cur_point(self):
        info_url = "https://api.juejin.cn/growth_api/v1/get_cur_point"
        response = requests.get(url=info_url, cookies=self.cookies)
        # 响应：{"err_no":0,"err_msg":"success","data":766}
        resp_data = json.loads(response.text)
        print("%s获取总矿石响应：%s" % (TitleType.JueJin.value[0], resp_data))

    # 沾福气
    def dip_luck(self):
        # 获取用户唯一id
        # user_param = unquote(self.cookies["__tea_cookie_tokens_2608"], encoding='utf-8', errors='replace')
        # uuid = user_param["web_id"]
        info_url = "https://api.juejin.cn/growth_api/v1/lottery_lucky/dip_lucky?aid=2608&uuid=7040367811554510371"
        response = requests.post(url=info_url, cookies=self.cookies)
        # 响应：{"err_no":0,"err_msg":"success","data":{"dip_action":1,"has_dip":false,"total_value":1679,"dip_value":10}}
        resp_data = json.loads(response.text)
        print("%s沾福气信息响应：%s" % (TitleType.JueJin.value[0], resp_data))
        if 0 == resp_data["err_no"]:
            if resp_data["err_msg"] == 'success':
                return "沾福气成功，获得幸运点数: %d" % (resp_data["data"]["dip_value"])
            else:
                return "沾福气失败: %s" % resp_data["err_msg"]
        else:
            return "沾福气失败,%s" % resp_data["err_msg"]

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
                # 响应 ： {'err_no': 0, 'err_msg': 'success', 'data': {'id': 19, 'lottery_id': '6981716980386496552',
                # 'lottery_name': '11矿石', 'lottery_type': 1, 'lottery_image':
                # 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32ed6a7619934144882d841761b63d3c~tplv-k3u1fbpfcp
                # -no-mark:0:0:0:0.image', 'lottery_desc': '', 'history_id': '7087024855945576482',
                # 'total_lucky_value': 1699, 'draw_lucky_value': 10}}
                resp_data = json.loads(response.text)
                print("%s抽奖响应：%s" % (TitleType.JueJin.value[0], resp_data))
                if resp_data["err_no"] == 0:
                    if "Bug" != resp_data["data"]["lottery_name"]:
                        return "中奖了: %s" % resp_data["data"]["lottery_name"]
                else:
                    return "抽奖失败: %s" % resp_data["err_msg"]
            else:
                return "今日已抽奖"
        else:
            return "获取抽奖信息失败: %s" % draw_info["err_msg"]

    # 获取用户信息
    def get_user_info(self):
        info_url = "https://api.juejin.cn/user_api/v1/user/get"
        response = requests.get(url=info_url, cookies=self.cookies)
        print(response.text)
