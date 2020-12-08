# -- coding:utf-8 --

from sys import argv

# arg_name, one, two, three = argv
arg_name = argv

if __name__ == "__main__":
    ''' 主程序-函数入口 '''
    place_holder = '%s %r'
    # print "\n"
    print "-" * 10 + '>'
    name = raw_input("What\'s your name?\n")
    # print 'arg_name: %r, %s, %s, %s' % (arg_name, one, two, three)
    print 'arg_name: %r' % (arg_name)
    # 注意print 后面',' 的高级表达方式
    print "->",
    # print("Hello %s" % name)
    # print(place_holder % ("Hello", name))
    print(place_holder % ("Hello", name)),
    print "<-"
    print "." * 10
    raw_input("按任意键结束")
    print("." * 3 + "系统执行 %s,此时我要 %s.\n" % ('结束', '退出'))
