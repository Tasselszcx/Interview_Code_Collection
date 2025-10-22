# ============================================================
# 12. 滑动窗口最大值
# ============================================================
"""
题目描述：
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。

核心思路：
单调队列：维护一个递减队列，队首始终是当前窗口最大值

单调队列套路：
1. 右边入（元素进入队尾，同时维护队列单调性）
2. 左边出（元素离开队首）
3. 记录/维护答案（根据队首）

复杂度分析：
- 时间复杂度：O(n) - 单调队列法
- 空间复杂度：O(k) - 存储队列元素
"""

from collections import deque

def max_sliding_window_monotonic_queue(nums, k):
    """
    单调队列法（最优解）
    
    思路：
    1. 使用双端队列存储可能成为最大值的元素索引
    2. 队列保持递减顺序（队首最大）
    3. 移除超出窗口范围的元素
    4. 移除比当前元素小的元素（它们不可能再成为最大值）
    
    优势：时间复杂度O(n)，每个元素入队出队一次
    劣势：逻辑相对复杂
    """
    if not nums or k == 0:
        return []
    
    n = len(nums)
    if k >= n:
        return [max(nums)] if nums else []
    
    result = []
    dq = deque()  # 存储索引的双端队列
    
    for i in range(n):
        # 移除超出窗口范围的元素（从队首）
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # 移除队列中比当前元素小的元素（从队尾）
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        # 将当前元素索引加入队列
        dq.append(i)
        
        # 当窗口形成时，记录最大值（队首元素）
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

def test_sliding_window_maximum():
    """测试函数：验证滑动窗口最大值算法"""
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
        ([], 0, []),
        ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5])
    ]
    
    print("滑动窗口最大值测试结果:")
    print("=" * 50)
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # 测试两种方法
        result1 = max_sliding_window_monotonic_queue(nums, k)
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        
        print(f"测试用例 {i}: {status1}")
        print(f"  数组: {nums}, 窗口大小: {k}")
        print(f"  单调队列法: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_sliding_window_maximum()