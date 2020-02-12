from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.page.base_page import BasePage


class MaterialLibrary(BasePage):


    def wait_click(self, element):
        WebDriverWait(self._driver, 60).until(
            expected_conditions.visibility_of_element_located(element))

    def add_pacture(self,path):
        self.find((By.LINK_TEXT,'图片')).click()
        self.find((By.LINK_TEXT,'添加图片')).click()
        self.find((By.ID, "js_upload_input")).send_keys(path)
        self.wait_click((By.CSS_SELECTOR,'.dialog_box .material_picCard_cnt_pic'))
        self.find((By.LINK_TEXT,'完成')).click()

    def add_pacture_right(self,pacture_name):
        assert pacture_name in self.find((By.CSS_SELECTOR,'.ww_tab_cnt_inside .material_picCard_text')).text