from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class Contact(BasePage):
    _add_member_button=(By.CSS_SELECTOR, "xxxx")

    #添加成员
    def add_member(self, username,acctid,mobile):
        name_locator=(By.NAME, 'username')
        acctid_locator=(By.NAME, 'acctid')
        mobile_locator=(By.NAME, 'mobile')
        button=(By.LINK_TEXT,'保存')
        self.find(name_locator).send_keys(username)
        self.find(acctid_locator).send_keys(acctid)
        self.find(mobile_locator).send_keys(mobile)
        self.find(button).click()

    def add_member_right(self,data):
        data_list=self.finds((By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)'))
        list=[]
        for x in data_list:
            list.append(x.text)
        assert data in list

    def edit_member(self,username,mobile):
        locator=(By.XPATH, '//*[@id="member_list"]/tr[1]/td[7]')
        WebDriverWait(self._driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )
        sleep(3)
        self.find(locator).click()
        self.find((By.LINK_TEXT,'编辑')).click()

        name_locator = (By.NAME, 'username')
        mobile_locator = (By.NAME, 'mobile')
        button = (By.LINK_TEXT, '保存')
        #先删除再填充
        self.clear_input(name_locator)
        self.find(name_locator).send_keys(username)
        self.clear_input(mobile_locator)
        self.find(mobile_locator).send_keys(mobile)
        self.find(button).click()

    def edit_member_right(self):
        assert '保存成功' in self.find((By.ID,'js_tips')).text




    def add_member_error(self, data):
        return AddMemberPage()


    def search(self, name):
        pass

    def import_users(self, data):
        pass

    def export_users(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass
