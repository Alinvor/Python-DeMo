# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.config.journal.common_config import config


class Test_Common_Config(unittest.TestCase):
    ''' the test common config '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')

    def setUp(self):
        super(Test_Common_Config, self).setUp()

    def test_config(self):
        'the test config'
        # kwargs = {'output_dir_name': ' ', 'file_name': ' '}
        # kwargs = {'output_dir_name': 'log', 'file_name': ' '}
        # kwargs = {'output_dir_name': ' ', 'file_name': 'log'}
        kwargs = {'output_dir_name': 'log', 'file_name': 'log'}
        # CRITICAL = 50
        # FATAL = CRITICAL
        # ERROR = 40
        # WARNING = 30
        # WARN = WARNING
        # INFO = 20
        # DEBUG = 10
        # NOTSET = 0
        # kwargs = {'output_dir_name': 'log', 'file_name': 'log', 'level': logging.ERROR}
        # kwargs = {'output_dir_name': 'log', 'file_name': 'log', 'level': logging.INFO}
        # kwargs = {'output_dir_name': 'log', 'file_name': 'log', 'level': logging.DEBUG}
        config(kwargs)
        logging.critical("the test config is succeed.")
        logging.error("the test config is succeed.")
        logging.warning("the test config is succeed.")
        logging.info("the test config is succeed.")
        logging.debug("the test config is succeed.")
        pass

    def tearDown(self):
        super(Test_Common_Config, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Common_Config)
    unittest.TextTestRunner(verbosity=2).run(suite)
