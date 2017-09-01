def func2(a):
    print "func2"

def func(a, *b, **c):
    print "a:", a
    print "b:", b
    print "c:", c
    print func.func_name, func.func_dict
    func2(a)

func.__setattr__("test", 111)
func.test2 = 222
func("111", "222")
