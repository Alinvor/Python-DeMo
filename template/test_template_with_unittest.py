# -*- coding:utf-8 -*-

# import logging
import unittest

# from com.dvsnier.config.journal.common_config import config


class Test_XXX(unittest.TestCase):
    ''' the test xxx '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        # kwargs = {'output_dir_name': 'log', 'file_name': 'config', 'level': logging.DEBUG}
        # cls._logging = config(kwargs)

    def setUp(self):
        super(Test_XXX, self).setUp()

    def test_xxx(self):
        print("the test xxx(test_template.py) is succeed.")
        pass

    def tearDown(self):
        super(Test_XXX, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    ''' the unittest suite '''
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_XXX)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
