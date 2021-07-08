# -*- coding:utf-8 -*-

# import tracemalloc
import unittest

from com.dvsnier.process.execute import execute, trace


class Test_Execute(unittest.TestCase):
    ''' the test execute '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')

    def setUp(self):
        super(Test_Execute, self).setUp()

    def test_execute(self):
        'the test execute'
        # self.debug_trace_malloc_start()
        # cmds = ["git config --local --list"]
        # cmds = ["git config --local --list", "grep \"user\""]
        cmds = ["git config --local --list", "grep \"user\"", "grep \"@\""]
        result = execute(cmds, quiet=False)
        self.assertIsNotNone(result, 'test_execute is error.')
        # self.debug_trace_malloc_end()

    def test_trace(self):
        'the test trace'
        # self.debug_trace_malloc_start()
        # cmds = ["git config --local --list"]
        # cmds = ["git config --local --list", "grep \"user\""]
        cmds = ["git config --local --list", "grep \"user\"", "grep \"@\""]
        trace(cmds)
        # self.debug_trace_malloc_end()

    # def debug_trace_malloc_start(self):
    #     tracemalloc.start()

    # def debug_trace_malloc_end(self):
    #     snapshot = tracemalloc.take_snapshot()
    #     top_stats = snapshot.statistics('lineno')
    #     print("[ Top 10 ]")
    #     for stat in top_stats[:10]:
    #         print(stat)

    def tearDown(self):
        super(Test_Execute, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Execute)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
