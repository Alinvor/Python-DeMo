# -*- coding:utf-8 -*-

import os
import unittest

from com.dvsnier.email.config.config import Config


class Test_Config(unittest.TestCase):
    ''' the test config '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls.config = Config()

    def setUp(self):
        super(Test_Config, self).setUp()

    def test_obtain_config(self):
        cwd = os.getcwd()
        self.assertIsNotNone(cwd, 'test_obtain_config is error.')
        cfg_file = os.path.join(cwd, '/conf/email_config.test.cfg') # error path
        cfg_file = os.path.join(cwd, 'conf/email_config.test.cfg') # ok path
        self.assertIsNotNone(cfg_file, 'test_obtain_config is error.')
        config = Test_Config.config.obtain_config(cfg_file)
        self.assertIsNotNone(config, 'test_obtain_config is error.')
        # print(config['project-prefix'])
        print(config['version_info'])


    def tearDown(self):
        super(Test_Config, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Config)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
