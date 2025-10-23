# ============================================================
# 13. 螺旋矩阵
# ============================================================
"""
题目描述：
给定一个 m x n 的矩阵，按照螺旋顺序返回矩阵中的所有元素。

核心思路：
1. 模拟法：按照右→下→左→上的顺序遍历，同时调整边界
2. 层层剥离：从外到内一层一层处理

复杂度分析：
- 时间复杂度：O(m×n)，需要访问每个元素一次
- 空间复杂度：O(1)，除了输出数组外，只使用常数空间
"""

def spiral_order_simulation(matrix):
    """
    方法一：边界模拟法（最优解）
    
    思路：
    1. 定义四个边界：上、下、左、右
    2. 按照右→下→左→上的顺序遍历
    3. 每完成一个方向后调整边界
    4. 当边界相遇时结束遍历
    
    优势：逻辑清晰，空间效率高
    劣势：需要处理多个边界条件
    """
    # 空集合直接输出即可
    if not matrix or not matrix[0]:
        return []
    
    # m为行数，n为列数
    m, n = len(matrix), len(matrix[0])
    result = []
    
    # 初始化四个边界
    top, bottom = 0, m - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # 从左到右遍历上边界
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # 从上到下遍历右边界
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # 检查是否还有行需要处理
        if top <= bottom:
            # 从右到左遍历下边界
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
        
        # 检查是否还有列需要处理
        if left <= right:
            # 从下到上遍历左边界
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result

def test_spiral_order():
    """测试函数：验证螺旋矩阵遍历算法"""
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        ([[]], []),
        ([[1]], [1]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3])
    ]
    
    print("螺旋矩阵测试结果:")
    print("=" * 50)
    
    for i, (matrix, expected) in enumerate(test_cases, 1):
        result1 = spiral_order_simulation(matrix)
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        
        print(f"测试用例 {i}: {status1} ")
        print(f"  输入矩阵: {matrix}")
        print(f"  边界模拟法: {result1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_spiral_order()
        
