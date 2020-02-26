from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"] = "UiAutomator2"
        # caps['dontStopAppOnReset']=True
        # caps["noReset"]=True
        caps["unicodeKeyboard"] = True
        caps["chromedriverExecutable"] = "/Users/chenyifei/webdriver/chromedriver_v2.20"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        sleep(10)
        self.driver.quit()

    # 作业二
    def test_search(self):
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='股票']").click()
        price = self.driver.find_element(MobileBy.XPATH,
                                         "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]").text
        assert float(price) > 200

    # 作业三
    def test_join(self):
        # 获取加自选的股票名称
        example = self.driver.find_element(MobileBy.ID, "stock_name_one").text

        # #添加一个涨幅第一的股票
        # self.driver.find_element(MobileBy.ID,"stock_one").click()
        # self.driver.find_elements(MobileBy.ID,"floating_action_image_view_id")[3].click()
        # self.driver.find_element(MobileBy.ID,"tv_left").click()
        #
        # #返回首页
        # self.driver.find_element(MobileBy.ID,"action_back").click()

        # 搜索这个股票
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys(example)
        self.driver.find_element(MobileBy.ID, "code").click()
        # assert "已添加"==self.driver.find_element(MobileBy.ID,"followed_btn").get_attribute("text")
        follow_button = self.driver.find_element(MobileBy.XPATH,
                                                 '//*[@text="%s"]/../../android.widget.LinearLayout[3]/android.widget.TextView' % example)
        assert 'com.xueqiu.android:id/followed_btn' == follow_button.get_attribute('resource-id')

    def test_scroll(self):
        size = self.driver.get_window_size()
        print(size)
        for i in range(5):
            TouchAction(self.driver).long_press(x=size['width'] * 0.5, y=size['height'] * 0.8) \
                .move_to(x=size['width'] * 0.5, y=size['height'] * 0.01) \
                .release().perform()

    def test_driver(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()

    def test_webview_context(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()

        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)

        self.driver.switch_to.context(self.driver.contexts[-1])

        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_agu_3ki").click()

        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        phone = (By.ID, 'phone-number')

        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(phone))
        self.driver.find_element(*phone).send_keys("15600534760")

    def test_webview_2(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab')]").click()

        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.contexts) > 1)

        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(By.CSS_SELECTOR, ".trade_home_xueying_SJY").click()

        WebDriverWait(self.driver, 30).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        phone = (By.XPATH, "//input[@placeholder='请输入手机号']")
        ver_code = (By.XPATH, "//input[@placeholder='请输入验证码']")
        button = (By.CSS_SELECTOR, '.open_form-submit_1Ms')
        js_toast = (By.CSS_SELECTOR, '.Toast_toast_22U')
        close = (By.ID, 'action_bar_close')
        back = (By.ID, 'action_bar_back')

        self.driver.switch_to.window(self.driver.window_handles[-1])

        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(phone))

        self.driver.find_element(*phone).send_keys("15600534760")
        self.driver.find_element(*ver_code).send_keys("1234")
        self.driver.find_element(*button).click()

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(js_toast))
        assert '请输入正确的验证码！' in self.driver.find_element(*js_toast).text

        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.switch_to.context(self.driver.contexts[0])

        # 判断页面有没有关闭这个控件，没有就点击后退
        if self.driver.find_elements(*close) == []:
            self.driver.find_element(*back).click()
            print("点击了返回")
        else:
            self.driver.find_element(*close).click()
            print("点击了关闭")



