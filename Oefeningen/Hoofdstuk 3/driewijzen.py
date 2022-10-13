t = round(float(input()), 2)
a = b = c = 0.01
flag = False
while a < t/3:
    if flag:
        break
    b = a
    while b <= t/2:
        c = round(t - a - b, 2)
        if round(a*b*c, 6) == round(a+b+c, 6) == round(t, 6) and a <= b <= c:
            print(f'${a:.2f} + ${b:.2f} + ${c:.2f} = ${a:.2f} x ${b:.2f} x ${c:.2f} = ${t:.2f}')
            flag = True
        b = round(b + 0.01, 2)
    a = round(a + 0.01, 2)
