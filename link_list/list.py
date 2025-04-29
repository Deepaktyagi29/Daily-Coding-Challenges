class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

class Solution:
    def segregate(self, head):
        count = [0, 0, 0]
        curr = head
        while curr:
            count[curr.data] += 1
            curr = curr.next
        curr = head
        i = 0
        while curr:
            if count[i] == 0:
                i += 1
            else:
                curr.data = i
                count[i] -= 1
                curr = curr.next
        return head

ll = LinkedList()
for val in [1, 2, 0, 1, 2, 0, 1]:
    ll.append(val)

print("Original List:")
ll.print_list()

s = Solution()
ll.head = s.segregate(ll.head)

print("Sorted List:")
ll.print_list()
