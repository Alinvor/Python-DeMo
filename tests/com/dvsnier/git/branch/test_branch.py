# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.config.journal.common_config import config
from com.dvsnier.git.branch.branch import Branch
from com.dvsnier.git.git import Git


class Test_Branch(unittest.TestCase):
    ''' the test branch '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        kwargs = {'output_dir_name': 'git', 'file_name': 'log', 'level': logging.DEBUG}
        config(kwargs)
        cls._git = Git()
        cls._git.config()
        cls._branch = Branch()

    def setUp(self):
        super(Test_Branch, self).setUp()

    def test_0_get_branch(self):
        branch_name = self._branch.get_branch()
        logging.info('the current branch name is {}'.format(branch_name))
        self.assertIsNotNone(branch_name, 'test_0_get_branch is error.')
        # print("the test get_branch is succeed.")

    def test_1_branch_to_file_and_commit_list(self):
        branch_commit_list = self._branch.branch_to_file_and_commit_list()
        logging.info(branch_commit_list)
        self.assertIsNotNone(branch_commit_list, 'test_0_branch_to_file_and_commit_list is error.')
        # print("the test branch_to_file_and_commit_list is succeed.")

    def test_2_branch_to_file_and_commit_list_with_more(self):
        branch_commit_list_more = self._branch.branch_to_file_and_commit_list_with_more()
        logging.info(branch_commit_list_more)
        self.assertIsNotNone(branch_commit_list_more, 'test_0_branch_to_file_and_commit_list_with_more is error.')
        # print("the test branch_to_file_and_commit_list_with_more is succeed.")

    def test_3_branch_set_upstream_to(self):
        branch_name = self._branch.get_branch()
        # branch_name = None
        # branch_name = ''
        # branch_name = ' '
        # branch_name = '0'
        branch_set_upstream_to = self._branch.branch_set_upstream_to(branch_name)
        if branch_set_upstream_to:
            logging.info(branch_set_upstream_to)
        self.assertIsNotNone(branch_set_upstream_to, 'test_3_branch_set_upstream_to is error.')

    def test_5_get_current_branch_name(self):
        # branch_name = self._branch.get_branch()
        # branch_name = None
        # branch_name = ''
        # branch_name = ' '
        # branch_name = '0'
        current_branch_name = self._branch.get_current_branch_name()
        if current_branch_name:
            logging.info('the current branch name is {0}.'.format(current_branch_name))
        self.assertIsNotNone(current_branch_name, 'test_5_get_current_branch_name is error.')

    def test_4_set_current_branch_name(self):
        branch_name = self._branch.get_branch()
        # branch_name = None
        # branch_name = ''
        # branch_name = ' '
        # branch_name = '0'
        self._branch.set_current_branch_name(branch_name)

    def test_get_current_branch_list(self):
        branch_list = self._branch.get_current_branch_list()
        self.assertIsNotNone(branch_list, 'test_get_current_branch_list is error.')
        logging.info(branch_list)

    def test_get_remote_branch_list(self):
        branch_list = self._branch.get_remote_branch_list()
        self.assertIsNotNone(branch_list, 'test_get_remote_branch_list is error.')
        logging.info(branch_list)

    def test_get_remote_prune(self):
        prune_result = self._branch.get_remote_prune()
        self.assertIsNotNone(prune_result, 'test_get_remote_prune is error.')
        logging.info(prune_result)

    def test_has_remote(self):
        hasRemote = self._branch.has_remote()
        self.assertTrue(hasRemote, 'test_has_remote is error.')
        logging.info(hasRemote)

    def test_has_specifical_branch(self):
        value = self._branch.has_specifical_branch('master', is_remote=True)
        self.assertTrue(value, 'test_has_specifical_branch is error.')
        logging.info(value)

    def tearDown(self):
        super(Test_Branch, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Branch)
    unittest.TextTestRunner(verbosity=2).run(suite)
