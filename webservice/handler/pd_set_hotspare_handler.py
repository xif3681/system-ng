#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    版权说明：Copyright (c) 2014 AnyRobot, EISOO
    文件作者: Tony.fang@eisoo.com
    @file: pd_set_hotspare_handler.py
    @time: 2016/12/8 21:57
"""
from arpylibs.basehandler.base_handler import BaseHandler
from modules.deco_deal_error import deco_deal_error
from modules.ar_pd_manager import ARPdManager


class PdSetHotSpareHandler(BaseHandler):

    @deco_deal_error
    def post(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        try:
            slot_number = self.get_argument_value('slot_number')
            result = ARPdManager().set_hotspare(slot_number)
            self.write(result)
        except Exception as e:
            self.set_status(202)
            raise e
