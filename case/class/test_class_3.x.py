# -- coding:utf-8 --
# python 3.7.4 version


class A(object):
    def foo(self):
        print('深度优先 -> called A.foo()')


class B(A, object):
    pass


class C(A, object):
    def foo(self):
        print('广度优先 -> called C.foo()')


class D(B, C, object):
    pass


if __name__ == '__main__':
    ''' 3.x 广度优先: D -> C -> A '''
    d = D()
    d.foo()
