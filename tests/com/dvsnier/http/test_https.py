# -*- coding:utf-8 -*-

import unittest
from com.dvsnier.http.https import Request


def test_two():
    # the origin request object, then test case two
    # _request = Request(url)
    # _request.requests()
    pass


class Test_Https(unittest.TestCase):
    ''' the test https '''
    @classmethod
    def setUpClass(cls):
        print("...the set up...")
        print

    def setUp(self):
        return super(Test_Https, self).setUp()

    def test_requests_one(self):
        'the test requests one'
        # url = 'http://www.xuexi.la/sudu/523441.html'
        _request = Request()
        self.assertIsNotNone(_request, 'test_requests_one is error.')
        self.assertIsNone(_request.requests())

    def test_requests_two(self):
        'the test requests two'
        url = 'http://www.xuexi.la/sudu/523441.html'
        _request = Request(url)
        self.assertIsNotNone(_request, 'test_requests_two is error')
        response = _request.requests()
        self.assertIsNotNone(response, 'test_requests_two is error.')

    def test_requests_three(self):
        'the test requests three'
        url = 'http://www.xuexi.la/sudu/523441.html'
        _request = Request()
        self.assertIsNotNone(_request, 'test_requests_three is error')
        response = _request.requests(url)
        self.assertIsNotNone(_request.getUrl(),
                             'test_requests_three is error.')
        self.assertIsNotNone(response, 'test_requests_three is error.')

    def test_getUrl(self):
        'the test get url'
        url = 'http://www.xuexi.la/sudu/523441.html'
        _request = Request(url)
        self.assertIsNotNone(_request.getUrl(), 'test_getUrl is error.')
        _request = Request()
        self.assertTupleEqual(_request.getUrl(), (), 'test_getUrl is error.')

    def tearDown(self):
        return super(Test_Https, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        print
        print("...the tear down...")


if __name__ == '__main__':
    unittest.main()
