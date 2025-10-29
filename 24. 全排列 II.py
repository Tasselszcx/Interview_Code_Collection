# ============================================================
# 24. 全排列 II
# ============================================================
"""
题目描述：
给定一个可包含重复数字的序列，返回所有不重复的全排列。
"""

def permute_unique_backtrack(nums):
    """
    方法一：回溯法 + 剪枝（最优解）
    
    思路：
    1. 先对数组排序，便于去重
    2. 使用回溯法生成所有排列
    3. 剪枝条件：当前元素与前一个元素相同且前一个元素未被使用
    
    优势：能够有效处理重复元素
    劣势：需要排序和额外的used数组
    """
    def backtrack(path, used):
        # 找到一个完整排列
        if len(path) == len(nums):
            result.append(path[:])
            return
        
        for i in range(len(nums)):
            # 跳过已使用元素
            if used[i]:
                continue
            
            # 相比于全排列，多加一步剪枝：当前元素与前一个相同，且前一个未被使用
            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue
            
            # 做选择
            used[i] = True
            path.append(nums[i])
            
            # 递归
            backtrack(path, used)
            
            # 撤销选择
            path.pop()
            used[i] = False
    
    nums.sort()  # 排序是去重的前提
    result = []
    used = [False] * len(nums)
    backtrack([], used)
    return result

def test_permute_unique():
    """测试函数：验证全排列II算法"""
    test_cases = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
        ([], [[]])
    ]
    
    print("全排列 II 测试结果:")
    print("=" * 50)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result1 = permute_unique_backtrack(nums.copy())
        
        # 标准化结果比较（排序每个排列和整个结果列表）
        def normalize_result(res):
            return sorted([tuple(perm) for perm in res])
        
        normalized_result1 = normalize_result(result1)
        normalized_expected = normalize_result(expected)
        
        status1 = "✓ 通过" if normalized_result1 == normalized_expected else "✗ 失败"
        
        print(f"  输入数组: {nums}")
        print(f"  回溯法结果数量: {len(result1)}")
        print(f"  预期结果数量: {len(expected)}")
        
        # 显示前几个结果（避免输出过多）
        if result1:
            print(f"  回溯法前3个结果: {result1[:3]}{'...' if len(result1) > 3 else ''}")
        print()


if __name__ == "__main__":
    test_permute_unique()