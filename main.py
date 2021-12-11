#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-11-13 11:45
# @Author  : tangjiale
# @Desc    : 
# @File    : main.py
# @Software: PyCharm
from youdaonote import note_checkin
from woshipm import woshipm_checkin
from sttcloud import stt_checkin
from pmquanzi import quanzi_checkin
from juejin import juejin_checkin

# 1. 有道云笔记
note = note_checkin.NoteCheckin()
note.checkin()

# 2. 人人都是产品经理
wspm = woshipm_checkin.WoShiPmCheckin()
wspm.login()
wspm.checkin()

# 3. sttcloud
stt = stt_checkin.SttCheckin()
stt.login()
stt.checkin()

# 4. 管理圈
qz = quanzi_checkin.QuanziCheckin()
qz.login()
qz.checkin()

# 5. 掘金
juejin = juejin_checkin.JueJinCheckin()
juejin.checkin()
juejin.draw()
