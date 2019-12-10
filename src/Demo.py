# -- coding:utf-8 --

if __name__ == "__main__":
    # print "\n"
    print "-" * 10 + '>'
    name = raw_input("What\'s your name?\n")
    print("Hello %s" % name)
    print "." * 10
    raw_input("按任意键结束")
    print("." * 3 + "系统执行 %s,此时我要 %s.\n" % ('结束', '退出'))
