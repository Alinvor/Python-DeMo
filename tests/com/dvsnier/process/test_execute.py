# -*- coding:utf-8 -*-

import unittest

from com.dvsnier.process.execute import execute, trace


class Test_Execute(unittest.TestCase):
    ''' the test execute '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Execute, self).setUp()

    def test_execute(self):
        'the test execute'
        # cmds = ["git config --local --list"]
        # cmds = ["git config --local --list", "grep \"user\""]
        cmds = ["git config --local --list", "grep \"user\"", "grep \"@\""]
        result = execute(cmds, quiet=False)
        self.assertIsNotNone(result, 'test_execute is error.')
        print(result)

    def test_trace(self):
        'the test trace'
        # cmds = ["git config --local --list"]
        # cmds = ["git config --local --list", "grep \"user\""]
        cmds = ["git config --local --list", "grep \"user\"", "grep \"@\""]
        trace(cmds)

    def tearDown(self):
        return super(Test_Execute, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
