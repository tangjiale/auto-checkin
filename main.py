#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-11-13 11:45
# @Author  : tangjiale
# @Desc    : 
# @File    : main.py
# @Software: PyCharm
from checkin import juejin, quanzi, sttcloud, woshipm, ynote

# 1. 有道云笔记
note = ynote.NoteCheckin()
note.checkin()

# 2. 人人都是产品经理
wspm = woshipm.WoShiPmCheckin()
wspm.login()
wspm.checkin()

# 3. sttCloud
stt = sttcloud.SttCheckin()
stt.login()
stt.checkin()

# 4. 管理圈
qz = quanzi.QuanziCheckin()
qz.login()
qz.checkin()

# 5. 掘金
jj = juejin.JueJinCheckin()
jj.checkin()
jj.draw()
