import json
from test.case.basecase import BaseCase

class TestGrantCouponToUser(BaseCase):
    def test_grant_coupon_to_user_normal(self):
        case_data = self.get_case_data('test_grant_coupon_to_user_normal')
        res = self.send_request(case_data)
        self.assertTrue(res.json()['result']['ifSuccess'])   # 断言
        #self.assertFalse(res.json()['result']['ifSuccess'])

    def test_grant_coupon_to_user_wrong(self):
        """ Level1: 券池异常"""   #Level1及是一个标签，放在docstring哪里都可以
        case_data = self.get_case_data('test_grant_coupon_to_user_wrong')
        res = self.send_request(case_data)
        self.assertDictEqual(res.json(), json.loads(case_data['expect_res']))   # 断言


