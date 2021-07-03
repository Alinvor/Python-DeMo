# -*- coding:utf-8 -*-

import json
import unittest

import logging

from com.dvsnier.config.cfg.configuration import Configuration
from com.dvsnier.config.journal.common_config import config


class Test_Configuration(unittest.TestCase):
    ''' the test configuration '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._config = Configuration()
        kwargs = {'output_dir_name': 'log', 'file_name': 'config', 'level': logging.DEBUG}
        cls._logging = config(kwargs)

    def setUp(self):
        super(Test_Configuration, self).setUp()

    def test_0_configuration(self):
        cfg = self._config.obtain_config('./conf/config.test.cfg')
        self.assertIsNotNone(cfg, 'test_0_configuration is error.')
        logging.warning(json.dumps(cfg, indent=4))
        logging.debug('the current key({}): value({})'.format('version_info', cfg['version_info']))

    def tearDown(self):
        super(Test_Configuration, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Configuration)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()