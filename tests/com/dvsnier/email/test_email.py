# -*- coding:utf-8 -*-

import logging
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

    def setUp(self):
        super(Test_Email, self).setUp()

    def test_0_config_file(self):
        self._email.config_file('conf/email_config.test.cfg')

    def test_1_get_config_info(self):
        cfg_info = self._email.get_config_info()
        self.assertIsNotNone(cfg_info)
        logging.info(cfg_info)
        # print(cfg_info)

    def test_2_init(self):
        # smtp ssl
        self._email.init(True)
        # the default smtp
        # self._email.init()
        logging.debug('开始初始化...')

    def test_3_builderText(self):
        logging.debug('开始构建邮件文本...')
        self._email.builderText('测试 Python 邮件', '您好，我是测试用例发来的邮件测试...')
        logging.debug('构建邮件文本完成...')

    def test_4_sendmail(self):
        self._email.sendmail()
        logging.debug('开始发送邮件...')

    def test_5_quit(self):
        self._email.quit()
        logging.debug('完成发送邮件, 状态完成...')

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
