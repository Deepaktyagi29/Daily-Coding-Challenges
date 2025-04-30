class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def countNodesInLoop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.countLoopLength(slow)
        return 0

    def countLoopLength(self, node_in_loop):
        count = 1
        current = node_in_loop.next
        while current != node_in_loop:
            count += 1
            current = current.next
        return count

# Sample linked list creation with loop
def createLinkedListWithLoop(values, loop_pos):
    head = Node(values[0])
    current = head
    loop_node = None

    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next
        if i == loop_pos:
            loop_node = current

    if loop_pos != -1:
        current.next = loop_node

    return head

# Example usage
values = [1, 2, 3, 4, 5]
loop_pos = 1  # 0-based index, set to -1 for no loop
head = createLinkedListWithLoop(values, loop_pos)

sol = Solution()
print("Length of Loop:", sol.countNodesInLoop(head))
