# -*- coding:utf-8 -*-

import os
import pytest


class DB(object):
    ''' db '''
    def __init__(self):
        self.intransaction = []

    def begin(self, name):
        ''' begin '''
        print('\nDB::begin: {}'.format(name))
        self.intransaction.append(name)

    def rollback(self):
        ''' rollback '''
        item = self.intransaction.pop()
        print('\nDB::rollback: {}'.format(item))


@pytest.fixture(scope="module")
def db():
    ''' db '''
    return DB()


class TestClass(object):
    ''' TestClass '''
    @pytest.fixture(autouse=True)
    def transact(self, request, db):
        ''' transact '''
        db.begin(request.function.__name__)
        yield
        db.rollback()

    def test_method1(self, db):
        ''' test_method1 '''
        print('\nTestClass::test_method1: {}'.format(db))
        assert db.intransaction == ["test_method1"]

    def test_method2(self, db):
        ''' test_method2 '''
        print('\nTestClass::test_method2: {}'.format(db))
        assert db.intransaction == ["test_method2"]


if __name__ == "__main__":
    ''' the main point '''
    retcode = pytest.main(args=['-v', '-s', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--fixtures', os.path.abspath(__file__)])
    # retcode = pytest.main(args=['--collect-only', os.path.abspath(__file__)])
    print(retcode)
