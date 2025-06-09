class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(node, data):
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node

class Solution:
    def isDeadEnd(self, root):
        def dfs(node, min_val, max_val):
            if not node:
                return False
            if min_val == max_val:
                return True
            return dfs(node.left, min_val, node.data - 1) or dfs(node.right, node.data + 1, max_val)
        return dfs(root, 1, float('inf'))

# Sample Input
# Enter number of nodes followed by space-separated node values
# Example: 7 8 5 9 2 7 1 3

arr = list(map(int, input("Enter nodes: ").split()))
n = arr[0]
values = arr[1:]

root = None
for val in values:
    root = insert(root, val)

sol = Solution()
print("Yes" if sol.isDeadEnd(root) else "No")
