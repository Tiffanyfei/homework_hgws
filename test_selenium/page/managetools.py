from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class ManageTools(BasePage):

    #前往素材库
    def goto_material_library(self):
        locator = (By.CSS_SELECTOR,'.manageTools_cnt_item:nth-child(5)')
        self.find(locator).click()



