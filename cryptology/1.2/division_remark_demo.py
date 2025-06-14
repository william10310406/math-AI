def division_remark_demo(a, b):
    print(f"a = {a}, b = {b}")
    real_div = a / b
    q = int(real_div)
    r = a - b * q
    print(f"a / b = {real_div}")
    print(f"q = int(a / b) = {q}")
    print(f"r = a - b * q = {r}")
    print(f"Python a // b = {a // b}, a % b = {a % b}")
    print(f"餘數是否一致: {r == a % b}")
    print('-' * 40)

# 測試案例
cases = [
    (123, 17),
    (100, 33),
    (89, 55),
    (233, 144),
    (987, 610),
]
for a, b in cases:
    division_remark_demo(a, b) 