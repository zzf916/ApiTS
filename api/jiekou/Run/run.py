# @author: Z
# @time: 2021/7/29 18:58
# @desc:
# -*- coding: utf-8 -*-
import HTMLTestRunner
import os
import time
import unittest

# 获取当前py文件绝对路径
cur_path = os.path.dirname(__file__)

def all_test():
    case_path = os.path.join(cur_path, '../caseTQ')
    suite = unittest.TestLoader().discover(start_dir=case_path, pattern="apicase.py", top_level_dir=None)
    return suite


if __name__ == '__main__':
    report_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../report'))
    # unittest.main()
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # print(now)
    # 2、html报告文件路径
    report_abspath = os.path.join(report_path, "result_" + now + ".html")
    # print(report_abspath)

    # 3、打开一个文件，将result写入此file中
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=r'接口自动化测试报告,测试结果如下：', description=r'用例执行情况：', tester=r'zzf')
    # 4、调用add_case函数返回值
    runner.run(all_test())
    fp.close()