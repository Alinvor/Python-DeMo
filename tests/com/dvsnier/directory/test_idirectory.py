# -*- coding:utf-8 -*-

import os
import unittest

# from com.dvsnier.config.journal.common_config import
from com.dvsnier.directory.idirectory import IDirectory


class Test_IDirectory(unittest.TestCase):
    ''' the test IDirectory '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        # kwargs = {'output_dir_name': 'log', 'file_name': 'config', 'level': logging.DEBUG}
        # cls._logging = config(kwargs)
        cls.directory = IDirectory()

    def setUp(self):
        super(Test_IDirectory, self).setUp()

    def test_0_set_work_region_space(self):
        self.assertIsNotNone(self.directory.set_work_region_space(os.getcwd()),
                             'test_0_set_work_region_space is error.')

    def test_1_get_work_region_space(self):
        self.assertIsNotNone(self.directory.get_work_region_space(), 'test_1_get_work_region_space is error.')

    def test_3_set_current_region_space(self):
        self.assertIsNotNone(self.directory.set_work_region_space(os.getcwd()),
                             'test_3_set_current_region_space is error.')

    def test_2_get_current_region_space(self):
        self.assertIsNotNone(self.directory.get_current_region_space(), 'test_2_get_current_region_space is error.')

    def test_5_set_executed_region_space(self):
        self.assertIsNotNone(self.directory.set_executed_region_space(os.getcwd()),
                             'test_5_set_executed_region_space is error.')

    def test_4_get_executed_region_space(self):
        self.assertIsNotNone(self.directory.get_executed_region_space(), 'test_4_get_executed_region_space is error.')

    def tearDown(self):
        super(Test_IDirectory, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_IDirectory)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
