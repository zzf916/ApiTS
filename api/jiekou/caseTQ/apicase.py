# @author: Z
# @time: 2021/7/20 19:29
# @desc:
import HTMLTestRunner
import json
import os
import time
import unittest
import pytest

from ddt import ddt, data, unpack

from ExcelRW.ExRW import RWexcel
from log.logsa import MyLogging
from caseTQ.apikey import Apikw



log = MyLogging().logger
# 读Excel 获取数据
def getExcelData(sheet):
    list_ = RWexcel(sheet).Rexcel()
    # print(list_)
    return list_


# 用来装饰测试类
@ddt
class TestCase(unittest.TestCase):
    '''接口测试类下'''
    @classmethod
    def setUpClass(cls) -> None:
        # cls.log = MyLogging().logger
        cls.b=1
        cls.ak = Apikw()
        cls.token = None
        cls.cityid = None
        cls.success = None


    # 装饰测试方法，拿到几个数据就执行几条用例 *表示解包 只能去掉最外层括号
    @data(*getExcelData('Sheet1'))
    # 拆分数据 按”，“拆分
    @unpack
    def test_1_tq(self, **kwargs):
        '''天气接口测试1'''

        # 日志
        log.info("【开始执行测试用例：{}】".format(kwargs['用例名']))
        # print('Excel数据:\n' + str(kwargs)+ '\n')
        # print(kwargs['excett'])
        c = kwargs['excett'].split("，")
        log.info("用例设置检查点：%s" % c)
        log.info("请求url：%s" % kwargs['url'])
        log.info("请求参数：%s" % kwargs['data'])

        # 获取响应结果
        response =self.ak.methon(**kwargs)
        log.info("返回数据：%s" % response.text)

        a=self.ak.ckeck(kwargs['excett'], response.text)

        # print(a)
        k = self.b + 1
        TestCase.b = k

        if False in a:
            log.info("【测试结果：失败】" + '\n')
            RWexcel('Sheet1').Wexcel(k, 9, "Failed")
        else:
            log.info("【测试结果：成功】" + '\n')
            RWexcel('Sheet1').Wexcel(k, 9, "Pass")
            # self.assertNotIn(False, a, msg="检查点数据与实际返回数据一致")
        self.assertNotIn(False, a, msg="检查点数据与实际返回数据不一致")

        # 赋值
        TestCase.success=self.ak.get_text(response.text, 'success')

        # print(self.ak.get_text(response.text, 'citynm'))


    def test_2_tq(self):
        '''天气接口测试2'''
        print(self.success)
    def test_3_tq(self):
        '''天气接口测试3'''
        pass


# if __name__ == '__main__':
#     report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../report'))
#     # unittest.main()
#     now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#     print(now)
#     # 2、html报告文件路径
#     report_abspath = os.path.join(report_path, "result_" + now + ".html")
#     print(report_abspath)
#
#     # 3、打开一个文件，将result写入此file中
#     fp = open(report_abspath, "wb")
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=r'接口自动化测试报告,测试结果如下：', description=r'用例执行情况：')
#     # 4、调用add_case函数返回值
#     runner.run(unittest.main())
#     fp.close()
