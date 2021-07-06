# -*- coding:utf-8 -*-

import os
import unittest

from com.dvsnier.directory.abstract_directory import AbstractDirectory


class Test_AbstrctDirectory(unittest.TestCase):
    ''' the test xxx '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls.directory = AbstractDirectory(strategy_mode=True)
        # cls.directory = AbstractDirectory()

    def setUp(self):
        super(Test_AbstrctDirectory, self).setUp()

    def test_0_mk_dir(self):
        self.directory.set_work_region_space(os.path.join(os.getcwd(), 'out'))
        self.directory.mk_dir('output/asc_0')

    def test_1_mk_children_dir(self):
        # the current executed environment directory
        self.directory.mk_children_dir(output_dir_name='out', sub_dir_name='sub_1/asc_1')
        # the settings work region space environment directory
        self.directory.mk_children_dir(output_dir_name=self.directory.get_work_region_space(),
                                       sub_dir_name='sub_2/asc_12')
        # the settings executed region space environment directory
        self.directory.mk_children_dir(output_dir_name=self.directory.get_executed_region_space(),
                                       sub_dir_name='sub_3/asc_123')
        # the settings current region space environment directory
        self.directory.mk_children_dir(output_dir_name=self.directory.get_current_region_space(),
                                       sub_dir_name='sub_4/asc_1234')

    def test_2_mk_output_dir(self):
        self.directory.mk_output_dir(output_dir_name=self.directory.get_work_region_space())
        self.directory.mk_output_dir(output_dir_name=self.directory.get_work_region_space(),
                                     output_default_super_dir_name='dist')

    def tearDown(self):
        super(Test_AbstrctDirectory, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_AbstrctDirectory)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
