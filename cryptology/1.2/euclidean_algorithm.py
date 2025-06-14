def gcd(a: int, b: int) -> int:
    """
    使用歐幾里得算法計算兩個數的最大公因數 (GCD)
    
    Args:
        a (int): 第一個正整數
        b (int): 第二個正整數
    
    Returns:
        int: a 和 b 的最大公因數
    """
    print(f"\n計算 gcd({a}, {b}) 的過程：")
    step = 1
    while b:
        print(f"步驟 {step}:")
        print(f"  a = {a}, b = {b}")
        print(f"  {a} = {b} × {a//b} + {a%b}")
        a, b = b, a % b
        step += 1
    print(f"最終結果: gcd = {a}")
    return a

def main():
    # 基本歐幾里得算法示例
    print("歐幾里得算法示例：")
    test_cases = [(48, 18), (54, 24), (7, 13)]
    
    for a, b in test_cases:
        result = gcd(a, b)
        print("-" * 40)

if __name__ == "__main__":
    main()
