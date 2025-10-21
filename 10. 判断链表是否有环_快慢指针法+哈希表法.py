# ============================================================
# 10. 判断链表是否有环
# ============================================================
"""
题目描述：
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。

核心思路：
1. 快慢指针法：快指针每次走两步，慢指针每次走一步，如果相遇则有环
2. 哈希表法：记录访问过的节点，如果重复访问则有环

复杂度分析：
- 时间复杂度：O(n)
- 空间复杂度：O(1) - 快慢指针法，空间复杂度O(n) - 哈希表法
"""
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def has_cycle_two_pointers(head):
    """
    方法一：快慢指针法（最优解）
    
    思路：
    1. 快指针每次移动两步，慢指针每次移动一步
    2. 如果快慢指针相遇，说明有环
    3. 如果快指针到达链表尾部，说明无环
    
    优势：空间复杂度O(1)，不需要额外存储
    劣势：无法找到环的入口点
    """
    if not head or not head.next:
        return False
    
    slow = head  # 慢指针
    fast = head  # 快指针
    
    while fast and fast.next:
        slow = slow.next          # 慢指针走一步
        fast = fast.next.next     # 快指针走两步
        
        if slow == fast:          # 相遇说明有环
            return True
    
    return False                  # 快指针到达尾部，无环

def has_cycle_hashset(head):
    """
    方法二：哈希表法
    
    思路：
    1. 使用集合记录访问过的节点
    2. 遍历链表，如果节点已在集合中则说明有环
    
    优势：逻辑简单，容易理解
    劣势：空间复杂度O(n)
    """
    visited = set()  # 哈希集
    current = head
    while current:
        if current in visited:
            return True  # 有经过之前经过的点说明有环，返回True
        visited.add(current)  # 否则就加入set中
        current = current.next

    return False


def create_linked_list_with_cycle(values, pos):
    """
    创建带环的链表用于测试
    
    参数：
        values: 链表节点的值列表
        pos: 环的入口位置（-1表示无环）
    """
    if not values:
        return None
    
    # 创建所有节点
    nodes = [ListNode(val) for val in values]
    
    # 连接节点
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # 创建环
    if pos >= 0 and pos < len(nodes):
        nodes[-1].next = nodes[pos]
    
    return nodes[0]

def test_has_cycle():
    """测试函数：验证环检测算法"""
    # 测试用例：(节点值列表, 环位置, 预期结果)
    test_cases = [
        ([3, 2, 0, -4], 1, True),   # 有环
        ([1, 2], 0, True),          # 有环
        ([1], -1, False),           # 无环
        ([], -1, False),            # 空链表
        ([1, 2, 3, 4], -1, False)   # 无环
    ]
    
    print("判断链表是否有环测试结果:")
    print("=" * 50)
    
    for i, (values, pos, expected) in enumerate(test_cases, 1):
        # 创建测试链表
        head = create_linked_list_with_cycle(values, pos)
        
        # 测试两种方法
        result1 = has_cycle_two_pointers(head)
        result2 = has_cycle_hashset(head)
        
        status1 = "✓ 通过" if result1 == expected else "✗ 失败"
        status2 = "✓ 通过" if result2 == expected else "✗ 失败"
        
        print(f"测试用例 {i}: {status1}")
        print(f"  链表: {values}, 环位置: {pos}")
        print(f"  快慢指针法: {result1}")
        print(f"  哈希表法: {result2}")
        print(f"  预期结果: {expected}")
        print()

if __name__ == "__main__":
    test_has_cycle()
