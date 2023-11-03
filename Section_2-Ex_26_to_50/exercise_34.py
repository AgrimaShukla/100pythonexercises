# LOcal vs Global Variables

'''def foo():
    c = 1
    return c

foo()
print(c)''' # c is not defined

def foo():
    global c
    c = 1
    return c

foo()
print(c)