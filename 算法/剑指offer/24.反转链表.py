# 反转链表
"""
题目：定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head: ListNode):
    if head is None:
        return None
    pre_node = None
    p_node = head
    while p_node:
        next_node = p_node.next
        p_node.next = pre_node
        pre_node = p_node

        p_node = next_node
    return pre_node


if __name__ == "__main__":
    # Test case 1: Empty list
    head = None
    result = reverse_list(head)
    print(result)  # Expected output: None

    # Test case 2: Single node list
    head = ListNode(1)
    result = reverse_list(head)
    print(result.val)  # Expected output: 1
    print(result.next)  # Expected output: None

    # Test case 3: Multiple node list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    result = reverse_list(head)
    while result:
        print(result.val)
        result = result.next
    # Expected output: 4 3 2 1