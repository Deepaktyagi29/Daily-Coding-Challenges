class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        if not head:
            new_node.next = new_node
            return new_node

        current = head
        while True:
            if current.data <= data <= current.next.data:
                break
            if current.data > current.next.data:
                if data >= current.data or data <= current.next.data:
                    break
            current = current.next
            if current == head:
                break

        new_node.next = current.next
        current.next = new_node
        return head if head.data <= data else new_node

def printCircularList(head):
    if not head:
        print("List is empty")
        return
    result = []
    current = head
    while True:
        result.append(str(current.data))
        current = current.next
        if current == head:
            break
    print(" -> ".join(result))

# Example usage
def createCircularSortedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    current.next = head
    return head

arr = [10, 20, 30, 40]
data_to_insert = 25

head = createCircularSortedList(arr)
print("Original Circular List:")
printCircularList(head)

sol = Solution()
head = sol.sortedInsert(head, data_to_insert)

print("Circular List After Insertion:")
printCircularList(head)
