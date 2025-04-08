def max_of_four(a, b, c, d):
    if a >= b and a >= c and a >= d:
        return a
    elif b >= a and b >= c and b >= d:
        return b
    elif c >= a and c >= b and c >= d:
        return c
    else:
        return d

x = int(input())
y = int(input())
z = int(input())
w = int(input())

print(max_of_four(x, y, z, w))