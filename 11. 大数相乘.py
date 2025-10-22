# ============================================================
# 11. 大数相乘
# ============================================================
"""
题目描述：
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，也用字符串表示。
注意：不能使用任何内置的大整数库或直接将输入转换为整数。

核心思路：
模拟竖式乘法：逐位相乘然后累加

复杂度分析：
- 时间复杂度：O(m×n)，m和n分别是两个数字的长度
- 空间复杂度：O(m+n)存储中间结果
"""

def multiply_big_numbers(num1, num2):
    """
    竖式乘法模拟
    
    思路：
    1. 创建结果数组，长度为len(num1)+len(num2)
    2. 从低位到高位逐位相乘
    3. 处理进位
    4. 去除前导零
    
    优势：模拟人工计算，逻辑清晰
    劣势：需要处理进位和前导零
    """

    if num1 == "0" or num2 == "0":
        return "0"
    
    m, n = len(num1), len(num2)
    # 结果数组，最大长度为m+n
    result = [0] * (m + n)
    
    # 从低位到高位逐位相乘
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # 当前位的乘积
            mul = int(num1[i]) * int(num2[j])
            # 乘积在结果数组中的位置
            p1, p2 = i + j, i + j + 1
            
            # 当前总和（包括之前的进位）
            total = mul + result[p2]
            
            # 更新结果数组
            result[p2] = total % 10  # 个位
            result[p1] += total // 10  # 进位
    
    # 将结果数组转换为字符串
    result_str = ''.join(str(x) for x in result)
    
    # 去除前导零
    start_index = 0
    while start_index < len(result_str) and result_str[start_index] == '0':
        start_index += 1
    
    return result_str[start_index:] if start_index < len(result_str) else "0"

def test_big_number_multiplication():
    """测试函数：验证大数相乘算法"""
    test_cases = [
        ("2", "3", "6"),
        ("123", "456", "56088"),
        ("0", "123", "0"),
        ("999", "999", "998001"),
        ("1" * 10, "1" * 10, "1234567900987654321"),  # 特殊模式
        ("", "123", "0"),  # 空字符串处理
    ]
    
    print("大数相乘测试结果:")
    print("=" * 50)
    
    for i, (num1, num2, expected) in enumerate(test_cases, 1):
        # 处理空字符串
        if not num1 or not num2:
            num1 = num1 or "0"
            num2 = num2 or "0"
        
        # 测试两种方法
        result1 = multiply_big_numbers(num1, num2)
        #result2 = multiply_simple(num1, num2)
        
        # 验证结果正确性（使用Python内置乘法验证）
        expected_python = str(int(num1) * int(num2))
        
        status1 = "✓ 通过" if result1 == expected_python else "✗ 失败"
        #status2 = "✓ 通过" if result2 == expected_python else "✗ 失败"
        
        print(f"测试用例 {i}: {status1}")
        print(f"  输入: '{num1}' × '{num2}'")
        print(f"  竖式乘法: {result1}")
        #print(f"  简化版: {result2}")
        print(f"  预期结果: {expected_python}")
        print()


if __name__ == "__main__":
    test_big_number_multiplication()