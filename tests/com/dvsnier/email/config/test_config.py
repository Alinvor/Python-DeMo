# -*- coding:utf-8 -*-

import logging
import os
import unittest

from com.dvsnier.config.common_conf import logging_conf
from com.dvsnier.email.config.config import Config


class Test_Config(unittest.TestCase):
    ''' the test config '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        kwargs = {'output_dir_name': 'email', 'file_name': 'email'}
        logging_conf(kwargs)
        cls.config = Config()
        cls.cfg = {}

    def setUp(self):
        super(Test_Config, self).setUp()

    def test_0_obtain_config(self):
        cwd = os.getcwd()
        self.assertIsNotNone(cwd, 'test_0_obtain_config is error.')
        # cfg_file = os.path.join(cwd, '/conf/email_config.test.cfg') # error path
        # cfg_file = os.path.join(cwd, 'conf/email_config.test.cfg') # ok path
        cfg_file = 'conf/email_config.test.cfg' # ok path
        self.assertIsNotNone(cfg_file, 'test_0_obtain_config is error.')
        self.cfg = Test_Config.config.obtain_config(cfg_file)
        self.assertIsNotNone(self.cfg, 'test_0_obtain_config is error.')
        # print(self.cfg['project-prefix'])
        # print(self.cfg['version_info'])
        # print(config['home'])
        # print(self.cfg)

    def test_1_get_mail_host(self):
        value = self.config.get_mail_host()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_2_get_mail_port(self):
        value = self.config.get_mail_port()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_3_get_mail_user(self):
        value = self.config.get_mail_user()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_4_get_mail_pass(self):
        value = self.config.get_mail_pass()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_5_get_mail_sender(self):
        value = self.config.get_mail_sender()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_6_get_sender_alias(self):
        value = self.config.get_sender_alias()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_7_get_mail_receiver(self):
        value = self.config.get_mail_receiver()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_8_get_receiver_alias(self):
        value = self.config.get_receiver_alias()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

    def test_9_get_config(self):
        value = self.config.get_config()
        logging.debug('the value is {}.'.format(value))
        self.assertIsNotNone(value)

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
