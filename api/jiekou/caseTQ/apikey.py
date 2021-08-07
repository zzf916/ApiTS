# @author: Z
# @time: 2021/7/20 19:08
# @desc:
import json

import jsonpath as jsonpath
import requests
import unittest

from log.logsa import MyLogging

log = MyLogging().logger
class Apikw:
    # # get请求
    # def get(self, url=None, headers=None, data=None):
    #     return requests.get(url=url, headers=headers, data=data)
    # post请求
    # def post(self, **kwargs):
    #     return requests.post(url=kwargs['url'], headers=kwargs['headers'], data=eval(kwargs['data']), json=kwargs['json'])

    # 请求方法
    def methon(self, **kwargs):

        # lower()转换字符串中大写为小写
        if kwargs['methon'].lower() =='post':

            res =requests.post(url=kwargs['url'], headers=kwargs['headers'],  json=eval(kwargs['data']))
            return res

        if kwargs['methon'].lower() =='get':

            res =requests.post(url=kwargs['url'], headers=kwargs['headers'],  data=eval(kwargs['data']))
            return res

    # 获取数据
    def get_text(self, res, key):

        if res is not None:
            try:
                text= json.loads(res)
                value= jsonpath.jsonpath(text, '$..{0}'.format(key))
                # print(type(value))
                # jsonpath获取的结果是list
                if len(value)== 1:
                    return value[0]
                else:
                    return value
            except Exception as e:
                return e
        else:
            return None

    # 赋值函数 可用于接口关联
    def fuzhi(self, kwargs):
        for key, value in kwargs.items():
            if type(value) is dict:
                self.fuzhi(value)

            else:
                kwargs[key] = getattr(self, key)
        return kwargs

    # 检查点
    def ckeck(self, exc, res):
        c=exc.split("，")
        lis = []
        for i in range(0, len(c)):
            real = self.get_text(res, c[i].split('=')[0])
            # print(c[i].split('=')[0])
            checkPoint_dict = {c[i].split('=')[0]: c[i].split('=')[1]}
            # print(c[i].split('=')[1])
            # print(checkPoint_dict)
            check = checkPoint_dict[c[i].split('=')[0]]
            # print(check)
            log.info("检查点数据{}：{},返回数据：{}".format(i+1, check, real))
            # print("检查点数据：{},返回数据：{}".format(check, real))


            lis.append(str(real) == str(check))

        return lis


