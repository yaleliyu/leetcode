#https://leetcode.com/problems/design-linked-list/
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = None


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1

        node = self.head
        value = -1
        for i in range(index):
            if node is None:
                break
            node = node.next

        if node is not None:
            value = node.val
        return value


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)



    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def deleteAtTail(self):
        self.deleteAtIndex(self.size-1)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            prev = self.head
            cur = prev.next
            for i in range(1, index):
                prev = cur
                cur = prev.next
            prev.next = new_node
            new_node.next = cur

        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return

        if index == 0:
            del_node = self.head
            self.head = self.head.next
            del del_node
        else:
            prev = self.head
            cur = prev.next
            for i in range(1, index):
                prev = cur
                cur = prev.next
            prev.next = cur.next if cur is not None else None
            del cur

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:

obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.addAtTail(4)
obj.deleteAtIndex(1)
obj.deleteAtTail()
print(obj.get(1))
