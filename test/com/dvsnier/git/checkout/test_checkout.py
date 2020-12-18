# -*- coding:utf-8 -*-

from com.dvsnier.git.checkout.checkout import Checkout
import unittest


class Test_Checkout(unittest.TestCase):
    ''' the test checkout '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Checkout, self).setUp()

    def test_branch_checkout(self):
        branch_checkout = Checkout()
        branch_checkout.branch_checkout()
        # branch_checkout.branch_checkout(branch='anonym')
        print "the test branch_checkout is succeed."
        pass

    def tearDown(self):
        return super(Test_Checkout, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
