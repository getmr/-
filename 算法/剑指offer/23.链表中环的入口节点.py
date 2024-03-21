# 链表中环的入口节点
"""
题目: 如果一个链表中包含环, 如何找出环的入口节点?
解题思路：首先确定链表中是否有环, 可以使用两个指针, 一个指针一次走一步, 一个指针一次走两步, 如果走得快的指针追上了走得慢的指针, 那么链表中包含环; 
接下来找出环的入口节点, 还是可以使用两个指针, 一个指针先走n步, 然后两个指针一起走, 当两个指针相遇时, 就是环的入口节点
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def meeting_node(head):
    """
    找出环中的相遇的点
    快慢指针
    """
    if not head:
        return None
    slow = head.next
    if not slow:
        return None
    fast = slow.next
    while slow and fast:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next
    return None


def entry_node_of_loop(head):
    """
    两个指针分别在端点和相遇点，每次走一步，相遇点即为环的入口
    """
    meeting = meeting_node(head)
    if not meeting:
        return None
    node1 = head
    node2 = meeting
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next
    return node1