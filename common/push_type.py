#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-09-28 11:02
# @Author  : jiale
# @Site    : 消息推送的类型值
# @File    : push_type.py
# @Software: PyCharm
from enum import Enum, unique


@unique
class PushType(Enum):
    WX = 1,
    BARK = 2