#coding=utf-8
from framework.base_page import BasePage

class SportNewsHomePage(BasePage):
    # NBA入口
    nba_link = "//div[@class='schedule clearfix']/ul/li[1]/a"

    def click_nba_link(self):
        self.click(self.nba_link)
