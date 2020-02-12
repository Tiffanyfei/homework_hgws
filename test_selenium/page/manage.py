from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Manage(BasePage):

    def goto_managetools(self):
        locator = (By.CSS_SELECTOR,'.manageTools_cnt_item:nth-child(5)')
        self.find(locator).click()



