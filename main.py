#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-11-13 11:45
# @Author  : tangjiale
# @Desc    : 
# @File    : main.py
# @Software: PyCharm
from checkin import juejin, quanzi, sttcloud, woshipm, ynote, huke
from common.push_message import push_message
from common.title_type import TitleType

# 需要推送的消息内容
# push_msg = ""

# 1. 有道云笔记 签到获取存储空间
# note = ynote.NoteCheckin()
# note_resp_checkin = note.checkin()
# # 推送消息
# push_message(TitleType.YNote.value[0], note_resp_checkin)


# 2. 人人都是产品经理 签到获得积分
# wspm = woshipm.WoShiPmCheckin()
# wspm_resp_checkin = wspm.checkin()
# 推送消息
# push_message(TitleType.WSPM.value[0], wspm_resp_checkin)

# 3. sttCloud 签到获得流量
stt = sttcloud.SttCheckin()
stt_resp_checkin = stt.checkin()
# 推送消息
push_message(TitleType.STT.value[0], stt_resp_checkin)

# 4. 管理圈 签到获得积分
# qz = quanzi.QuanziCheckin()
# qz_resp_checkin = qz.checkin()
# # 推送消息
# push_message(TitleType.PMQZ.value[0], qz_resp_checkin)

# 5. 掘金 签到获得钻石并抽奖，并沾福气
jj = juejin.JueJinCheckin()
resp_checkin = jj.checkin()
resp_draw = jj.draw()
resp_dip_luck = jj.dip_luck_list()
jj_msg = "签到：%s\n抽奖：%s \n沾福气：%s" % (resp_checkin, resp_draw, resp_dip_luck)
# 推送消息
#push_message(TitleType.JueJin.value[0], jj_msg)

# 6. 虎课网签到得虎课币
# hk = huke.HuKeCheckin()
# hk_resp_checkin = hk.checkin()
# push_message(TitleType.HuKe.value[0], hk_resp_checkin)
