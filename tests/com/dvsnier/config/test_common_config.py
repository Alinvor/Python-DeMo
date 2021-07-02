# -*- coding:utf-8 -*-

import unittest
from com.dvsnier.directory.common_dir import generate_file_name_only, mk_dir


class Test_Common_Config(unittest.TestCase):
    ''' the test common conf '''

    _Conf = None
    test_config_dir = None
    file_name = None

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        self._Conf = Conf()
        self.test_config_dir = mk_dir('conf')
        self.file_name = generate_file_name_only(self.test_config_dir, 'test_config.cfg')
        return super(Test_Common_Config, self).setUp()

    def test_conf(self):
        'the test conf'
        self.assertIsNotNone(self._Conf, 'test_conf is error.')

    def test_conf_1_write(self):
        'the test conf write'
        self._Conf.set('test_conf_write', 'test1', 'test1')
        self._Conf.set('test_conf_write', 'test2', 'test2')
        self._Conf.write(self.file_name)
        print("the test test_conf_1_write is succeed.")
        # self.debug()

    def test_conf_2_read(self):
        'the test conf read'
        self._Conf.read(self.file_name)
        self.assertIsNotNone(self._Conf.sections(), 'test_conf_2_read is error.')
        print("the test test_conf_2_read is succeed.")
        # self.debug()

    def test_conf_3_add_section(self):
        'the test conf add section'
        #
        # 测试用例不是按照代码从上往下有序执行，而是指令重排列(字母表)
        #
        self._Conf.add_section('test_conf_add_section')
        self._Conf.set('test_conf_add_section', 'test1', '1')
        self._Conf.set('test_conf_add_section', 'test2', '2')
        self._Conf.write(self.file_name)
        self.assertIsNotNone(self._Conf.sections(), 'test_conf_3_add_section is error.')
        print("the test test_conf_3_add_section is succeed.")
        # self.debug()

    def test_conf_4_remove_section(self):
        'the test conf remove section'
        self._Conf.add_section('test_conf_remove_section')
        self._Conf.remove_section('test_conf_remove_section')
        self._Conf.write(self.file_name)
        self.assertIsNotNone(self._Conf.sections(), 'test_conf_4_remove_section is error.')
        print("the test test_conf_4_remove_section is succeed.")
        # self.debug()

    def test_conf_5_sections(self):
        'the test conf sections'
        self._Conf.read(self.file_name)
        # self._Conf.set('test_conf_write', 'test1', 'test1')
        # self._Conf.set('test_conf_write', 'test2', 'test2')
        self.assertIsNotNone(self._Conf.sections(), 'test_conf_5_sections is error.')
        print("the test test_conf_5_sections is succeed.")
        # self.debug()

    def test_conf_6_options(self):
        'the test conf options'
        self._Conf.read(self.file_name)
        self._Conf.set('test_conf_add_section', 'test1', 'test1')
        self.assertIsNotNone(self._Conf.options('test_conf_add_section'), 'test_conf_6_options is error.')
        print("the test test_conf_6_options is succeed.")
        # self.debug()

    def test_conf_7_get(self):
        'the test conf options that get value'
        self._Conf.read(self.file_name)
        self._Conf.set('test_conf_get', 'test1', 'test1')
        self.assertIsNotNone(self._Conf.get('test_conf_get', 'test1'), 'test_conf_7_get is error.')
        print("the test test_conf_7_get is succeed.")
        # self.debug()

    def test_conf_8_getboolean(self):
        'the test conf options that get boolean value'
        self._Conf.read(self.file_name)
        self._Conf.set('test_conf_getboolean', 'test0', 'getboolean')
        self._Conf.set('test_conf_getboolean', 'test1', 'true')
        self._Conf.set('test_conf_getboolean', 'test2', 'True')
        self._Conf.set('test_conf_getboolean', 'test3', '0')
        self._Conf.set('test_conf_getboolean', 'test4', '1')
        self._Conf.set('test_conf_getboolean', 'test5', 'false')
        self._Conf.set('test_conf_getboolean', 'test6', 'False')
        self.assertTrue(self._Conf.getboolean('test_conf_getboolean', 'test1'), 'test_conf_8_getboolean is error.')
        self.assertTrue(self._Conf.getboolean('test_conf_getboolean', 'test2'), 'test_conf_8_getboolean is error.')
        self.assertFalse(self._Conf.getboolean('test_conf_getboolean', 'test3'), 'test_conf_8_getboolean is error.')
        self.assertTrue(self._Conf.getboolean('test_conf_getboolean', 'test4'), 'test_conf_8_getboolean is error.')
        self.assertFalse(self._Conf.getboolean('test_conf_getboolean', 'test5'), 'test_conf_8_getboolean is error.')
        self.assertFalse(self._Conf.getboolean('test_conf_getboolean', 'test6'), 'test_conf_8_getboolean is error.')
        self.assertIsNotNone(self._Conf.getboolean('test_conf_getboolean', 'test1'), 'test_conf_8_getboolean is error.')
        print("the test test_conf_8_getboolean is succeed.")
        # self.debug()

    def test_conf_9_getfloat(self):
        'the test conf options that get float value'
        self._Conf.read(self.file_name)
        self._Conf.set('test_conf_getfloat', 'test0', 'getfloat')
        self._Conf.set('test_conf_getfloat', 'test1', '0')
        self._Conf.set('test_conf_getfloat', 'test2', '1')
        self._Conf.set('test_conf_getfloat', 'test3', '2')
        self._Conf.set('test_conf_getfloat', 'test4', '3.0')
        self._Conf.set('test_conf_getfloat', 'test5', '-1')
        self._Conf.set('test_conf_getfloat', 'test6', '-1.2')
        self.assertIsNotNone(self._Conf.getfloat('test_conf_getfloat', 'test1'), 'test_conf_9_getfloat is error.')
        print("the test test_conf_9_getfloat is succeed.")
        # self.debug()

    def test_conf_10_getint(self):
        'the test conf options that get int value'
        self._Conf.read(self.file_name)
        self._Conf.set('test_conf_getint', 'test0', 'getint')
        self._Conf.set('test_conf_getint', 'test1', '0')
        self._Conf.set('test_conf_getint', 'test2', '1')
        self._Conf.set('test_conf_getint', 'test3', '2')
        self._Conf.set('test_conf_getint', 'test4', '3.0')
        self._Conf.set('test_conf_getint', 'test5', '-1')
        self._Conf.set('test_conf_getint', 'test6', '-1.2')
        self.assertIsNotNone(self._Conf.getint('test_conf_getint', 'test1'), 'test_conf_10_getint is error.')
        print("the test test_conf_10_getint is succeed.")
        # self.debug()

    def debug(self):
        'the debug mode'
        for section_element in self._Conf.sections():
            options = self._Conf.options(section_element)
            for option_element in options:
                print('\noption: %s, key: %s, value: %s' %
                      (section_element, option_element, self._Conf.get(section_element, option_element)))
            # else:
            #     print('\noption: %s, key: %s, value: %s' %
            #           (section_element, 'None', 'None'))

    def tearDown(self):
        return super(Test_Common_Config, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Common_Config)
    unittest.TextTestRunner(verbosity=2).run(suite)
