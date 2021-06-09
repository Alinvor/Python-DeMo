# -*- coding:utf-8 -*-

import unittest


class Test_Demo(unittest.TestCase):
    ''' the test demo '''

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')

    def setUp(self):
        super(Test_Demo, self).setUp()

    def _xxx(self):
        print("the test xxx is succeed.")
        pass

    def test_xxx(self):
        print("the test xxx is succeed.")
        pass

    def tearDown(self):
        super(Test_Demo, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Demo)
    unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
