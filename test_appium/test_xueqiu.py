from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "test"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["automationName"]="UiAutomator2"
        caps['dontStopAppOnReset']=True
        caps["noReset"]=True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        sleep(10)
        # self.driver.quit()

    #作业二
    def test_search(self):
        self.driver.find_element(MobileBy.ID,"tv_search").click()
        self.driver.find_element(MobileBy.ID,"search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.XPATH,"//*[@text='09988']").click()
        assert float(self.driver.find_element(MobileBy.ID,'current_price').text)>200

    #作业三
    def test_join(self):
        # 获取加自选的股票名称
        example=self.driver.find_element(MobileBy.ID,"stock_name_one").text

        # #添加一个涨幅第一的股票
        # self.driver.find_element(MobileBy.ID,"stock_one").click()
        # self.driver.find_elements(MobileBy.ID,"floating_action_image_view_id")[3].click()
        # self.driver.find_element(MobileBy.ID,"tv_left").click()
        #
        # #返回首页
        # self.driver.find_element(MobileBy.ID,"action_back").click()

        #搜索这个股票
        self.driver.find_element(MobileBy.ID, "tv_search").click()
        self.driver.find_element(MobileBy.ID, "search_input_text").send_keys(example)
        self.driver.find_element(MobileBy.ID, "code").click()
        # assert "已添加"==self.driver.find_element(MobileBy.ID,"followed_btn").get_attribute("text")
        follow_button=self.driver.find_element(MobileBy.XPATH, '//*[@text="%s"]/../../android.widget.LinearLayout[3]/android.widget.TextView'%example)
        assert 'com.xueqiu.android:id/followed_btn' ==follow_button.get_attribute('resource-id')

    def test_scroll(self):
        size=self.driver.get_window_size()
        print(size)
        for i in range(5):
            TouchAction(self.driver).long_press(x=size['width']*0.5,y=size['height']*0.8)\
                .move_to(x=size['width']*0.5,y=size['height']*0.01)\
                .release().perform()

    def test_driver(self):
        self.driver.background_app(5)
        self.driver.lock(5)
        self.driver.unlock()


















