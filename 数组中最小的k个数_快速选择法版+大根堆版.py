# ============================================================
# 3. 数组中最小的k个数 - 快速选择+分区
# ============================================================
import random

def find_k_smallest(arr, k):
    """
    方法一：使用快速选择找到第k小的元素，然后返回所有小于等于它的元素
    
    参数:
        arr: 输入数组
        k: 要找到的最小数的个数
    
    思路：
    1. 使用快速选择算法找到第k小的元素位置
    2. 该位置左边的所有元素都是最小的k个数
    
    时间复杂度: 平均O(n)，最坏O(n²)
    空间复杂度: O(log n) 递归栈空间
    """
    if k == 0 or len(arr) == 0:
        return []
    
    # 创建数组副本，避免修改原数组
    arr_copy = arr.copy()
    
    def quick_select(left, right, k_smallest):
        """
        快速选择递归函数
        
        参数:
            left, right: 当前搜索区间
            k_smallest: 要找的第k小的元素位置
        """
        # 递归终止条件
        if left >= right:
            return
        
        # 随机选择基准元素，避免最坏情况
        random_index = random.randint(left, right)
        # 将随机选择的基准元素交换到最右侧
        arr_copy[random_index], arr_copy[right] = arr_copy[right], arr_copy[random_index]
        
        # 使用给定的partition函数进行分区
        pivot_index = partition(arr_copy, left, right)
        
        # 根据基准位置决定递归方向
        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            quick_select(left, pivot_index - 1, k_smallest)
        else:
            quick_select(pivot_index + 1, right, k_smallest)
    
    # 找到第k小的元素的位置
    quick_select(0, len(arr_copy) - 1, k - 1)
    
    # 返回前k个元素
    return sorted(arr_copy[:k])

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

# ============================================================
# 3. 数组中最小的k个数 - 堆排序
# ============================================================
import heapq
def find_k_smallest_heap(arr, k):
    """
    使用大根堆找到数组中最小的k个数
    
    参数:
        arr: 输入数组
        k: 要找到的最小数的个数
    
    思路:
        1. 维护一个大小为k的大根堆
        2. 当堆满时，新元素如果小于堆顶则替换
        3. 最终堆中就是最小的k个数
    
    时间复杂度: O(n log k)
    空间复杂度: O(k)
    """
    if k == 0 or len(arr) == 0:
        return []
    
    # python中的heapq是小根堆，使用负数来模拟大根堆
    max_heap = []
    for num in arr:
        # 将当前元素的负数加入堆中（模拟大根堆）
        heapq.heappush(max_heap, -num)

        # 如果堆的大小超过k，弹出堆顶元素
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    
    # 将堆中的负数还原为正数并返回
    return sorted([-x for x in max_heap])


# 测试示例
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("3. 数组中最小的k个数测试")
    print("=" * 60)

    test_arr = [4, 5, 3, 3, 3, 1, 6, 2, 7, 3, 8, 3, 3, 3]
    k = 3
    result = find_k_smallest(test_arr, k)
    print(f"快速选择法 - 数组 {test_arr} 中最小的 {k} 个数是: {result}")
    print()
    print(f"大根堆法 - 数组 {test_arr} 中最小的 {k} 个数是: {find_k_smallest_heap(test_arr, k)}")
