# 从尾到头打印链表
"""
题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class ListNode(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)


def print_list_reversingly(node):
    if node:
        if node.next:
            print_list_reversingly(node.next)
        print(node.value)


if __name__ == '__main__':
    list_node = ListNode()
    for i in range(10):
        list_node.add(i)
    print_list_reversingly(list_node.head)
