from test_selenium.page.contact import Contact
from test_selenium.page.main import Main


class TestContact:
    def setup(self):
        self.contact=Contact(reuse=True)

    def test_add_user(self):
        """
        测试添加用户
        :return:
        """
        self.contact.add_member("ccc77",'ccc77','13312341240')
        self.contact.get_js_right('保存成功')

    def test_edit_user(self):
        """
        测试编辑用户
        :return:
        """
        self.contact.edit_member('aaaedit','13300001111')
        self.contact.get_js_right('保存成功')

    def test_del_user(self):
        """
        测试删除用户
        :return:
        """
        self.contact.del_member()
        self.contact.get_js_right('正在删除')






