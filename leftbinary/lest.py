class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def LeftView(self, root):
        if not root:
            return []
        result = []
        queue = [(root, 0)]
        level_map = {}
        for node, level in queue:
            if level not in level_map:
                level_map[level] = node.data
                result.append(node.data)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result

# Example usage
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    sol = Solution()
    print(sol.LeftView(root))  # Output: [1, 2, 4]
