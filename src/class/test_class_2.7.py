# -- coding:utf-8 --
# python 2.7.16 version


class A:
    def foo(self):
        print('深度优先 -> called A.foo()')


class B(A):
    pass


class C(A):
    def foo(self):
        print('广度优先 -> called C.foo()')


class D(B, C):
    pass


if __name__ == '__main__':
    ''' 深度优先: D -> B -> A '''
    d = D()
    d.foo()
