# -- coding:utf-8 --
# python 3.7.4 version


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
    ''' 3.x 广度优先: D -> C -> A '''
    # 此处有点反直觉, 3.x 的应该是做了兼容为新式类型，
    #       D -> C -> A
    # 我在我得机器上是:
    #       D -> B -> A
    #       深度优先 -> called A.foo()
    d = D()
    d.foo()
