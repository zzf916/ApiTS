# # # @author: Z
# # # @time: 2021/7/23 1:06
# # # @desc:
# # -*- coding: utf-8 -*-
# # from ddt import ddt, data, unpack, file_data
# # import requests
# #
# # from ExcelRW.ExRW import RWexcel
# # from caseTQ.apikey import Apikw
# #
# # # lsit_ = RWexcel().Rexcel()
# # # print(lsit_)
# # # for case in lsit_:
# # #     id = case.get('id')
# # #     url = case.get('url')
# # #     data_ = eval(case.get('data'))
# # #
# # #     methon = case.get('methon')
# # #     excett = case.get('excett')
# # #     # i = i + 1
# # #     RWexcel().Wexcel(id + 1, 7, '实际结果2')
# # #     response = Apikw().post(url=url, json=data_)
# #
# # # url = 'http://api.k780.com'
# # # da = {
# # #     'app': 'weather.today',
# # #     'weaId': '1',
# # #     'appkey': '60311',
# # #     'sign': '1cf54158f5308f6107b5c0596b27a1c0',
# # #     'format': 'json',
# # # }
# #
# #     # print(response.text)
# #
# # # # 赋值
# # # Apicse.token = self.ak.get_text(response.text, 'token')
# # # try:
# # #     b = response.json()
# # #     dic= self.fuzhi(b)
# # #     Apicse.success = dic['success']
# # #     Apicse.cityid= dic['cityid']
# # # except AttributeError as e:
# # #     print(e)
# #
# # # r = response.text
# # # print(response.text)
# #     # response =requests.post(url=url, headers=None, json=data)
# #     # print(response.text)
# #     # print('------------------')
# #
# # import unittest
# # a=[{'workbook': 'F:\\sd\\sd\\ExcelRW\\case.xlsx', 'sheet1': 'Sheet1 , 'sheet2': 'sheet2'}]
# #
# # @ddt
# # class test(unittest.TestCase):
# #     @data(a)
# #     @unpack
# #     def test_1(self, *args):
# #
# #         print('====')
# #         print(args[1])
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
# # from Rconfig.configRW import configRW
# #
# # a = configRW().configR('email')
# #
# # print(a)
#
#
# import jsonpath
# # checkPoint='citynm=北京，cityid=101010100'
# # c = checkPoint.split("，")
# # flag = None
# # for i in range(0, len(c)):
# #     checkPoint_dict = {}
# #     checkPoint_dict[c[i].split('=')[0]] = c[i].split('=')[1]
# #     print( checkPoint_dict)
# #     print(c[i].split('=')[1])
#     # jsonpath方式获取检查点对应的返回数据
#     # list = jsonpath.jsonpath(res, c[i].split('=')[0])
#     # value = list[0]
#     # check = checkPoint_dict[c[i].split('=')[0]]
#     # log.info("检查点数据{}：{},返回数据：{}".format(i + 1, check, value))
#     # print("检查点数据{}：{},返回数据：{}".format(i + 1, check, value))
#     # # 判断检查点数据是否与返回的数据一致
#     # flag = IsInstance().get_instance(value, check)
#
# # if flag:
# #     log.info("【测试结果：通过】")
# #     ExcelData(file_path, sheet_name).write(rowNumber + 1, 12, "Pass")
# # else:
# #     log.info("【测试结果：失败】")
# #     ExcelData(file_path, sheet_name).write(rowNumber + 1, 12, "Fail")
#
# # # 断言
# # self.assertTrue(flag, msg="检查点数据与实际返回数据不一致")
#
# # -*- coding:utf-8 -*-
# import unittest
# import os
# import time
# import HTMLTestRunner
#
# # 用例路径
# case_path = os.path.join(os.getcwd())
# # 报告存放路径
# report_path = os.path.join(os.getcwd(), 'report')
# print (report_path)
#
# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
#
#     print (discover)
#     return (discover)
#
# if __name__ == '__main__':
#     # 1、获取当前时间，这样便于下面的使用。
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#
#     # 2、html报告文件路径
#     report_abspath = os.path.join(report_path, "result_"+now+".html")
#
#     # 3、打开一个文件，将result写入此file中
#     fp = open(report_abspath, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=r'接口自动化测试报告,测试结果如下：',description=r'用例执行情况：')
#     # 4、调用add_case函数返回值
#     runner.run(all_case())
#     fp.close()
#
from Rconfig.configRW import configRW
#
a = configRW().configR('mysql')
print(a)

# def list_dict(list_data):
#    dict_data = {}
#    for i in list_data:
#        key= i[0]
#        value= i[1]
#        dict_data[key] = value
#    return dict_data
#
#
# if __name__ == '__main__':
#     list_data = [('aa','aa'),
#                  ('bb','bb'),
#                  ('cc','cc'),
#                  ('dd','dd')]
#     print(list_dict(list_data))
#     # list_data = [{'aa': 'aa'},
#     #              {'bb': 'bb'},
#     #              {'cc': 'cc'},
#     #              {'dd': 'dd'}]
