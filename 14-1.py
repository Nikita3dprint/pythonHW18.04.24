x = 3 * 5103 ** 2020 + 3 * 729 ** 2021 - 2 * 242 ** 2022 + 27 **2023 - 4 * 7 ** 2024 - 2029
k = 0
while x > 0:
    if x % 27 > 9:
        k += 1
    x = x // 27
print(k)
