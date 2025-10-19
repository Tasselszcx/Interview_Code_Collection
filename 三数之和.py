# ============================================================
# 5. 三数之和 - 排序 + 双指针
# ============================================================
def three_sum(nums):
    """
    三数之和 - 找出所有和为0的不重复三元组
    
    核心思路：排序 + 双指针
    
    算法流程：
    1. 先对数组排序，方便去重和使用双指针
    2. 固定第一个数 nums[i]，问题转化为：在剩余数组中找两个数，使得和为 -nums[i]
    3. 使用双指针在 [i+1, len-1] 范围内查找两数之和
    4. 如果 sum < 0，左指针右移；如果 sum > 0，右指针左移
    5. 如果 sum == 0，记录结果，并移动指针跳过重复元素
    
    去重策略：
    - 对于第一个数：如果 nums[i] == nums[i-1]，跳过
    - 对于第二、三个数：找到答案后，移动指针时跳过相同的数
    
    时间复杂度：O(n²) - 外层循环O(n)，内层双指针O(n)
    空间复杂度：O(1) - 不计返回结果的空间
    
    参数：
        nums: 整数数组
    返回：
        所有和为0的不重复三元组列表
    """

    # 结果列表
    result = []
    
    # 边界检查：数组长度小于3，无法组成三元组
    if not nums or len(nums) < 3:
        return result
    
    # 第一步：排序数组，时间复杂度 O(nlogn)
    # 排序的好处：
    # 1. 可以使用双指针
    # 2. 方便跳过重复元素
    # 3. 如果 nums[i] > 0，后面的数都大于0，和不可能为0
    nums.sort()
    
    # 第二步：遍历数组，固定第一个数
    for i in range(len(nums)):
        # 优化1：如果当前数字大于0，后面的数都大于0，不可能和为0
        if nums[i] > 0:
            break
        
        # 优化2：去重 - 如果当前数字和前一个相同，跳过
        # i > 0 确保不会越界
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # 第三步：使用双指针在剩余数组中找两数之和 = -nums[i]
        # left指向i的下一个位置，right指向数组末尾
        left = i + 1
        right = len(nums) - 1
        
        # 目标值：需要找到两个数，使得它们的和等于target
        target = -nums[i]
        
        # 双指针遍历
        while left < right:
            # 计算当前两数之和
            current_sum = nums[left] + nums[right]
            
            # 情况1：和小于目标值，需要更大的数，左指针右移
            if current_sum < target:
                left += 1
            
            # 情况2：和大于目标值，需要更小的数，右指针左移
            elif current_sum > target:
                right -= 1
            
            # 情况3：找到一组解
            else:
                # 记录这组三元组
                result.append([nums[i], nums[left], nums[right]])
                
                # 去重：跳过所有重复的左指针值
                # 例如：[-2, 0, 0, 2, 2]，找到 [-2,0,2] 后
                # 需要跳过后面的0和2
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # 去重：跳过所有重复的右指针值
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # 同时移动两个指针，继续查找下一组解
                left += 1
                right -= 1
    
    return result


def test_three_sum():
    """测试三数之和函数"""
    print("=" * 70)
    print("三数之和 - 测试")
    print("=" * 70)
    
    # 测试用例1：基本情况
    print("\n测试用例1：基本情况")
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"输入: {nums1}")
    result1 = three_sum(nums1)
    print(f"输出: {result1}")
    print(f"预期: [[-1, -1, 2], [-1, 0, 1]]")
    
    # 测试用例2：空数组
    print("\n测试用例2：空数组")
    nums2 = []
    print(f"输入: {nums2}")
    result2 = three_sum(nums2)
    print(f"输出: {result2}")
    print(f"预期: []")
    
    # 测试用例3：无解
    print("\n测试用例3：无解")
    nums3 = [1, 2, 3]
    print(f"输入: {nums3}")
    result3 = three_sum(nums3)
    print(f"输出: {result3}")
    print(f"预期: []")
    
    # 测试用例4：全是0
    print("\n测试用例4：全是0")
    nums4 = [0, 0, 0, 0]
    print(f"输入: {nums4}")
    result4 = three_sum(nums4)
    print(f"输出: {result4}")
    print(f"预期: [[0, 0, 0]]")
    
    # 测试用例5：有重复元素
    print("\n测试用例5：有重复元素")
    nums5 = [-2, 0, 0, 2, 2]
    print(f"输入: {nums5}")
    result5 = three_sum(nums5)
    print(f"输出: {result5}")
    print(f"预期: [[-2, 0, 2]]")
    
    # 测试用例6：较大数组
    print("\n测试用例6：较大数组")
    nums6 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    print(f"输入: {nums6}")
    result6 = three_sum(nums6)
    print(f"输出: {result6}")

if __name__ == "__main__":
    test_three_sum()
