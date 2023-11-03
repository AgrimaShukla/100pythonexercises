# TypeError

'''def foo(a, b):
    print(a + b)

x = foo(2 + 3) * 10 '''# TypeError - cannot multiply none type object with integer
# instead write return rather than print

def foo(a, b):
    return a + b

x = foo(2, 3) * 10
print(x)


