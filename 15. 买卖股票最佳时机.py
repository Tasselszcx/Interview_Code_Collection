# ============================================================
# 15. 买卖股票最佳时机
# ============================================================
"""
题目描述：
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择某一天买入，并在未来的某一个不同的日子卖出，计算你所能获取的最大利润。
如果不能获取任何利润，返回 0。

核心思路：
1. 一次遍历：记录历史最低价，计算当前价格卖出的最大利润
2. 动态规划：dp[i]表示第i天卖出的最大利润

复杂度分析：
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
def max_profit_one_pass(prices):
    """
    一次遍历法（最优解）
    
    思路：
    1. 记录历史最低价格
    2. 遍历每天的价格，计算如果在历史最低点买入，当天卖出的利润
    3. 更新最大利润
    
    优势：时间复杂度O(n)，空间复杂度O(1)
    """
    # 特殊情况简化
    if not prices or len(prices) < 2:
        return 0
    
    min_price = float('inf')  # 历史最低价格
    max_profit = 0            # 最大利润
    
    for price in prices:
        # 更新历史最低价
        if price < min_price:
            min_price = price
        # 计算当前卖出的利润，更新最大利润
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit

def test_max_profit():
    """测试函数：验证股票买卖算法"""
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),   # 在第2天买入，第5天卖出
        ([7, 6, 4, 3, 1], 0),      # 无法获得利润
        ([1, 2], 1),               # 简单情况
        ([2, 1], 0),               # 价格递减
        ([3, 2, 6, 5, 0, 3], 4),   # 复杂情况
        ([], 0),                   # 空数组
        ([1], 0)                   # 单元素数组
    ]
    
    print("买卖股票最佳时机测试结果:")
    print("=" * 50)
    
    for i, (prices, expected) in enumerate(test_cases, 1):
        result1 = max_profit_one_pass(prices)
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        
        print(f"  价格序列: {prices}")
        print(f"  一次遍历法: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_max_profit()
