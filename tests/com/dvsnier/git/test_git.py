# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.git.git import Git

class Test_Git(unittest.TestCase):
    ''' the test git '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._git = Git()
        cls._git.config()

    def setUp(self):
        super(Test_Git, self).setUp()

    def test_config(self):
        ''' the test config
            note:
                    1. the currently, only one process instance log object is supported.
                    2. the following consideration is to support multi process and multi instance log objects
        '''
        self.assertIsNotNone(Test_Git._git, 'test_config is error.')
        # Test_Git._git.config(output_dir_name='test_git')
        # Test_Git._git.config(file_name='record')
        # Test_Git._git.config(output_dir_name='test_git', file_name='record')
        logging.warn('the test config is succeed.')
        print("the test config is succeed.")

    def tearDown(self):
        super(Test_Git, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Git)
    unittest.TextTestRunner(verbosity=2).run(suite)
