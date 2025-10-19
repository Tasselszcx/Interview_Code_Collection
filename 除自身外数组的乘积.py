# ============================================================
# 6. 除自身外数组的乘积（方法1：基本方法 - 使用左右乘积数组）
# ============================================================

def product_except_self_basic(nums):
    """
    除自身外数组的乘积 - 基础方法（使用额外数组）
    
    核心思路：
    对于位置i的结果 = 左边所有数的乘积 * 右边所有数的乘积
    
    可视化理解（以 [1,2,3,4] 为例）：
    位置:      0    1    2    3
    原数组:    1    2    3    4
    左积数组:  1    1    2    6    (left[i] = nums[0]*...*nums[i-1])
    右积数组:  24   12   4    1    (right[i] = nums[i+1]*...*nums[n-1])
    结果数组:  24   12   8    6    (answer[i] = left[i] * right[i])
    
    详细解释：
    - left[0] = 1 (左边没有元素)
    - left[1] = 1 (左边只有nums[0]=1)
    - left[2] = 1*2 = 2 (左边是nums[0]*nums[1])
    - left[3] = 1*2*3 = 6 (左边是nums[0]*nums[1]*nums[2])
    
    - right[3] = 1 (右边没有元素)
    - right[2] = 4 (右边只有nums[3]=4)
    - right[1] = 3*4 = 12 (右边是nums[2]*nums[3])
    - right[0] = 2*3*4 = 24 (右边是nums[1]*nums[2]*nums[3])
    
    算法步骤：
    1. 创建left数组，left[i]存储nums[0]到nums[i-1]的乘积
    2. 创建right数组，right[i]存储nums[i+1]到nums[n-1]的乘积
    3. 结果answer[i] = left[i] * right[i]
    
    时间复杂度：O(n) - 需要遍历三次数组
    空间复杂度：O(n) - 需要left和right两个额外数组
    
    参数：
        nums: 输入数组
    返回：
        结果数组，answer[i] = 除nums[i]外所有元素的乘积
    """
    n = len(nums)
    
    # 创建三个数组
    left = [1] * n    # left[i] = nums[0] * ... * nums[i-1]
    right = [1] * n   # right[i] = nums[i+1] * ... * nums[n-1]
    answer = [1] * n  # 最终结果，初始化为1

    # left[i] 表示位置i左边所有数的乘积
    for i in range(1, n):
        # left[i] = left[i-1] 的基础上再乘以 nums[i-1]
        left[i] = left[i - 1] * nums[i - 1]

    # right[i] 表示位置i右边所有数的乘积
    for i in range(n - 2, -1, -1):
        # right[i] = right[i+1] 的基础上再乘以 nums[i+1]
        right[i] = right[i + 1] * nums[i + 1]
    
    for i in range(n):
        answer[i] = left[i] * right[i]
    
    return answer

# ============================================================
# 6. 除自身外数组的乘积（方法2：空间优化方法 - 只使用输出数组（O(1)额外空间））
# ============================================================

def product_except_self_optimized(nums):
    """
    除自身外数组的乘积 - 空间优化方法（推荐）
    
    优化思路：
    - 方法1需要left和right两个额外数组，空间O(n)
    - 观察发现：可以直接用answer数组存储左积，然后用一个变量维护右积
    - 这样就不需要额外的数组了！
    
    算法流程：
    1. 第一遍：answer[i]先存储左边的乘积
    2. 第二遍：从右向左遍历，用变量right_product维护右边的乘积
              同时更新answer[i] *= right_product
    
    可视化过程（以 [1,2,3,4] 为例）：
    
    第一遍后：answer = [1, 1, 2, 6]
              每个位置存储的是左边的乘积
    
    第二遍：从右向左，用right_product维护右边的乘积
    - i=3: right_product=1, answer[3] = 6*1 = 6
    - i=2: right_product=4, answer[2] = 2*4 = 8
    - i=1: right_product=12, answer[1] = 1*12 = 12
    - i=0: right_product=24, answer[0] = 1*24 = 24
    
    最终：answer = [24, 12, 8, 6]
    
    时间复杂度：O(n) - 两次遍历
    空间复杂度：O(1) - 除了输出数组外，只用了常数空间
    
    参数：
        nums: 输入数组
    返回：
        结果数组，answer[i] = 除nums[i]外所有元素的乘积
    """
    n = len(nums)

    # 结果数组，初始化为1
    answer = [1] * n

    # left_product 记录当前位置左边所有数的乘积
    left_product = 1

    # answer[i] 将存储 nums[0] * nums[1] * ... * nums[i-1]
    for i in range(n):
        # answer[i] 先存储左边的乘积
        # 对于第一个元素，左边没有数，所以是1
        answer[i] = left_product

        # 更新 left_product，为下一个位置准备
        # 当前位置的数要参与到下一个位置的左积中
        left_product *= nums[i]
    
    # right_product 记录当前位置右边所有数的乘积
    right_product = 1

    for i in range(n - 1, -1, -1):
        # answer[i] 已经存储了左边的乘积
        # 现在乘上右边的乘积，得到最终结果
        old = answer[i]
        answer[i] *= right_product
        
        # 更新 right_product，为下一个位置（左边一个位置）准备
        right_product *= nums[i]
    
    return answer

def test_product_except_self():
    """测试除自身外数组的乘积函数"""
    print("=" * 70)
    print("6. 除自身外数组的乘积 - 测试")
    print("=" * 70)
    
    # 测试用例1：基本情况（展示基础方法）
    nums1 = [1, 2, 3, 4]
    print(f"\n输入数组: {nums1}")
    result1 = product_except_self_basic(nums1)
    print(f"基础方法输出结果: {result1}")
    print(f"✓ 验证: 24=2×3×4, 12=1×3×4, 8=1×2×4, 6=1×2×3")

    # 测试用例2：基本情况（展示优化方法）
    nums2 = [1, 2, 3, 4]
    print(f"\n输入数组: {nums2}")
    result2 = product_except_self_optimized(nums2)
    print(f"空间优化方法输出结果: {result2}")

if __name__ == "__main__":
    test_product_except_self()