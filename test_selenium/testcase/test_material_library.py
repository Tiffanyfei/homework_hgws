from test_selenium.page.main import Main
from test_selenium.page.managetools import ManageTools
from test_selenium.page.material_library import MaterialLibrary


class TestMaterialLibrary:
    def setup(self):
        self.main=Main(reuse=True)
        self.manage=ManageTools(reuse=True)
        self.material_library=MaterialLibrary(reuse=True)

    def test_add_picture(self):
        self.main.goto_manage_tools()
        self.manage.goto_material_library()
        self.material_library.add_pacture('/Users/chenyifei/Documents/图片/Jietu20180523-143249.jpg')
        self.material_library.add_pacture_right('Jietu20180523-143249.jpg')


