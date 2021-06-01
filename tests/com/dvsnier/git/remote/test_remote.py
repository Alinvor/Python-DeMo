# -*- coding:utf-8 -*-

from com.dvsnier.git.remote.remote import Remote
import unittest


class Test_Remote(unittest.TestCase):
    ''' the test remote '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Remote, self).setUp()

    def test_branch_prune(self):
        prune = Remote()
        prune.branch_prune()
        print "the test branch_prune is succeed."
        pass

    def tearDown(self):
        return super(Test_Remote, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
