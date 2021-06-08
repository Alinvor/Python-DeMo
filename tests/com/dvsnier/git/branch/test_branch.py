# -*- coding:utf-8 -*-

import logging
import unittest

from com.dvsnier.git.branch.branch import Branch
from com.dvsnier.git.git import Git


class Test_Branch(unittest.TestCase):
    ''' the test branch '''

    _git = None

    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print('')
        cls._git = Git()
        cls._git.config()

    def setUp(self):
        super(Test_Branch, self).setUp()

    def test_get_branch(self):
        branch = Branch()
        branch_name = branch.get_branch()
        logging.info(branch_name)
        self.assertIsNotNone(branch_name, 'test_get_branch is error.')
        print("the test get_branch is succeed.")

    def test_branch_to_file_and_commit_list(self):
        branch = Branch()
        branch_commit_list = branch.branch_to_file_and_commit_list()
        logging.info(branch_commit_list)
        self.assertIsNotNone(branch_commit_list,
                             'test_branch_to_file_and_commit_list is error.')
        print("the test branch_to_file_and_commit_list is succeed.")

    def test_branch_to_file_and_commit_list_with_more(self):
        branch = Branch()
        branch_commit_list_more = branch.branch_to_file_and_commit_list_with_more()
        logging.info(branch_commit_list_more)
        self.assertIsNotNone(
            branch_commit_list_more,
            'test_branch_to_file_and_commit_list_with_more is error.')
        print("the test branch_to_file_and_commit_list_with_more is succeed.")

    def tearDown(self):
        super(Test_Branch, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print('')
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
