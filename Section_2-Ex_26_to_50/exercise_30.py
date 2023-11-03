# Arguments

'''def foo(a = 2, b):
    return a + b ''' # SyntaxError - non-default arguments follows default argument

def foo(b, a = 2):
    return a + b

print(foo(3))