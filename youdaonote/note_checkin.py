#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 用于有道笔记自动签到获取存储空间
# @File    : note_checkin.py
# @Software: PyCharm
import json
import requests


class NoteCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Content-Type": "text/json; charset=utf-8"
        }
        cookies_str = "OUTFOX_SEARCH_USER_ID=829440896@118.122.120.118; JSESSIONID=aaa3DvhjED3UUbD0evHVx; YNOTE_SESS=v2|ocoqFOpFjVw4Ofgu0Mlf0eunHlWn4eyRYEnMlWhfOMRQLRfQSO4lW0OY64UWn4JyR6ynfQBnHqy0w4RflmOfqFRY5nflGn4gyR; YNOTE_LOGIN=3||1631757132180"
        cookies_dict = {}
        for cookie in cookies_str.split('; '):
            cookies_dict[cookie.split('=')[0]] = cookie.split('=')[-1]
        self.cookies = cookies_dict

        self.uid = "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"
        # 当前应用消息title
        self.title = "有道云笔记"

    # 签到
    # @param uid 微信用户id
    def checkin(self, uid):
        checkin_url = "https://note.youdao.com/yws/mapi/user?method=checkin"
        response = requests.post(url=checkin_url, cookies=self.cookies)
        resp_data = json.loads(response.text)
        print(resp_data)

        if resp_data["success"] == 1:
            success_msg = "%s: 签到成功，增加空间: %dM" % (self.title, resp_data["space"] / 1024 / 1024)
            # 推送微信消息
            self.push_message(uid, success_msg)
        else:
            self.push_message(uid, "%s: 签到失败")

    def get_user_info(self):
        info_url = "https://note.youdao.com/yws/api/self?ClientVer=61000010000&GUID=PCaf5d9a6fe329076c9&client_ver=61000010000&device_id=PCaf5d9a6fe329076c9&device_name=DESKTOP-PBA1643&device_type=PC&keyfrom=pc&method=get&os=Windows&os_ver=Windows%2010&subvendor=&vendor=website&vendornew=website"
        response = requests.post(url=info_url, cookies=self.cookies)
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
note = NoteCheckin()
# # note.get_user_info()
note.checkin(note.uid)
