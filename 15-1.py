out = set()
for a in range(1, 1000):
    flag = 1
    for x in range(1, 1000):
        if ((x % a == 0) or (x % 28 != 0) or (x % 49 != 0)) == 0:
            flag = 0
    if flag == 1:
        print(a)
        out.add(a)
print(max(out))
