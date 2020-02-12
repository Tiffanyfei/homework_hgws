from test_selenium.page.contact import Contact
from test_selenium.page.main import Main


class TestContact:
    def setup(self):
        self.main=Main(reuse=True)
        self.contact=Contact(reuse=True)

    def test_add_user(self):
        """
        测试添加用户
        :return:
        """
        self.main.goto_add_member()
        self.contact.add_member("ccc55",'ccc55','13312341239')
        self.contact.add_member_right('ccc55')

    def test_edit_user(self):
        """
        测试编辑用户
        :return:
        """
        self.main.goto_contact()
        self.contact.edit_member('edit','13300001111')
        self.contact.edit_member_right()




