# ============================================================
# 20. 打家劫舍 II
# ============================================================
"""
题目描述：
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""
def rob_circular_detailed(nums):
    """
    方法：详细动态规划
    
    思路：
    1. 分别处理包含第一个房屋和不包含第一个房屋的情况
    2. 使用两个dp数组分别记录两种情况的最高金额
    3. 最终取两种情况的最大值
    """

    if not nums:
        return 0
    
    n = len(nums)
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    # 情况1：偷第一个房屋，不能偷最后一个
    dp1 = [0] * (n - 1)
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
    
    # 情况2：不偷第一个房屋，可以偷最后一个
    
    dp2 = [0] * n
    dp2[1] = nums[1]
    dp2[2] = max(nums[1], nums[2])

    for i in range(3, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
    
    # 返回情况1和情况2的大值，相当于分类讨论
    return max(dp1[-1], dp2[-1])

def test_rob_circular():
    """测试函数：验证环形打家劫舍算法"""
    test_cases = [
        ([2, 3, 2], 3),           # 不能同时偷第一个和最后一个
        ([1, 2, 3, 1], 4),        # 偷第一个和第三个
        ([0], 0),                  # 只有一个房屋
        ([1, 2], 2),               # 两个房屋，偷金额大的
        ([1, 3, 1, 3, 100], 103),  # 复杂情况
        ([], 0)                    # 空数组
    ]
    
    print("打家劫舍 II 测试结果:")
    print("=" * 50)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result1 = rob_circular_detailed(nums)
        
        print(f"  房屋金额: {nums}")
        print(f"  详细DP法: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_rob_circular()
        