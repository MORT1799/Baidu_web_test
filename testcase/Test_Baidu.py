from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 处理鼠标事件
from selenium.webdriver.support.select import Select  # 用于处理下拉框
from selenium.common.exceptions import *  # 用于处理异常
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait  # 用于处理元素等待
import time
import unittest
from class_package import test_Baidu_class


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = test_Baidu_class.Act()

    def test1_open(self):

        # 打开网址
        judge = self.driver.open(url="http://www.baidu.com")
        print(judge)

        # 断言
        self.assertTrue(judge)

    def test2_search(self):

        # 搜索
        s = 'selenium'
        title = self.driver.search(content=s, num=2)

        # 断言
        self.assertEqual(s+'_百度搜索', title)

    def test3_back(self):
        self.driver.back()

    def test4_link(self):

        s = '新闻'
        title = self.driver.link(s)

        self.assertIn(s, title)

    def test5_setting(self):

        judge = self.driver.setting(content1='搜索设置', content2='prefpanelgo')

        # 断言
        self.assertTrue (judge)

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        time.sleep(3)
        driver.quit()


