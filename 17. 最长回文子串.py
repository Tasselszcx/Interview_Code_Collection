# ============================================================
# 17. 最长回文子串
# ============================================================
"""
题目描述：
给定一个字符串 s，找到 s 中最长的回文子串。
"""

def longest_palindrome_dp(s):
    """
    方法一：动态规划
    
    思路：
    1. dp[i][j]表示s[i:j+1]是否为回文
    2. 状态转移：dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]
    3. 基础情况：单个字符是回文，相邻相同字符是回文
    
    """
    if not s or len(s) < 1:
        return ""
    
    n = len(s)
    # dp[i][j]表示s[i..j]是否为回文
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1  # 至少单个字符是回文
    
    # 所有单个字符都是回文
    for i in range(n):
        dp[i][i] = True
    
    # 检查长度为2的子串
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # 检查长度>=3的子串
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # 首尾字符相同且内部子串是回文
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

def longest_palindrome_center(s):
    """
    方法二：中心扩展法（最优解）
    
    思路：
    1. 遍历每个字符，以该字符为中心向两边扩展
    2. 考虑奇数长度（单个中心）和偶数长度（两个中心）
    3. 记录最长回文子串的起始位置和长度
    """

    if not s or len(s) < 1:
        return ""
    
    start, end = 0, 0  # 记录最长回文子串的起止位置
    
    def expand_around_center(left, right):
        """从中心向两边扩展，返回回文长度"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # 回文长度
    
    for i in range(len(s)):
        # 奇数长度回文（以单个字符为中心）
        len1 = expand_around_center(i, i)
        # 偶数长度回文（以两个字符为中心）
        len2 = expand_around_center(i, i + 1)
        
        # 取较长的回文长度, 以单个字符、以两个字符已经包含了所有情况
        max_len = max(len1, len2)
        
        # 如果找到更长的回文，更新起止位置
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

def test_longest_palindrome():
    """测试函数：验证最长回文子串算法"""
    test_cases = [
        ("babad", "bab"),  # "aba" 也是有效答案
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),  # "c" 也是有效答案
        ("", ""),
        ("abcba", "abcba"),
        ("abb", "bb")
    ]
    
    print("最长回文子串测试结果:")
    print("=" * 50)
    
    for i, (s, expected) in enumerate(test_cases, 1):
            result1 = longest_palindrome_center(s)
            result2 = longest_palindrome_dp(s)
            
            # 由于可能有多个正确答案，检查长度是否一致
            status1 = "✓ 通过" if len(result1) == len(expected) else "✗ 失败"
            status2 = "✓ 通过" if len(result2) == len(expected) else "✗ 失败"
            
            # print(f"测试用例 {i}: {status1} | {status2}")
            print(f"  输入: '{s}'")
            print(f"  中心扩展法: '{result1}' (长度: {len(result1)})")
            print(f"  动态规划法: '{result2}' (长度: {len(result2)})")
            print(f"  预期长度: {len(expected)}")
            print()



if __name__ == "__main__":
    test_longest_palindrome()
    
