from test_selenium.page.main import Main
from test_selenium.page.manage import Manage
from test_selenium.page.manageTools import ManageTools


class TestManageTools:
    def setup(self):
        self.main=Main(reuse=True)
        self.manage=Manage(reuse=True)
        self.managetools=ManageTools(reuse=True)

    def test_add_picture(self):
        self.main.goto_manage()
        self.manage.goto_managetools()
        self.managetools.add_pacture('/Users/chenyifei/Documents/图片/Jietu20180523-143249.jpg')
        self.managetools.add_pacture_right('Jietu20180523-143249.jpg')


