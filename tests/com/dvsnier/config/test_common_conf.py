# -*- coding:utf-8 -*-

import unittest

from com.dvsnier.config.common_conf import logging_conf


class Test_Common_Conf(unittest.TestCase):
    ''' the test common conf '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')

    def setUp(self):
        super(Test_Common_Conf, self).setUp()

    def test_logging_conf(self):
        'the test logging conf'
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
        # kwargs = {'output_dir_name': 'log', 'file_name': 'log', 'level': logging.DEBUG}
        # kwargs = {'output_dir_name': 'log', 'file_name': 'log', 'level': logging.ERROR}
        # kwargs = {'output_dir_name': 'log', 'file_name': 'log', 'level': logging.INFO}
        logging_conf(kwargs)
        # logging.critical("the test test_logging_conf is succeed.")
        # logging.error("the test test_logging_conf is succeed.")
        # logging.warning("the test test_logging_conf is succeed.")
        # logging.info("the test test_logging_conf is succeed.")
        # logging.debug("the test test_logging_conf is succeed.")
        pass

    def tearDown(self):
        super(Test_Common_Conf, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Common_Conf)
    unittest.TextTestRunner(verbosity=2).run(suite)
