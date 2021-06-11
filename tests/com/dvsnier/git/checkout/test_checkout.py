# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.git.branch.branch import Branch
from com.dvsnier.git.checkout.checkout import Checkout


class Test_Checkout(unittest.TestCase):
    ''' the test checkout '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._branch = Branch()
        cls._branch.set_current_branch_name(cls._branch.get_branch())

    def setUp(self):
        super(Test_Checkout, self).setUp()

    def test_branch_checkout(self):
        branch_checkout = Checkout()
        current_branch = Test_Checkout._branch.get_current_branch_name()
        logging.debug('the current branch name is {}'.format(current_branch))
        branch_checkout.branch_checkout(current_branch)
        # branch_checkout.branch_checkout(branch='anonym')
        # print("the test branch_checkout is succeed.")

    def tearDown(self):
        super(Test_Checkout, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Checkout)
    unittest.TextTestRunner(verbosity=2).run(suite)
