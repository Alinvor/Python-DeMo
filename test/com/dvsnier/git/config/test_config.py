# -*- coding:utf-8 -*-

from com.dvsnier.git.config.config import Config
import unittest


class Test_Config(unittest.TestCase):
    ''' the test xxx '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Config, self).setUp()

    def test_global_info(self):
        config = Config()
        info = config.global_info()
        self.assertIsNotNone(info, 'test_global_info is error.')
        print(info)
        print "the test global info is succeed."
        pass

    def test_local_info(self):
        config = Config()
        info = config.local_info()
        self.assertIsNotNone(info, 'test_local_info is error.')
        print(info)
        print "the test local info is succeed."
        pass

    def tearDown(self):
        return super(Test_Config, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
