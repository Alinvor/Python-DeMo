# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.git.config.config import Config
from com.dvsnier.git.git import Git


class Test_Config(unittest.TestCase):
    ''' the test xxx '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._git = Git()
        cls._git.config()
        cls._config = Config()

    def setUp(self):
        super(Test_Config, self).setUp()
        logging.debug('the start setUp item tests.')

    def test_0_global_info(self):
        info = Test_Config._config.global_info()
        self.assertIsNotNone(info, 'test_0_global_info is error.')
        logging.debug(info)
        # print(info)
        # print("the test global info is succeed.")

    def test_1_local_info(self):
        info = Test_Config._config.local_info()
        self.assertIsNotNone(info, 'test_1_local_info is error.')
        logging.debug(info)
        # print(info)
        # print("the test local info is succeed.")

    def tearDown(self):
        super(Test_Config, self).tearDown()
        logging.debug('the end tearDown item tests.')

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Config)
    unittest.TextTestRunner(verbosity=2).run(suite)
