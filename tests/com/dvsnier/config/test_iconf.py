# -*- coding:utf-8 -*-

import unittest


class Test_IConf(unittest.TestCase):
    ''' the test iconf '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')

    def setUp(self):
        super(Test_IConf, self).setUp()

    def test_0_iconf(self):
        print("the test xxx(test_iconf.py) is succeed.")
        pass

    def tearDown(self):
        super(Test_IConf, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_IConf)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
