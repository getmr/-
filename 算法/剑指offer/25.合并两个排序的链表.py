# 合并两个排序的链表，并且保持有序
"""
题目: 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
例如: 输入1->3->5->7和2->4->6->8,则合并之后的升序链表为1->2->3->4->5->6->7->8
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    merge_head = None
    if head1.val < head2.val:
        merge_head = head1
        merge_head.next = merge(head1.next, head2)
    else:
        merge_head = head2
        merge_head.next = merge(head1, head2.next)
    return merge_head


def merge2(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    merge_head = None
    if head1.val < head2.val:
        merge_head = head1
        head1 = head1.next
    else:
        merge_head = head2
        head2 = head2.next
    p_node = merge_head
    while head1 and head2:
        if head1.val < head2.val:
            p_node.next = head1
            head1 = head1.next
        else:
            p_node.next = head2
            head2 = head2.next
        p_node = p_node.next
    if head1:
        p_node.next = head1
    if head2:
        p_node.next = head2
    return merge_head


if __name__ == "__main__":
    # 测试用例
    # Test case 1: Empty list
    head1 = None
    head2 = None
    result = merge(head1, head2)
    print(result)  # Expected output: None

    # Test case 2: Single node list
    head1 = ListNode(1)
    head2 = ListNode(2)
    result = merge(head1, head2)
    while result:
        print(result.val)
        result = result.next
    print("+"*10)
    # Expected output: 1 2
        
    # Test case 3: Multiple node list
    head1 = ListNode(1)
    head1.next = ListNode(3)
    head1.next.next = ListNode(5)
    head1.next.next.next = ListNode(7)
    head2 = ListNode(2)
    head2.next = ListNode(4)
    head2.next.next = ListNode(6)
    head2.next.next.next = ListNode(8)
    result = merge(head1, head2)
    while result:
        print(result.val)
        result = result.next
    # Expected output: 1 2 3 4 5 6 7 8