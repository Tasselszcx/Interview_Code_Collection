# ============================================================
# 21. 实现 pow(x, n)
# ============================================================
"""
题目描述：
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""
def my_pow_recursive(x, n):
    """
    方法：递归快速幂
    
    思路：
    1. 利用分治思想：x^n = x^(n/2) * x^(n/2)
    2. 处理奇偶性：奇数需要多乘一个x
    3. 处理负指数：x^(-n) = 1 / x^n
    
    优势：代码简洁，时间复杂度低
    劣势：递归栈空间O(log n)
    """
    if x == 0 and n < 0:
        return float('inf')

    if n < 0:
        x = 1 / x
        n = -n
    
    def fast_pow(x, n):
        # 递归终止条件
        if n == 0:
            return 1.0
        if n == 1:
            return x
        
        # 计算一半的幂
        half = fast_pow(x, n // 2)
        
        # 根据奇偶性返回结果
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
    
    return fast_pow(x, n)


def test_my_pow():
    """测试函数：验证幂运算算法"""
    test_cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (1.0, 100, 1.0),
        (0.0, 10, 0.0),
        (0.0, -1, float('inf')),  # 0的负指数是无穷大
        (1.0, -2147483648, 1.0),  # 边界情况
    ]
    
    print("pow(x, n) 测试结果:")
    print("=" * 50)
    
    for i, (x, n, expected) in enumerate(test_cases, 1):
        # 测试快速幂方法
        result1 = my_pow_recursive(x, n)
        
        # 对于浮点数，使用近似比较
        tolerance = 1e-9
        status1 = "✓ 通过" if abs(result1 - expected) < tolerance else "✗ 失败"
        
        print(f"  输入: {x}^{n}")
        print(f"  递归快速幂: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_my_pow()