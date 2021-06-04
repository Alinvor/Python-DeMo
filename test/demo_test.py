# -*- coding:utf-8 -*-

import unittest


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

    def test_demo(self):
        cmd_str = "the total time spent executing the current command({command}) is {cmd} s.\n"
        content_str = "the execution result is ['{content}']."
        msg = (cmd_str + content_str).format(command="命令",
                                             cmd="cmds",
                                             content="content")
        print msg
        print "the test demo is succeed."
        pass

    def tearDown(self):
        return super(Test_Demo, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
