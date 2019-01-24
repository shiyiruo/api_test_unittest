import unittest
import sys
sys.path.append('../..')
from test.case.user.test_grant_coupon_to_user import *

smoke_suite = unittest.TestSuite()
smoke_suite.addTests([TestGrantCouponToUser('test_grant_coupon_to_user_normal')])

def get_suite(suite_name):
    return globals().get(suite_name)