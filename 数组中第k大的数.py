# ============================================================
# 2. 数组中最大的第k个数（第k大元素）
# ============================================================

def find_kth_largest(arr, k):
    """
    找到数组中第k大的元素
    
    核心思路：
    - 如果数组排序后：[1, 2, 3, 4, 5, 6]
    - 第1大是6（索引5），第2大是5（索引4），第3大是4（索引3）
    - 第k大的元素在索引 len(arr) - k 的位置
    
    算法：快速选择（Quick Select）
    1. 使用快排的partition思想，将数组分为两部分
    2. partition后，基准值左边都≤它，右边都≥它
    3. 判断基准值的位置是否就是目标位置
    4. 如果不是，只需要在一侧继续查找（不用两边都找）
    
    时间复杂度：平均O(n)，最坏O(n²)
    空间复杂度：O(1)
    
    参数：
        arr: 输入数组，例如 [3,2,1,5,6,4]
        k: 第几大（k从1开始），例如 k=2 表示第2大
    返回：
        第k大的元素值
    
    示例：
        arr = [3,2,1,5,6,4], k = 2
        排序后 [1,2,3,4,5,6]
        第2大是5，在索引4的位置（len=6, 6-2=4）
    """

    # 计算第k大元素在升序数组中的目标索引
    # 例如：数组长度6，第2大元素在索引 6-2=4 的位置
    target_index = len(arr) - k

    # 初始化查找范围：整个数组
    left, right = 0, len(arr) - 1

    # 循环查找，直到找到目标位置
    while left <= right:
        # 执行分区操作，返回基准值的最终位置
        # partition会将小于等于基准值的放左边，大于的放右边
        pivot_index = partition(arr, left, right)
        
        # 情况1：基准值正好在目标位置，找到答案
        if pivot_index == target_index:
            return arr[pivot_index]
        
        # 情况2：基准值位置 < 目标位置，说明目标在右半部分
        # 例如：pivot在索引2，target在索引4，继续在右边找
        elif pivot_index < target_index:
            left = pivot_index + 1
        # 情况3：基准值位置 > 目标位置，说明目标在左半部分
        else:
            right = pivot_index - 1
    
    # 理论上不会到达这里（如果输入合法的话）
    return -1

def partition(arr, left, right):
    """
    分区函数 - 将数组分为小于和大于基准值的两部分
    
    思路：
    1. 选择最右边的元素作为基准值
    2. 使用i指针维护"小于基准值"区域的右边界
    3. j指针遍历数组，遇到小于基准值的元素就交换到左边
    4. 最后将基准值放到正确位置
    
    参数：
        arr: 数组
        left: 分区左边界
        right: 分区右边界
    返回：
        基准值的最终索引位置
    """
    # 选择最右边的元素作为基准值
    pivot = arr[right]
    
    # i指向"小于pivot区域"的最后一个元素
    # 初始时为left-1，表示该区域为空
    i = left - 1
    
    # j遍历从left到right-1的所有元素
    for j in range(left, right):
        # 如果当前元素小于等于基准值
        if arr[j] <= pivot:
            i += 1  # 扩展"小于pivot区域"
            # 将当前元素交换到"小于pivot区域"的末尾
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准值放到正确位置（i+1是第一个大于pivot的位置）
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    
    # 返回基准值的最终位置
    return i + 1

# 测试示例
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("2. 第K大元素测试")
    print("=" * 60)
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"数组: {arr}, k={k}")
    print(f"第{k}大的元素: {find_kth_largest(arr, k)}")