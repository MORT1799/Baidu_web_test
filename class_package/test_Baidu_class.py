from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains  # 处理鼠标事件
from selenium.webdriver.support.select import Select  # 用于处理下拉框
from selenium.common.exceptions import *  # 用于处理异常
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait  # 用于处理元素等待
import time


class Act(object):

    def __init__(self):

        self.driver = webdriver.Chrome("F:\Anaconda3\chromedriver.exe")
        # 隐性等待。设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
        self.driver.implicitly_wait(10)

    def open(self, url):

        # 通过浏览器向服务器发送URL请求
        self.driver.get(url)

        # 窗口最大化
        # self.driver.maximize_window()

        # 打印当前页面title
        title = self.driver.title
        print('当前页面title：', title)

        # 打印当前页面URL
        now_url = self.driver.current_url
        print('当前页面URL：', now_url)

        judge = WebDriverWait(self.driver, 30).until(ec.title_contains('百度一下'))

        return judge

    def search(self, content, num=None):
        self.driver.find_element_by_id("kw").send_keys(content)

        # 鼠标点击搜索
        self.driver.find_element_by_id("su").click()
        time.sleep(3)

        # 获得百度搜索窗口句柄
        search_window = self.driver.current_window_handle

        # 打印当前页面title
        title = self.driver.title
        print('当前页面title：', title)

        # 打印当前页面URL
        now_url = self.driver.current_url
        print('当前页面URL：', now_url)

        # 获取结果数目
        user = self.driver.find_element_by_class_name('nums').text
        print(user)

        # 定位一组元素,获得搜索出的当前页面的链接
        elements = self.driver.find_elements_by_xpath('//div/h3/a')
        print('当前搜索页面的元素：', elements)

        # 循环遍历出每一条搜索结果的标题
        if num is not None:
            c = 0
            for t in elements:
                print('第%s条搜索结果的标题:' % t, t.text)
                element = self.driver.find_element_by_link_text(t.text)
                element.click()
                time.sleep(3)
                c = c + 1
                if c == num:
                    break

        # 回到搜索窗口
        self.driver.switch_to.window(search_window)
        time.sleep(3)

        return title

    def back(self):
        self.driver.back()
        print('返回百度首页')
        time.sleep(2)

    def setting(self, content1, content2):
        # 定位到要悬停的元素
        element = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')

        # 对定位到的元素执行鼠标悬停操作
        ActionChains(self.driver).move_to_element(element).perform()

        # 找到链接
        elem1 = self.driver.find_element_by_link_text(content1)
        elem1.click()

        # 通过元素选择器找到id=sh_2,并点击设置
        elem2 = self.driver.find_element_by_id("sh_1")  # //*[@id="sh_1"]是否显示搜索历史
        elem2.click()

        # 保存设置
        elem3 = self.driver.find_element_by_class_name(content2)
        elem3.click()

        # 打开alert需要给缓冲时间，否则出现 No alert is active 错误
        time.sleep(1)
        judge = True
        try:
            # 保存成功，出现弹窗
            # 点击确认
            self.driver.switch_to.alert.accept()
            # driver.switch_to_alert().dismiss() #取消
            # driver.switch_to_alert().send_keys("只对prompt有效") #在弹出框输入内容
        except Exception as e:
            print(e)
            judge = False
        time.sleep(2)
        print('完成搜索设置')

        return judge

    def link(self, content):
        # 获得当前窗口句柄
        window = self.driver.current_window_handle

        self.driver.find_element_by_link_text(content).click()
        time.sleep(3)

        # 打印当前页面title
        title = self.driver.title
        print('当前页面title：', title)

        # 回到之前的窗口
        self.driver.switch_to.window(window)

        time.sleep(2)

        return title

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    driver = Act()
    driver.open("http://www.baidu.com")
    driver.search('selenium', num=2)
    driver.back()
    driver.link('新闻')
    driver.setting('搜索设置', 'prefpanelgo')
    driver.quit()

