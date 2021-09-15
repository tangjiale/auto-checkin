#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 推送微信消息
# @File    : push_wx_message.py
# @Software: PyCharm
import requests


# 推送信息到微信
# @param uid wxPusher的用户id
# @param message 推送消息
def push_message(uid, message):
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

# stt.push_message("UID_qNCI9uES2zahjmm8W3iGZAEB07sv", "您似乎已经签到过了...")
