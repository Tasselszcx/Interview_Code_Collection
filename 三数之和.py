# ============================================================
# 5. 三数之和
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
