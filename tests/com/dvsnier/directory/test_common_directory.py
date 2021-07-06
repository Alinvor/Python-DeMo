# -*- coding:utf-8 -*-

import unittest

from com.dvsnier.directory.common_directory import CommonDirectory


class Test_Common_Directory(unittest.TestCase):
    ''' the test common dir '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls.directory = CommonDirectory()

    def setUp(self):
        super(Test_Common_Directory, self).setUp()

    def test_generate_complex_file_name(self):
        'the test generate complex file name'
        dir_name = 'https'
        file_name = 'test_name'
        output = self.directory.generate_complex_file_name(dir_name, file_name)
        print("\nthe test generate_complex_file_name(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_generate_complex_file_name is error.')

    def test_generate_fmt_file_name(self):
        'the test generate fmt file name'
        dir_name = 'https'
        file_name = 'test_name'
        # output = generate_fmt_file_name(dir_name, file_name)
        output = self.directory.generate_fmt_file_name(dir_name, file_name, fmt='%Y%m%d_%H%M%S.%f')
        print("\nthe test generate_fmt_file_name(%s) is succeed." % output)
        self.assertIsNotNone(output, 'generate_fmt_file_name is error.')

    def test_generate_file_name(self):
        'the test generate file name'
        dir_name = 'https'
        file_name = 'test_name'
        output = self.directory.generate_file_name(dir_name, file_name)
        print("\nthe test test_generate_file_name(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_generate_file_name is error.')

    def test_generate_file_name_only(self):
        'the test generate file name only'
        dir_name = 'out/https_2'
        file_name = 'test_name'
        output = self.directory.generate_file_name_only(dir_name, file_name)
        print("\nthe test test_generate_file_name_only(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_generate_file_name_only is error.')

    def test_generate_complex_or_fmt_file_name(self):
        'the test generate complex or fmt file name'
        dir_name = 'https'
        # file_name = ''
        # file_name = ' '
        # file_name = 'test_name'
        # file_name = ' test_name'
        # file_name = 'test_name '
        # file_name = ' test_name '
        file_name = 'test_name.txt'
        # file_name = 'test_name.txt.log'
        # file_name = '.test_name.txt.log'
        # file_name = '.test_name.txt.log.'
        # file_name = 'test.name.txt.log'
        output = self.directory.generate_complex_or_fmt_file_name(dir_name, file_name)
        print("\nthe test test_generate_complex_or_fmt_file_name(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_generate_complex_or_fmt_file_name is error.')

    def test_mk_dir(self):
        'the test mk dir'
        dir_name = 'config'
        output = self.directory.mk_dir(dir_name)
        print("\nthe test test_mk_dir(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_mk_dir is error.')

    def test_mk_output_dir(self):
        'the test mk output dir'
        dir_name = 'https'
        output = self.directory.mk_output_dir(dir_name)
        print("\nthe test mk_output_dir(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_mk_output_dir is error.')

    def test_mk_children_dir(self):
        'the test mk childer dir'
        sub_name = 'children'
        output = self.directory.mk_children_dir('out/http', sub_dir_name=sub_name)
        print("\nthe test mk_children_dir(%s) is succeed." % output)
        self.assertIsNotNone(output, 'test_mk_children_dir is error.')

    def tearDown(self):
        super(Test_Common_Directory, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Common_Directory)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
