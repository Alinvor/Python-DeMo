# -*- coding:utf-8 -*-

import unittest
from com.dvsnier.conf.common_conf import logging_conf


class Test_Common_Conf(unittest.TestCase):
    ''' the test common conf '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Common_Conf, self).setUp()

    def test_logging_conf(self):
        'the test logging conf'
        # kwargs = {'output_dir_name': ' ', 'file_name': ' '}
        # kwargs = {'output_dir_name': 'request', 'file_name': ' '}
        # kwargs = {'output_dir_name': ' ', 'file_name': 'request'}
        kwargs = {'output_dir_name': 'request', 'file_name': 'request'}
        logging_conf(kwargs)
        print "the test test_logging_conf is succeed."
        pass

    def tearDown(self):
        return super(Test_Common_Conf, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
