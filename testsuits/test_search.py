# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class Baidu_Search(unittest.TestCase):
    @classmethod # 类方法（不需要实例化类就可以被类本身调用）
    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    @classmethod # 类方法（不需要实例化类就可以被类本身调用）
    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.quit()

    def test_(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        homepage = HomePage(self.driver)
        '''在当前测试类里面，self.driver是来自浏览器引擎类中方法得到的，在初始化一个页面对象的时候，也把这个来自浏览器引擎类的driver给赋值给当前的页面对象，这样，才能执行页面对象或者基类里面的相关driver方法'''
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'python' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

    def test_search_python(self):
        homepage = HomePage(self.driver)
        homepage.type_search('python')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        time.sleep(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
            print ('Test Pass.')
        except Exception as e:
            print ('Test Fail.', format(e))

if __name__ == '__main__':
    unittest.main()