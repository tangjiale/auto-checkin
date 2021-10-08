#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-10-08 09:42
# @Author  : jiale
# @Site    : 消息标题类型
# @File    : title_type.py
# @Software: PyCharm
from enum import Enum, unique


@unique
class TitleType(Enum):
    CSDN = "CSDN",
    PMQZ = "PM圈子",
    STT = "SttCloud",
    WSPM = "人人都是产品经理"
    YNote = "有道云笔记"
