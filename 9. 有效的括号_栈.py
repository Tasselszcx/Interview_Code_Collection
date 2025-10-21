# ============================================================
# 9. 有效的括号
# ============================================================
"""
题目描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

核心思路：
使用栈来匹配括号，遇到左括号入栈，遇到右括号检查栈顶是否匹配

复杂度分析：
- 时间复杂度：O(n)，n为字符串长度
- 空间复杂度：O(n)，最坏情况下需要存储所有左括号
"""
def is_valid(s):
    """
    栈方法
    
    思路：
    1. 使用栈存储遇到的左括号
    2. 遇到右括号时，检查栈顶是否匹配
    3. 最终栈为空则有效
    """
    
    # 创建括号映射表：右括号 -> 左括号
    # 这样可以快速判断是否匹配
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    # 优化：如果字符串长度是奇数，不可能全部匹配
    if len(s) % 2 != 0:
        return False
    
    for char in s:
        if char in bracket_map.values():
            # 左括号，入栈
            stack.append(char)
        elif char in bracket_map.keys():
            # 右括号，检查匹配
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()  # 匹配成功，弹出栈顶
        else:
            # 非法字符
            return False
    
    # 栈为空说明所有括号都匹配成功
    return len(stack) == 0

def test_valid_parentheses():
    """测试函数：验证括号有效性判断"""
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((()))", True),
        ("((())", False)
    ]
    print("有效的括号测试结果:")
    print("=" * 50)
    
    for i, (s, expected) in enumerate(test_cases, 1):
        result = is_valid(s)
        status = "✓ 通过" if result == expected else "✗ 失败"
        
        print(f"测试用例 {i}: {status}")
        print(f"  输入: '{s}'")
        print(f"  输出: {result}")
        print(f"  预期: {expected}")
        print()

if __name__ == "__main__":
    test_valid_parentheses()
