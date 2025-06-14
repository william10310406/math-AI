import math

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
    original_b = b  # 保存原始的 b 值用於計算理論界限
    
    while b:
        print(f"步驟 {step}:")
        print(f"  a = {a}, b = {b}")
        print(f"  {a} = {b} × {a//b} + {a%b}")
        a, b = b, a % b
        step += 1
    
    theoretical_bound = 2 * math.log2(original_b) + 1
    print(f"最終結果: gcd = {a}")
    print(f"實際迭代次數: {step-1}")
    print(f"理論界限: 2log₂({original_b}) + 1 = {theoretical_bound:.2f}")
    print(f"是否滿足理論界限: {step-1 <= theoretical_bound}")
    return a

def main():
    # 基本歐幾里得算法示例
    print("歐幾里得算法示例：")
    # 使用斐波那契數列相鄰的數字，這會產生最壞的情況
    test_cases = [
        (48, 18),  # 基本測試
        (89, 55),  # 斐波那契數列相鄰數字
        (233, 144),  # 斐波那契數列相鄰數字
        (987, 610),  # 斐波那契數列相鄰數字
        (4181, 2584),  # 斐波那契數列相鄰數字
        (10946, 6765),  # 斐波那契數列相鄰數字
    ]
    
    for a, b in test_cases:
        result = gcd(a, b)
        print("-" * 40)

if __name__ == "__main__":
    main()
