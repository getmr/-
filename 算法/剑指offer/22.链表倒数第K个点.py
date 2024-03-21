# 链表中倒数第k个节点
# 输入一个链表，输出该链表中倒数第k个结点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾结点是倒数第一个结点。例如一个链表有6个结点，
# 从头结点开始它们的值依次是1、2、3、4、5、6。这个链表的倒数第三个结点是值为4的结点。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 方法一：两次遍历
# 时间复杂度：O(n)
# 空间复杂度：O(1)
# 直接遍历一次获取链表长度，然后通过长度减k活的
def find_kth_to_tail(head, k):
    if not head or k <= 0:
        return None
    length = 0
    node = head
    while node:
        length += 1
        node = node.next
    if k > length:
        return None
    for i in range(length - k):
        head = head.next
    return head

# 方法二：双指针
# 时间复杂度：O(n)
# 空间复杂度：O(1)
def find_kth_to_tail2(head: ListNode, k):

    if head is None or k <= 0:
        return None
    a_head_node = head
    for i in range(k):
        if a_head_node is None:
            return False
        a_head_node = head.next
    p_head_node = head
    while a_head_node.next is not None:
        a_head_node = a_head_node.next
        p_head_node = p_head_node.next
    return p_head_node