def euclidean_steps(a: int, b: int):
    """
    執行歐幾里得演算法並回傳每一步的餘數序列 r_i
    """
    r = [a, b]
    while r[-1] != 0:
        r.append(r[-2] % r[-1])
    return r

def verify_case1(r):
    """
    驗證每一組 (r_i, r_{i+1}, r_{i+2}) 是否滿足 Case I 的條件，並美化輸出
    """
    print("\nCase I 驗證 (r_{i+1} <= 1/2 r_i ⇒ r_{i+2} < r_{i+1} <= 1/2 r_i)")
    print("{:>3}  {:>10}  {:>10}  {:>10}  {:>15}  {:>15}".format('i', 'r_i', 'r_(i+1)', 'r_(i+2)', 'r_(i+1) <= 1/2 r_i', 'r_(i+2) < r_(i+1)'))
    print("-" * 70)
    for i in range(len(r) - 2):
        ri, ri1, ri2 = r[i], r[i+1], r[i+2]
        cond1 = ri1 <= 0.5 * ri
        cond2 = ri2 < ri1
        if cond1:
            print("{:>3}  {:>10}  {:>10}  {:>10}  {:>15}  {:>15}".format(
                i, ri, ri1, ri2, '✔' if cond1 else '', '✔' if cond2 else ''))
    print()

def main():
    # 可以自行更換 a, b 來測試
    test_cases = [
        (48, 18),
        (89, 55),
        (233, 144),
        (987, 610),
        (4181, 2584),
        (10946, 6765),
        (100000, 12345),
    ]
    for a, b in test_cases:
        print("="*60)
        print(f"測試 gcd({a}, {b}) 的餘數序列:")
        r = euclidean_steps(a, b)
        print("r_i 序列:", r)
        verify_case1(r)
    print("="*60)

if __name__ == "__main__":
    main() 