# ============================================================
# 7. 最大子数组和 - 动态规划解法
# ============================================================
def max_subarray_sum(nums):
    """
    最大子数组和 - 动态规划解法（Kadane算法）
    
    核心思路：
    对于每个位置i，我们要决定：
    - 是把当前元素加入前面的子数组？
    - 还是从当前元素重新开始？
    
    状态定义：
    dp[i] = 以nums[i]结尾的最大子数组和
    
    状态转移方程：
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    
    解释：
    - nums[i]: 从当前位置重新开始
    - dp[i-1] + nums[i]: 将当前元素加入前面的子数组
    
    可视化理解（nums = [-2,1,-3,4,-1,2,1,-5,4]）：
    索引:  0   1   2   3   4   5   6   7   8
    值:   -2   1  -3   4  -1   2   1  -5   4
    dp:   -2   1  -2   4   3   5   6   1   5
    
    解释：
    - dp[0] = -2 (只有-2)
    - dp[1] = max(1, -2+1) = 1 (从1重新开始更好)
    - dp[2] = max(-3, 1-3) = -2 (都不好，选较大的)
    - dp[3] = max(4, -2+4) = 4 (从4重新开始更好)
    - dp[4] = max(-1, 4-1) = 3 (加入前面的子数组)
    - dp[5] = max(2, 3+2) = 5 (加入前面的子数组)
    - dp[6] = max(1, 5+1) = 6 (加入前面的子数组) ← 最大值
    
    时间复杂度：O(n)
    空间复杂度：O(1) - 可以只用一个变量
    
    参数：
        nums: 整数数组
    返回：
        最大子数组和
    """
    if not nums:
        return 0
    
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(current_sum, max_sum)
    
    return max_sum

# ============================================================
# 测试函数
# ============================================================
def test_max_subarray_sum():
    """测试最大子数组和函数"""
    print("=" * 70)
    print("最大子数组和 - 测试")
    print("=" * 70)
    
    # 测试用例1：经典示例
    print("\n测试用例1：经典示例")
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"输入: {nums1}")
    result1 = max_subarray_sum(nums1)
    print(f"最大子数组和: {result1}")
    print(f"预期: 6")
    
    # 测试用例2：全是正数
    print("\n测试用例2：全是正数")
    nums2 = [1, 2, 3, 4, 5]
    print(f"输入: {nums2}")
    result2 = max_subarray_sum(nums2)
    print(f"最大子数组和: {result2}")
    print(f"预期: 15 (所有元素的和)")
    
    # 测试用例3：全是负数
    print("\n测试用例3：全是负数")
    nums3 = [-5, -2, -8, -1, -4]
    print(f"输入: {nums3}")
    result3 = max_subarray_sum(nums3)
    print(f"最大子数组和: {result3}")
    print(f"预期: -1 (最大的单个元素)")
    
    # 测试用例4：只有一个元素
    print("\n测试用例4：只有一个元素")
    nums4 = [5]
    print(f"输入: {nums4}")
    result4 = max_subarray_sum(nums4)
    print(f"最大子数组和: {result4}")
    print(f"预期: 5")
    
    # 测试用例5：正负交替
    print("\n测试用例5：正负交替")
    nums5 = [5, -3, 5]
    print(f"输入: {nums5}")
    result5 = max_subarray_sum(nums5)
    print(f"最大子数组和: {result5}")
    print(f"预期: 7 (整个数组)")
    
    # 测试用例6：大的负数在中间
    print("\n测试用例6：大的负数在中间")
    nums6 = [8, -19, 5, -4, 20]
    print(f"输入: {nums6}")
    result6 = max_subarray_sum(nums6)
    print(f"最大子数组和: {result6}")
    print(f"预期: 21")

if __name__ == "__main__":
    test_max_subarray_sum()