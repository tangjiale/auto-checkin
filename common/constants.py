#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-11-13 14:45
# @Author  : tangjiale
# @Desc    : 
# @File    : constants.py
# @Software: PyCharm
import os

# 环境变量
env = os.environ

# system
push_type = env.get("PUSH_TYPE")

# stt
stt_main = env.get("STT_DOMAIN")
stt_username = env.get("STT_USER_NAME")
stt_password = env.get("STT_PASSWORD")

# 管理圈
pmqz_username = env.get("PMQZ_USER_NAME")
pmqz_password = env.get("PMQZ_PASSWORD")

# 人人都是产品经理
wspm_username = env.get("WSPM_USER_NAME")
wspm_password = env.get("WSPM_PASSWORD")

# 有道云笔记
ynote_cookie = env.get("YNOTE_COOKIE")

# ios bark
bark_key = env.get("BARK_KEY")

# 微信公众号
weixin_userId = env.get("WEIXIN_UID")
weixin_appToken = env.get("WEIXIN_APP_TOKEN")
