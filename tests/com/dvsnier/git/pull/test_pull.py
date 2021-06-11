# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.git.git import Git
from com.dvsnier.git.pull.pull import Pull


class Test_Pull(unittest.TestCase):
    ''' the test pull '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._git = Git()
        cls._git.config()
        cls._pull = Pull()

    def setUp(self):
        super(Test_Pull, self).setUp()

    def test_fast_foward(self):
        pull_fast_foward = Test_Pull._pull.fast_foward()
        self.assertIsNotNone(pull_fast_foward, 'test_fast_foward is error.')
        logging.debug(pull_fast_foward)
        # print("the test fast_foward is succeed.")

    def tearDown(self):
        super(Test_Pull, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Pull)
    unittest.TextTestRunner(verbosity=2).run(suite)
