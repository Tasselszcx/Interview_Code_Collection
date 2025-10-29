# ============================================================
# 23. 全排列
# ============================================================
"""
题目描述：
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""
def permute_backtrack(nums):
    """
    方法：回溯算法
    
    思路：
    1. 使用回溯法生成所有排列
    2. 使用used数组标记已使用元素
    3. 当路径长度等于数组长度时，保存结果
    
    优势：逻辑清晰，易于理解
    劣势：需要used数组记录状态
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
            
            # 做选择
            used[i] = True
            path.append(nums[i])
            
            # 递归探索
            backtrack(path, used)
            
            # 撤销选择
            path.pop()
            used[i] = False
    
    result = []
    used = [False] * len(nums)
    backtrack([], used)
    return result

def test_permute():
    """测试函数：验证全排列算法"""
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
        ([], [[]])
    ]
    
    print("全排列测试结果:")
    print("=" * 50)
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result1 = permute_backtrack(nums.copy())
        
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
    test_permute()
    