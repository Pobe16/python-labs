def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b


x = 19
y = 29
x,y = swap(x, y)

#x, y = y, x
print("x = ", x)
print("y = ", y)
