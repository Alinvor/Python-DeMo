# -*- coding:utf-8 -*-

from com.dvsnier.git.pull.pull import Pull
import unittest


class Test_Pull(unittest.TestCase):
    ''' the test pull '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Pull, self).setUp()

    def test_fast_foward(self):
        pull = Pull()
        pull_fast_foward = pull.fast_foward()
        self.assertIsNotNone(pull_fast_foward, 'test_fast_foward is error.')
        print "the test fast_foward is succeed."
        pass

    def tearDown(self):
        return super(Test_Pull, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
