# -*- coding:utf-8 -*-

from com.dvsnier.git.git import Git
import logging
import unittest


class Test_Git(unittest.TestCase):
    ''' the test git '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Git, self).setUp()

    def test_config(self):
        git = Git()
        self.assertIsNotNone(git, 'test_config is error.')
        git.config()
        # git.config(output_dir_name='test_git')
        # git.config(file_name='record')
        # git.config(output_dir_name='test_git', file_name='record')
        logging.warn('the test config is succeed.')
        print "the test config is succeed."
        pass

    def tearDown(self):
        return super(Test_Git, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
