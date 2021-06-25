# -*- coding:utf-8 -*-

import logging
import time
import unittest

from com.dvsnier.config.common_conf import logging_conf
from com.dvsnier.email.email import Email


class Test_Email(unittest.TestCase):
    ''' the test email '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        kwargs = {'output_dir_name': 'email', 'file_name': 'email'}
        logging_conf(kwargs)
        cls._email = Email()
        cls._switch_ssl = False
        # cls._switch_ssl = True

    def setUp(self):
        super(Test_Email, self).setUp()

    def test_0_config_file(self):
        if self._switch_ssl:
            self._email.config_file('conf/email_ssl_config.test.cfg')
        else:
            self._email.config_file('conf/email_config.test.cfg')

    def test_1_get_config_info(self):
        cfg_info = self._email.get_config_info()
        self.assertIsNotNone(cfg_info)
        logging.info(cfg_info)
        # print(cfg_info)

    def test_2_init(self):
        if self._switch_ssl:
            # smtp ssl
            self._email.init(True)
        else:
            # the default smtp
            self._email.init()

    def test_3_builderText(self):
        timestamps = time.strftime("%Y-%m-%d %H:%M:%S",
                                   time.localtime(time.time()))
        content = '''
                     您好，我是测试用例发来的邮件测试({0})...
                  '''.format(timestamps)
        self._email.builderText('测试 Python 邮件 {0} '.format(timestamps),
                                content)

    def test_4_sendmail(self):
        self._email.sendmail()
        # pass

    def test_5_quit(self):
        self._email.quit()

    def tearDown(self):
        super(Test_Email, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Email)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
