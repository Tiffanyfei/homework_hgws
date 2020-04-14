from test_requests.test_wework.api.department import Department

class TestDepartment:

    @classmethod
    def setup(cls):
        cls.department = Department()

    def test_department_create_1(self):
        """
        测试添加部门
        :return:
        """
        r = self.department.create(name='test1', parentid=1)
        assert r['errcode'] == 0
        assert r['errmsg'] == "created"
        assert r['id'] is not None


    def test_department_create_2(self):
        """
        测试添加名称重复
        :return:
        """
        r = self.department.create(name='test1', parentid=1)
        assert r['errcode'] != 0
        assert 'department existed' in r['errmsg']

    def test_department_create_3(self):
        """
        测试部门名称为空
        :return:
        """
        r = self.department.create(name='', parentid=1)
        assert r['errcode'] != 0
        assert 'name exceed min utf8 words 1' in r['errmsg']

    def test_department_create_4(self):
        """
        测试添加二级子部门
        :return:
        """
        r = self.department.create(name='test2', parentid=13)
        assert r['errcode'] == 0
        assert r['errmsg'] == "created"
        assert r['id'] is not None

    def test_department_create_5(self):
        """
        parentid为空
        :return:
        """
        r = self.department.create(name='测试开发', parentid=None)
        assert r['errcode'] != 0
        assert 'parent department not found' in r['errmsg']

    def test_department_list_1(self):
        """
        测试部门查询
        :return:
        """
        r = self.department.list()
        assert r['errcode'] == 0
        assert r['errmsg'] == 'ok'
        assert len(r['department']) > 0

    def test_department_list_2(self):
        """
        测试部门查询
        :return:
        """
        test_id = 3
        r = self.department.list(id=test_id)
        assert r['errcode'] == 0
        assert r['errmsg'] == 'ok'
        assert len(r['department']) > 0

        for i in r['department']:
            if i['id'] != test_id:
                assert i['parentid'] % 10 == test_id
            else:
                assert i['id'] % 10 == test_id

    def test_department_update_1(self):
        """修改部门名称"""
        test_id = 14
        r = self.department.update(id=test_id, name='testupdate')
        assert r['errcode'] == 0
        assert r['errmsg'] == 'updated'

    def test_department_update_2(self):
        """修改父部门id"""
        test_id = 14
        r = self.department.update(id=test_id, parentid=5)
        assert r['errcode'] == 0
        assert r['errmsg'] == 'updated'

    def test_department_update_3(self):
        """修改order次序值"""
        test_id = 5
        r = self.department.update(id=test_id, order=100000001)
        assert r['errcode'] == 0
        assert r['errmsg'] == 'updated'

    def test_department_delete_1(self):
        """删除0成员一级子部门"""
        test_id = 14
        r = self.department.delete(id=test_id)
        assert r['errcode'] == 0
        assert r['errmsg'] == 'deleted'

    def test_department_delete_2(self):
        """删除0成员二级子部门"""
        test_id = 15
        r = self.department.delete(id=test_id)
        assert r['errcode'] == 0
        assert r['errmsg'] == 'deleted'

    def test_department_delete_3(self):
        """删除含有子部门的部门"""
        test_id = 3
        r = self.department.delete(id=test_id)
        assert r['errcode'] != 0
        assert 'department contains sub-department' in r['errmsg']

    def test_department_delete_4(self):
        """删除含有子成员的部门"""
        test_id = 5
        r = self.department.delete(id=test_id)
        assert r['errcode'] != 0
        assert 'department contains user' in r['errmsg']


