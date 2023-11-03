# Function Blueprint

def foo(a = 1, b = 2):
    return a + b


# x = foo - 1 # TypeError - unsupported operand type for -: 'function' and 'int'

x = foo() -1
print(type(foo))
print(type(foo()))