"""
题目：最长公共子序列（Longest Common Subsequence, LCS）
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
如果不存在公共子序列，返回 0。

关键概念：
- 子序列（subsequence）：可以不连续，但必须保持相对顺序
- 例如："ace" 是 "abcde" 的子序列（删除了 b 和 d）
- 例如："aec" 不是 "abcde" 的子序列（顺序改变了）

示例1：
输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，长度为 3

示例2：
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，长度为 3

示例3：
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列
"""

# ============================================================
# 8. 最长公共子序列（动态规划解法）
# ============================================================
def longest_common_subsequence(text1, text2):
    """
    最长公共子序列 - 动态规划解法
    
    核心思路：
    使用二维DP数组，dp[i][j] 表示：
    - text1 的前 i 个字符 和 text2 的前 j 个字符的最长公共子序列长度
    
    状态转移方程：
    1. 如果 text1[i-1] == text2[j-1]：
       当前字符相同，可以加入LCS
       dp[i][j] = dp[i-1][j-1] + 1
    
    2. 如果 text1[i-1] != text2[j-1]：
       当前字符不同，LCS要么来自text1的前i-1个字符，要么来自text2的前j-1个字符
       dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    可视化理解（text1="ace", text2="abcde"）：
           ""  a  b  c  d  e
        "" 0   0  0  0  0  0
        a  0   1  1  1  1  1    ← text1[0]='a' 与 text2[0]='a' 匹配
        c  0   1  1  2  2  2    ← text1[1]='c' 与 text2[2]='c' 匹配
        e  0   1  1  2  2  3    ← text1[2]='e' 与 text2[4]='e' 匹配
    
    解释：
    - dp[1][1] = 1: "a"和"a"的LCS是"a"，长度1
    - dp[2][3] = 2: "ac"和"abc"的LCS是"ac"，长度2
    - dp[3][5] = 3: "ace"和"abcde"的LCS是"ace"，长度3
    
    与最长公共子串的区别：
    - 子串（substring）：必须连续，不匹配时dp[i][j]=0
    - 子序列（subsequence）：可以不连续，不匹配时dp[i][j]=max(dp[i-1][j], dp[i][j-1])
    
    时间复杂度：O(m*n)，m和n分别是两个字符串的长度
    空间复杂度：O(m*n)
    
    参数：
        text1: 第一个字符串
        text2: 第二个字符串
    返回：
        最长公共子序列的长度
    """

   # 边界检查
    if not text1 or not text2:
        return 0
    
    m, n = len(text1), len(text2)
    
    # 创建DP表，大小为 (m+1) x (n+1)
    # dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的LCS长度
    # 第0行和第0列都是0（空字符串的LCS长度为0）
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 填充DP表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 情况1：当前字符相同
            if text1[i - 1] == text2[j - 1]:
                # 在之前的基础上+1
                dp[i][j] = dp[i - 1][j - 1] + 1
            
            # 情况2：当前字符不同
            else:
                # 取"不要text1当前字符"和"不要text2当前字符"中的较大值
                # dp[i-1][j]: text1前i-1个字符 与 text2前j个字符的LCS
                # dp[i][j-1]: text1前i个字符 与 text2前j-1个字符的LCS
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # 右下角的值就是最长公共子序列的长度
    return dp[m][n]

# ============================================================
# 8. 拓展——最长公共子序列，返回长度和具体的子序列
# ============================================================
def longest_common_subsequence_with_sequence(text1, text2):
    """
    最长公共子序列 - 返回长度和具体的子序列
    
    在基础版本上增加回溯，找出具体的LCS字符串
    
    回溯思路：
    从dp[m][n]开始往回找：
    1. 如果text1[i-1] == text2[j-1]，说明这个字符在LCS中，记录下来，往左上走
    2. 如果不相等，往较大值的方向走（上或左）
    
    参数：
        text1: 第一个字符串
        text2: 第二个字符串
    返回：
        (LCS长度, LCS字符串)
    """
    if not text1 or not text2:
        return 0, ""
    
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 填充DP表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # 回溯找出LCS字符串
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        # 如果当前字符相同，说明这个字符在LCS中
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            i -= 1
            j -= 1
        # 如果不相同，往值较大的方向走
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1  # 往上走
        else:
            j -= 1  # 往左走
    
    # 因为是从后往前回溯的，需要反转
    lcs.reverse()
    
    return dp[m][n], ''.join(lcs)

# ============================================================
# 测试函数
# ============================================================

def test_longest_common_subsequence():
    """测试最长公共子序列函数"""
    print("=" * 70)
    print("最长公共子序列（LCS）- 测试")
    print("=" * 70)
    
    # 测试用例1：示例1
    print("\n测试用例1：示例1")
    text1_1 = "abcde"
    text2_1 = "ace"
    print(f"字符串1: '{text1_1}'")
    print(f"字符串2: '{text2_1}'")
    result1 = longest_common_subsequence(text1_1, text2_1)
    length1, seq1 = longest_common_subsequence_with_sequence(text1_1, text2_1)
    print(f"LCS长度: {result1}")
    print(f"LCS字符串: '{seq1}'")
    print(f"预期: 3, 'ace'")
    
    # 测试用例2：示例2
    print("\n测试用例2：示例2")
    text1_2 = "abc"
    text2_2 = "abc"
    print(f"字符串1: '{text1_2}'")
    print(f"字符串2: '{text2_2}'")
    result2 = longest_common_subsequence(text1_2, text2_2)
    length2, seq2 = longest_common_subsequence_with_sequence(text1_2, text2_2)
    print(f"LCS长度: {result2}")
    print(f"LCS字符串: '{seq2}'")
    print(f"预期: 3, 'abc'")
    
    # 测试用例3：示例3
    print("\n测试用例3：示例3（无公共子序列）")
    text1_3 = "abc"
    text2_3 = "def"
    print(f"字符串1: '{text1_3}'")
    print(f"字符串2: '{text2_3}'")
    result3 = longest_common_subsequence(text1_3, text2_3)
    length3, seq3 = longest_common_subsequence_with_sequence(text1_3, text2_3)
    print(f"LCS长度: {result3}")
    print(f"LCS字符串: '{seq3}'")
    print(f"预期: 0, ''")
    
    # 测试用例4：较长字符串
    print("\n测试用例4：较长字符串")
    text1_4 = "AGGTAB"
    text2_4 = "GXTXAYB"
    print(f"字符串1: '{text1_4}'")
    print(f"字符串2: '{text2_4}'")
    result4 = longest_common_subsequence(text1_4, text2_4)
    length4, seq4 = longest_common_subsequence_with_sequence(text1_4, text2_4)
    print(f"LCS长度: {result4}")
    print(f"LCS字符串: '{seq4}'")
    print(f"预期: 4, 'GTAB'")
    
    # 测试用例5：空字符串
    print("\n测试用例5：包含空字符串")
    text1_5 = "abc"
    text2_5 = ""
    print(f"字符串1: '{text1_5}'")
    print(f"字符串2: '{text2_5}'")
    result5 = longest_common_subsequence(text1_5, text2_5)
    print(f"LCS长度: {result5}")
    print(f"预期: 0")

# 运行测试函数
if __name__ == "__main__":
    test_longest_common_subsequence()