#coding=utf-8
import unittest
import os
import time
import HTMLTestRunner
from testsuits.baidu_search import BaiduSearch
from testsuits.test_search import Baidu_Search
from testsuits.test_get_page_title import GetPageTitle


#添加单个测试用例到套件中
'''
suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
suite.addTest(Baidu_Search('test_search_python'))
suite.addTest(GetPageTitle('test_get_title'))
'''
#一次性加载一个类文件下所有测试用例到suite中去
#suite = unittest.TestSuite(unittest.makeSuite(Baidu_Search))

report_path = os.path.dirname(os.path.abspath('.')) + '/testreports/'
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")
#加载一个路径下所有的测试用例
suite = unittest.defaultTestLoader.discover("testsuits")

if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"TestBaidu测试报告", description=u"用例测试情况")
    runner.run(suite)
    fp.close()