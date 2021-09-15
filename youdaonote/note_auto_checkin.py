#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 用于有道笔记自动签到获取存储空间
# @File    : note_auto_checkin.py
# @Software: PyCharm
from push_wx_message import *


class NoteAutoCheckin:

    def __init__(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01"
        }
        self.cookies = {}

    # 签到
    # @param uid 微信用户id
    def checkin(self, uid):
        checkin_url = "http://note.youdao.com/yws/mapi/user?method=checkin"
        response = requests.post(url=checkin_url, cookies=self.cookies)
        resp_data = eval(response.text.encode().decode("unicode_escape"))
        print(resp_data)
        # 推送微信消息
        push_message(uid, resp_data["msg"])


# 请求数据
req_data_list = [
    {
        'cookie': 'YNOTE_FORCE=true; YNOTE_SESS=v2|Nu56ORnwBVzWhHkEh4UA0pFkfJB6LqZ0P4OLlGPMTyRTZh4OMnHJZ0k5hLzfPMqB0kWn4OGk4PB0OWh4llOfkG0kMP4PFhLlW0; YNOTE_LOGIN=5||1630747833014; JSESSIONID=aaacd-PKzHyS37I_jQJTx',
        "uid": "UID_qNCI9uES2zahjmm8W3iGZAEB07sv"
    }
]
note = NoteAutoCheckin()
for req_data in req_data_list:
    note.cookies = req_data["cookie"]
    note.checkin(req_data["uid"])
