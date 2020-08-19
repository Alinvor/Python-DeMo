# -*- coding:utf-8 -*-

import unittest
import os


class Test_Demo(unittest.TestCase):
    ''' the test demo '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Demo, self).setUp()

    def _xxx(self):
        print "the test xxx is succeed."
        pass

    def test_xxx(self):
        # cwd == ./
        # cwd = os.getcwd()

        file = os.path.abspath("./readMe.md")
        # file_1 = os.path.abspath(".")
        # file_2 = os.path.abspath("./../")
        # file_3 = os.path.abspath("./../readMe.md")
        if os.path.exists(file):
            if os.path.isfile(file):
                print "the current is file(%s)" % file
        print "the test xxx is succeed."
        pass

    def tearDown(self):
        return super(Test_Demo, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
