# @author: Z
# @time: 2021/7/23 15:46
# @desc:读取配置文件
import configparser
import os


class configRW:

     def configR(self, section):

        # 绝对路径
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        # 实例化configParser对象
        cf = configparser.ConfigParser()

        # 读取ini文件
        cf.read(BASE_DIR+'/config.ini')
        # print(cf.items(section))
        # print(type(cf.items(section)))

        # list_ = []
        # for sections in config.sections():
        # for a, b in cf.items(section):
        #     # print(a)
        #     # print(type(a))
        #     dict_ = {a: b}
        #     list_.append(dict_)
        # return list_

        dict_data = {}
        for i in cf.items(section):
            key = i[0]
            value = i[1]
            dict_data[key] = value
        return dict_data
        # section(节点)：【Excel】节点
        # 节点可包含多个键值对：option(选项)表示{}里的键值对
        # s=config.sections()
        # o=config.options(section)




        # # -Excel（section）得到该section的所有键值对
        # Iteam=config.items('Excel')
        # print(Iteam)
        #
        # for a,b in Iteam:
        #     print(b)


        # -get(section,option)得到section中option的值，返回为string类型
        # workbook=config.get('Excel', 'workbook')
        # sheet=config.get('Excel', 'sheet')
        # print(sheet)

