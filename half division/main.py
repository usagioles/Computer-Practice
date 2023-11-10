import math

def f(x):
    return math.cosh(x) - x/4

a = 1.8
b = 2
e = 0.001
k = 0

print("a =", a)
print("b =", b)
print("e =", e)

if f(a) * f(b) < 0:
    print("Умова виконана")
    while True:
        x = (a + b) / 2.0
        k += 1
        if abs(f(x)) < e:
            break
        if f(a) * f(x) < 0:
            a = a
            b = x
        else:
            a = x
            b = b

    print("Корінь x =", x)
    print("К-сть ітерацій k =", k)
else:
    print("Умова не виконана")
