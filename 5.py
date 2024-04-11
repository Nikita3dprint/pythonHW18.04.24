out = set()
for n in range(1, 200):
    b = bin(n)[2:]
    if n % 2 == 0:
        b = b + '01'
    else:
        b = '1' + b + '1'
    r = int(b, 2)
    if r > 156:
        out.add(n)
print(min(out))
