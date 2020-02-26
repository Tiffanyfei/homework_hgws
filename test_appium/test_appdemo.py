from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class Testappdemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        # caps["noReset"] = True
        # caps["dontStopAppOnReset"] = True
        # caps["unicodeKeyboard"] = True
        # caps["resetKeyboard"] = True
        caps["skipServerInstallation"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def teardown(self):
        pass
        #sleep(10)
        # self.driver.quit()

    def test_demo(self):
        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Views").instance(0));')
        self.driver.find_element(*scroll_to_element).click()

        scroll_to_element = (
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable('
            'new UiSelector().scrollable(true).instance(0))'
            '.scrollIntoView('
            'new UiSelector().text("Popup Menu").instance(0));')
        self.driver.find_element(*scroll_to_element).click()
        # self.driver.find_element(By.XPATH, "//*[@text='MAKE A POPUP!']").click()
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Make a Popup!").click()
        self.driver.find_element(By.XPATH, "//*[@text='Search']").click()
        toast = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        assert "Search" in toast
        assert "Clicked" in toast


















