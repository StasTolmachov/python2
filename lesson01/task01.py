n = 65432

res = 0

while n > 0:
    x = n % 10
    res = res + x
    n = n // 10

print(res)