# -*- coding:utf-8 -*-

import unittest


class Test_XXX(unittest.TestCase):
    ''' the test xxx '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_XXX, self).setUp()

    def test_xxx(self):
        print ("the test xxx is succeed.")
        pass

    def tearDown(self):
        return super(Test_XXX, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
