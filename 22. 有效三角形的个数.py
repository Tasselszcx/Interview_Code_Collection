# ============================================================
# 22. 有效三角形的个数
# ============================================================
"""
题目描述：
给定一个包含非负整数的数组，统计其中可以组成三角形三条边的三元组个数。
"""
def triangle_number_two_pointers(nums):
    """
    方法：排序 + 双指针
    
    思路：
    1. 对数组排序，便于使用三角形不等式
    2. 固定最长边（从大到小遍历）
    3. 使用双指针在剩余数组中寻找满足条件的两边
    
    优势：时间复杂度O(n²)，可以处理较大规模数据
    劣势：需要修改原数组（排序）
    """
    if not nums or len(nums) < 3:
        return 0
    
    nums.sort()  # 排序是双指针法的前提
    count = 0
    n = len(nums)
    
    # 从最大的数开始，固定为最长边
    for i in range(n - 1, 1, -1):
        left, right = 0, i - 1
        
        while left < right:
            # 三角形条件：两边之和大于第三边
            if nums[left] + nums[right] > nums[i]:
                # 所有left到right-1的数都能与right和i组成三角形
                count += right - left
                # 减小right继续搜索
                right -= 1
            else:
                # 两边之和小于等于第三边时，增大left
                left += 1
    
    return count

def test_triangle_number():
    """测试函数：验证有效三角形个数算法"""
    test_cases = [
        ([2, 2, 3, 4, 5, 6], 3),      # [2,3,4], [2,3,4], [2,2,3]
        ([4, 2, 3, 4], 4),      # 额外多一个[2,3,4]
        ([1, 1, 3, 4], 0),      # 无法组成三角形
        ([0, 0, 0], 0),         # 零不能作为边长
        ([1, 2, 3], 0),         # 不满足三角形条件
        ([], 0),                # 空数组
        ([1, 2], 0)             # 元素不足
    ]
    
    print("有效三角形的个数测试结果:")
    print("=" * 50)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result1 = triangle_number_two_pointers(nums.copy())
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        
        print(f"  输入数组: {nums}")
        print(f"  双指针法: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_triangle_number()