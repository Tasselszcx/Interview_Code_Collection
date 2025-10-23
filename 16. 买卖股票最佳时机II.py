# ============================================================
# 16. 买卖股票最佳时机
# ============================================================
"""
买卖股票的最佳时机 II

题目描述：
给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候最多只能持有一股股票。
你也可以先购买，然后在同一天出售。计算你所能获取的最大利润。

核心思路：
1. 贪心算法：只要今天价格比昨天高，就进行交易
2. 动态规划：dp[i][0]表示第i天不持有股票的最大利润，dp[i][1]表示第i天持有股票的最大利润

复杂度分析：
- 时间复杂度：O(n)
- 空间复杂度：O(1) - 优化后的动态规划
"""

def max_profit_greedy(prices):
    """
    贪心算法（最优解）
    
    思路：
    1. 只要今天的价格比昨天高，就进行交易（昨天买入，今天卖出）
    2. 累计所有正收益
    
    优势：代码简单，时间复杂度低
    """
    if not prices or len(prices) < 2:
        return 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
        
    return max_profit

def test_max_profit_ii():
    """测试函数：验证多次买卖股票算法"""
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7),   # 多次交易：1买5卖，3买6卖
        ([1, 2, 3, 4, 5], 4),      # 连续上涨：1买5卖 或 多次交易
        ([7, 6, 4, 3, 1], 0),      # 价格递减，无法获利
        ([1], 0),                   # 单元素数组
        ([], 0),                    # 空数组
        ([2, 1, 2, 0, 1], 2)       # 复杂情况
    ]
    
    print("买卖股票最佳时机 II 测试结果:")
    print("=" * 50)
    
    for i, (prices, expected) in enumerate(test_cases, 1):
        result1 = max_profit_greedy(prices)
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        
        print(f"  价格序列: {prices}")
        print(f"  贪心算法: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_max_profit_ii()