# -*- coding:utf-8 -*-

import unittest

from com.dvsnier.git.git import Git
from com.dvsnier.git.remote.remote import Remote


class Test_Remote(unittest.TestCase):
    ''' the test remote '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._git = Git()
        cls._git.config()
        cls._prune = Remote()

    def setUp(self):
        return super(Test_Remote, self).setUp()

    def test_branch_prune(self):
        Test_Remote._prune.branch_prune()
        # print("the test branch_prune is succeed.")

    def tearDown(self):
        return super(Test_Remote, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Remote)
    unittest.TextTestRunner(verbosity=2).run(suite)
