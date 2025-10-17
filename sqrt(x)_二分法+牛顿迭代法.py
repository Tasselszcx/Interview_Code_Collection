# ============================================================
# 4. 计算平方根 - 二分法
# ============================================================
def my_sqrt(x):
    """
    计算并返回 x 的平方根（精确到小数点后两位）
    
    方法：二分查找
    
    核心思路：
    1. 平方根一定在 [0, x] 范围内（当x≥1时，可优化为[0, x/2+1]）
    2. 使用二分查找在这个范围内找答案
    3. 不断缩小范围，直到精度满足要求（0.01）
    
    算法流程：
    1. 设定查找范围 left=0, right=x
    2. 取中点 mid，计算 mid²
    3. 如果 mid² > x，说明答案在左半边，right = mid
    4. 如果 mid² < x，说明答案在右半边，left = mid
    5. 当 right - left < 0.01 时，精度已满足要求
    
    时间复杂度：O(log(x/precision))，precision=0.01
    空间复杂度：O(1)
    
    参数：
        x: 非负数（整数或浮点数）
    返回：
        x的平方根，保留两位小数
    
    示例：
        my_sqrt(2) → 1.41
        my_sqrt(8) → 2.83
        my_sqrt(0.25) → 0.50
    """

    # 特殊情况处理
    if x < 0:
        raise ValueError("输入必须是非负数")
    if x == 0 or x == 1:
        return round(x, 2)
    
    # 设定精度：小数点后两位，即误差 < 0.01
    precision = 0.01

    # 初始化二分查找的范围
    # 优化：对于x>1，平方根一定小于x/2+1
    if x < 1:
        left, right = x, 1.0 # 对于0<x<1的情况，平方根在[x,1]之间
    else:
        left, right = 0.0, x / 2 + 1

    # 二分查找，直到范围足够小
    while right - left >= precision:
        # 计算中点
        mid = (left + right) / 2

        # 计算 mid 的平方
        mid_squared = mid * mid
        
        # 判断mid²与x的关系，调整查找范围
        if abs(mid_squared - x) < precision:
            # mid²已经足够接近x，可以返回
            return round(mid, 2)  
        elif mid_squared > x:
            # mid² > x，答案在左半边
            right = mid  
        else:
            # mid² < x，答案在右半边
            left = mid   # 答案在右半边

    return round((left + right) / 2, 2)

# ============================================================
# 4. 计算平方根 - 牛顿迭代法
# ============================================================
def my_sqrt_newton(x):
    """
    计算并返回 x 的平方根（牛顿迭代法，精确到小数点后两位）
    
    方法：牛顿迭代法（Newton's Method）
    
    数学原理：
    - 要求解方程 f(k) = k² - x = 0
    - 牛顿迭代公式：k_new = k - f(k)/f'(k)
    - 其中 f'(k) = 2k
    - 代入得：k_new = k - (k²-x)/(2k) = (k + x/k) / 2
    
    几何意义：
    - 从一个初始猜测值开始
    - 在该点做切线，切线与x轴的交点作为新的猜测值
    - 不断重复，快速收敛到真实值
    
    优点：收敛速度非常快（二次收敛）
    
    时间复杂度：O(log(log(x/precision)))，比二分查找更快
    空间复杂度：O(1)
    
    参数：
        x: 非负数
    返回：
        x的平方根，保留两位小数
    
    示例：
        my_sqrt_newton(2) → 1.41
        my_sqrt_newton(8) → 2.83
    """

    # 特殊情况处理
    if x < 0:
        raise ValueError("输入必须是非负数")
    if x == 0 or x == 1:
        return round(x, 2)
    
    # 设定精度：小数点后两位，即误差 < 0.01
    precision = 0.01

    # 初始猜测值：取 x/2 或 1（取较大者作为起点）
    # 对于大数，x/2 是更好的初始值
    # 对于小数（0<x<1），1 是更好的初始值
    k = max(1.0, x / 2)

    # 牛顿迭代：不断用新值更新 k
    # 当 k² 足够接近 x 时停止
    while abs(k * k - x) >= precision:
        # 牛顿迭代公式：k_new = (k + x/k) / 2
        # 推导：切线方程 y - (k²-x) = 2k(x - k)
        # 令 y=0，解得下一个近似值
        k = (k + x / k) / 2  # 牛顿迭代公式

    # 返回结果，保留两位小数
    return round(k, 2)

# 测试示例
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("4. 平方根计算测试")
    print("=" * 60)
    test_cases = [2, 8, 0.25, 16, 25, 1, 0]
    for x in test_cases:
        result = my_sqrt(x)
        print(f"二分法: my_sqrt({x}) = {result}")
    print()
    for x in test_cases:
        result_newton = my_sqrt_newton(x)
        print(f"牛顿迭代法: my_sqrt_newton({x}) = {result_newton}")