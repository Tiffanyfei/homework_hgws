from test_appium.page.app import App



class TestStocks:
    def setup(self):
        self.stocks=App().start().main().goto_stocks()

    def test_stocks_goto_search(self):
        assert '已添加' in self.stocks.stocks_goto_search().search('jd').add_select().get_msg()
        self.stocks.goto_back()
        assert '京东'==self.stocks.get_stocks_name()