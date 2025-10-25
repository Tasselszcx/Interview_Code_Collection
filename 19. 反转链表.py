# ============================================================
# 19. 反转链表
# ============================================================
"""
题目描述：
给定单链表的头节点 head ，请反转链表，并返回反转后的链表。
"""
class ListNode:
    """链表节点定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list_iterative(head):
    """
    方法一：迭代法（最优解）
    
    思路：
    1. 使用三个指针：prev, current, next
    2. 逐个反转节点的指向
    3. 最终prev成为新的头节点
    """
    prev = None
    current = head
    
    while current:
        # 保存下一个节点
        next = current.next
        # 反转当前节点的指向
        current.next = prev
        # 移动指针
        prev = current
        current = next
    
    return prev

def reverse_list_dummy(head):
    """
    方法二：头插法（使用哑节点）
    
    思路：
    1. 创建哑节点作为新链表的头部
    2. 遍历原链表，将每个节点插入到哑节点之后
    3. 最终哑节点的下一个节点就是反转后的头节点
    """
    dummy = ListNode(0)
    current = head
    
    while current:
        # 保存下一个节点
        next_temp = current.next
        # 将当前节点插入到哑节点之后
        current.next = dummy.next
        dummy.next = current
        # 移动到下一个节点
        current = next_temp
    
    return dummy.next


def create_linked_list(arr):
    """根据数组创建链表"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def linked_list_to_list(head):
    """将链表转换为列表"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


def test_reverse_list():
    """测试函数：验证链表反转算法"""
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
        ([1, 2], [2, 1])
    ]
    
    print("反转链表测试结果:")
    print("=" * 50)
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        # 创建测试链表
        head1 = create_linked_list(arr)
        head2 = create_linked_list(arr)
        
        # 测试三种方法
        result1 = reverse_list_iterative(head1)
        result2 = reverse_list_dummy(head2)
        
        list1 = linked_list_to_list(result1)
        list2 = linked_list_to_list(result2)

        print(f"  输入链表: {arr}")
        print(f"  迭代法: {list1}")
        print(f"  头插法: {list2}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_reverse_list()