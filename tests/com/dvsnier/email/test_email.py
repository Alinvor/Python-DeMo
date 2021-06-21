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
        ...

    def test_3_builderText(self):
        ...

    def test_4_sendmail(self):
        ...

    def test_5_quit(self):
        ...

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
