# -*- coding:utf-8 -*-

import abc
import pytest

class Base_ABC():

    __metaclass__ = abc.ABCMeta # python 2.x
    '''
        the ABC class

        多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
        在面向对象方法中一般是这样表述多态性：

            向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，即执行不同的函数。
    '''
    def __init__(self):
        super(Base_ABC, self).__init__()

    @abc.abstractmethod
    def onCallback(self):
        'the abstract oncallback method'
        # raise AttributeError('the subclasses need to be implemented.')
        raise NotImplementedError('the subclasses need to be implemented.')

class D(Base_ABC):

    def __init__(self):
        super(D, self).__init__()

    def onCallback(self):
        print('class D onCallback method')
        pass


class E(Base_ABC):

    def __init__(self):
        super(E, self).__init__()

    def onCallback(self):
        print('class E onCallback method')
        pass

@pytest.fixture()
def method_abc():
    'the method abc'
    return Base_ABC()

@pytest.fixture()
def method_d():
    'the method d'
    return D()

@pytest.fixture()
def method_e():
    'the method e'
    return E()

def test_needsfiles(tmpdir):
    'the test temp files'
    print(tmpdir)

def test_inherit(method_abc):
    'the test inherit'
    # with pytest.raises(Exception) as e:
    #     pass
    try:
        method_abc.onCallback()
    except TypeError as e:
        pass

def test_inherit_with_d(method_d):
    'the test inherit with d'
    method_d.onCallback()

def test_inherit_with_e(method_e):
    'the test inherit with e'
    method_e.onCallback()
