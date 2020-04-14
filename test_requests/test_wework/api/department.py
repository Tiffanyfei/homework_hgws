import requests

from test_requests.test_wework.api.wework import WeWork


class Department(WeWork):
    """
    部门管理
    """
    secret = "G1bKCaizwcnHww7K4RfHEVpYMnzdSa141jGujwQcU1g"

    def create(self, name='', parentid=1, **kwargs):
        """
        创建部门
        """
        data = {'name': name, 'parentid': parentid}
        data.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json=data
        )
        self.format(r)
        return r.json()

    def list(self, **kwargs):
        """获取部门列表"""
        params={'access_token': self.get_token(self.secret)}
        params.update(kwargs)
        url='https://qyapi.weixin.qq.com/cgi-bin/department/list'
        r=requests.get(url=url,params=params)
        self.format(r)
        return r.json()

    def update(self,id:int,**kwargs):
        """修改部门"""
        data = {'id': id}
        data.update(kwargs)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/update'
        r = requests.post(
            url,
            params={'access_token': self.get_token(self.secret)},
            json=data
        )
        self.format(r)
        return r.json()

    def delete(self,id:int):
        """删除部门"""
        params = {'access_token': self.get_token(self.secret),'id':id}
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        r = requests.get(url=url, params=params)
        self.format(r)
        return r.json()
