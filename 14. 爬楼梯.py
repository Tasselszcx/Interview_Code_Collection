# ============================================================
# 14. 爬楼梯
# ============================================================
"""
题目描述：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶？

核心思路：
1. 动态规划：dp[i] = dp[i-1] + dp[i-2]
2. 公式法：直接使用斐波那契数列通项公式

复杂度分析：
- 时间复杂度：O(n) - 动态规划，O(log n) - 矩阵快速幂
- 空间复杂度：O(1) - 优化后的动态规划
"""

def climb_stairs_dp(n):
    """
    方法一：动态规划（最优解）
    
    思路：
    1. 到达第i阶的方法数 = 到达第i-1阶的方法数 + 到达第i-2阶的方法数
    2. 基础情况：dp[0]=1, dp[1]=1
    
    优势：思路清晰，代码简单
    劣势：时间复杂度O(n)
    """

    if n <= 1:
        return 1
    
    # 空间优化，只保存前两个状态
    step1, step2 = 1, 1 # 初始化, step1代表0楼, step2代表1楼
    for i in range(2, n + 1):
        curr = step1 + step2
        step1 = step2
        step2 = curr
    return step2

def climb_stairs_formula(n):
    """
    方法二：通项公式法（Binet公式）
    
    思路：
    使用斐波那契数列的通项公式直接计算
    
    优势：时间复杂度O(1)
    劣势：存在浮点数精度问题，不适用于大数
    """
    import math
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2  # 黄金比例
    psi = (1 - sqrt5) / 2
    
    # 使用斐波那契数列通项公式
    return int((phi**(n + 1) - psi**(n + 1)) / sqrt5)

def test_climb_stairs():
    """测试函数：验证爬楼梯算法"""
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
        (0, 1)
    ]
    
    print("爬楼梯测试结果:")
    print("=" * 50)
    
    for i, (n, expected) in enumerate(test_cases, 1):
        result1 = climb_stairs_dp(n)
        result2 = climb_stairs_formula(n)
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        status2 = "✓ 通过" if result2 == expected else "✗ 失败"
        
        # print(f"测试用例 {i}: {status1} | {status2}")
        print(f"  台阶数: {n}")
        print(f"  动态规划: {result1}")
        print(f"  通项公式: {result2}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_climb_stairs()