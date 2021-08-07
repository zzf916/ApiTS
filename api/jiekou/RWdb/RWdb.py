# @author: Z
# @time: 2021/8/1 20:17
# @desc:数据库
# -*- coding: utf-8 -*-
from Rconfig.configRW import configRW

dbdata=configRW().configR('mysql')
print(dbdata)