# ============================================================
# 1. 快速排序（基本方法 - 使用额外空间）
# ============================================================
def quick_sort_basic(arr):
    """
    快速排序 - 基本实现（使用额外空间）
    
    思路：
    1. 选择数组中的一个元素作为基准值(pivot)
    2. 将小于基准值的元素放到左边，大于基准值的放到右边
    3. 递归地对左右两部分进行排序
    
    时间复杂度：平均O(nlogn)，最坏O(n²)
    空间复杂度：O(n) - 需要额外数组存储
    
    参数：
        arr: 待排序的数组
    返回：
        排序后的数组
    """
    # 递归终止条件：数组长度小于等于1时已经有序
    if len(arr) <= 1:
        return arr
    
    # 选择中间元素作为基准值（也可以选择第一个或最后一个）
    pivot = arr[len(arr) // 2]
    
    # 将数组分为三部分：小于pivot、等于pivot、大于pivot
    left = [x for x in arr if x < pivot]    # 小于基准值的元素
    middle = [x for x in arr if x == pivot] # 等于基准值的元素
    right = [x for x in arr if x > pivot]   # 大于基准值的元素
    
    # 递归排序左右两部分，并将三部分合并
    return quick_sort_basic(left) + middle + quick_sort_basic(right)

# ============================================================
# 1. 快速排序（原地排序 - 低空间复杂度）
# ============================================================

def quick_sort_inplace(arr, left=0, right=None):
    """
    快速排序 - 原地排序实现（空间优化版本）
    
    思路：
    1. 使用双指针法在原数组上进行分区操作
    2. 选择最右边的元素作为基准值
    3. 将小于基准值的元素移到左边，大于的移到右边
    4. 递归处理左右两个分区
    
    时间复杂度：平均O(nlogn)，最坏O(n²)
    空间复杂度：O(logn) - 仅递归调用栈的空间
    
    参数：
        arr: 待排序的数组（会被直接修改）
        left: 当前排序范围的左边界
        right: 当前排序范围的右边界
    返回：
        None（直接修改原数组）
    """
    # 初始化right为数组最后一个元素的索引
    if right is None:
        right = len(arr) - 1
    
    # 递归终止条件：左边界大于等于右边界
    if left >= right:
        return
    
    # 执行分区操作，返回基准值最终位置
    pivot_index = partition(arr, left, right)
    
    # 递归排序基准值左边的部分
    quick_sort_inplace(arr, left, pivot_index - 1)
    # 递归排序基准值右边的部分
    quick_sort_inplace(arr, pivot_index + 1, right)


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

if __name__ == "__main__":
    print("=" * 60)
    print("1. 快速排序测试")
    print("=" * 60)
    test_arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"原始数组: {test_arr}")
    print(f"基本快排: {quick_sort_basic(test_arr)}")