#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 用于有道笔记自动签到获取存储空间
# @File    : note_checkin.py
# @Software: PyCharm
import json
import requests
from common import constants
from common.push_message import push_message
from common.title_type import TitleType


class NoteCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Content-Type": "text/json; charset=utf-8"
        }
        cookies_str = constants.ynote_cookie
        cookies_dict = {}
        for cookie in cookies_str.split('; '):
            cookies_dict[cookie.split('=')[0]] = cookie.split('=')[-1]
        self.cookies = cookies_dict

    # 签到
    # @param uid 微信用户id
    def checkin(self):
        checkin_url = "https://note.youdao.com/yws/mapi/user?method=checkin"
        response = requests.post(url=checkin_url, cookies=self.cookies)
        resp_data = json.loads(response.text)
        print("%s签到响应：%s" % (TitleType.YNote.value[0], resp_data))
        if "error" in resp_data:
            push_message(TitleType.YNote.value[0], "签到失败,%s" % resp_data["message"])
        else:
            if resp_data["success"] == 1:
                success_msg = "签到成功，增加空间: %dM" % (resp_data["space"] / 1024 / 1024)
                # 推送微信消息
                push_message(TitleType.YNote.value[0], success_msg)
            else:
                push_message(TitleType.YNote.value[0], "签到失败")

    def get_user_info(self):
        info_url = "https://note.youdao.com/yws/api/self?ClientVer=61000010000&GUID=PCaf5d9a6fe329076c9&client_ver=61000010000&device_id=PCaf5d9a6fe329076c9&device_name=DESKTOP-PBA1643&device_type=PC&keyfrom=pc&method=get&os=Windows&os_ver=Windows%2010&subvendor=&vendor=website&vendornew=website"
        response = requests.post(url=info_url, cookies=self.cookies)
        print(response.text)


# 请求数据
# note = NoteCheckin()
# # # note.get_user_info()
# note.checkin()
