# ============================================================
# 18. 删除链表倒数第k个节点
# ============================================================
"""
题目描述：
给定一个链表，删除链表的倒数第k个节点，并返回链表的头节点。
"""
class ListNode:
    """链表节点定义"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end_two_pointers(head, k):
    """
    方法：双指针法
    
    思路：
    1. 使用快慢指针，快指针先走k步
    2. 然后快慢指针一起移动，直到快指针到达尾部
    3. 此时慢指针指向要删除节点的前一个节点
    """
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    for _ in range(k + 1):
        fast = fast.next
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
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


def test_remove_nth_from_end():
    """测试函数：验证删除倒数第k个节点算法"""
    test_cases = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # 删除倒数第2个节点(4)
        ([1], 1, []),                         # 删除唯一节点
        ([1, 2], 1, [1]),                     # 删除尾节点
        ([1, 2], 2, [2]),                     # 删除头节点
        ([1, 2, 3], 3, [2, 3]),               # 删除头节点
    ]
    
    print("删除链表倒数第k个节点测试结果:")
    print("=" * 50)
    
    for i, (arr, k, expected) in enumerate(test_cases, 1):
        # 创建测试链表
        head1 = create_linked_list(arr)
        head2 = create_linked_list(arr)
        
        # 测试两种方法
        result1 = remove_nth_from_end_two_pointers(head1, k)
        
        list1 = linked_list_to_list(result1)
        
        status1 = "✓ 通过" if list1 == expected else "✗ 失败"
        
        print(f"  输入链表: {arr}, k={k}")
        print(f"  双指针法: {list1}")
        print(f"  预期结果: {expected}")
        print()


if __name__ == "__main__":
    test_remove_nth_from_end()