# coding=utf-8
import time
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.baidu_sport_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
        # 初始化百度首页，并点击新闻链接
        baiduhome = HomePage(self.driver)
        #baiduhome.click_news()
        self.driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_trnews']").click()
        # 初始化一个百度新闻主页对象，点击体育
        newshome = NewsHomePage(self.driver)
        #newshome.click_sports()
        self.driver.find_element_by_xpath("//div[@id='channel-all']/div/ul/li[7]/a").click()
        # 初始化一个体育新闻主页，点击NBA
        sportnewhome = SportNewsHomePage(self.driver)
        #sportnewhome.click_nba_link()
        self.driver.find_element_by_xpath("//div[@class='schedule clearfix']/ul/li[1]/a").click()
        time.sleep(5)
        sportnewhome.get_windows_img()
if __name__ == '__main__':
    unittest.main()