#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-06 10:10
# @Author  : jiale
# @Site    : 推送微信消息
# @File    : push_message.py
# @Software: PyCharm
import requests
from common.push_type import PushType


# 统一消息推送
# @param push_type 消息推送类型 PushType
# @param uid 用户id
# @param title 消息标题
# @param message 推送消息
def push_message(push_type: PushType, uid, title, message):
    if push_type == PushType.WX:
        __push_wx_message(uid, title, message)
    elif push_type == PushType.BARK:
        __push_ios_bark_message(uid, title, message, "")
    else:
        print("消息推送类型不存在")


# 推送信息到微信
# @param uid wxPusher的用户id
# @param message 推送消息
def __push_wx_message(uid, title, message):
    push_url = "http://wxpusher.zjiecode.com/api/send/message"
    req_json = {
        "appToken": "AT_cWSuidnpkwufJ5JgF1PverQoF0cQr3No",
        "summary": title,
        "content": message,
        "contentType": 1,
        "uids": [uid]
    }
    header = {
        "Content-Type": "application/json"
    }
    response = requests.post(url=push_url, json=req_json, headers=header)
    print(response.text)


# ios bark 消息通知推送（只能推送ios设置，并必须安装bark应用）
# @param uid 用户唯一key
# @param title 通知消息标题
# @param message 通知消息正文
def __push_ios_bark_message(uid, title, message, category):
    push_url = "https://api.day.app/%s" % uid
    req_json = {
        "title": title,
        "body": message,
        "category": category
    }
    header = {
        "Content-Type": "application/json"
    }
    response = requests.post(url=push_url, json=req_json, headers=header)
    print(response.text)




# stt.push_message("UID_qNCI9uES2zahjmm8W3iGZAEB07sv", "您似乎已经签到过了...")
# push_message(PushType.WX,"PBF2K8wMRPdj5bKhcdiy6G", "管理圈", "您似乎已经签到过了...")