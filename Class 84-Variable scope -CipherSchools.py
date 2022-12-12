#scope
x=20
def func():
    global x
    x = 22
    return x
print(x)
print(func())
print(x)