class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def getMaxSum(self, root):
        def helper(node):
            if not node:
                return (0, 0)
            
            left_include, left_exclude = helper(node.left)
            right_include, right_exclude = helper(node.right)
            
            current_include = node.data + left_exclude + right_exclude
            current_exclude = max(left_include, left_exclude) + max(right_include, right_exclude)
            
            return (current_include, current_exclude)
        
        include, exclude = helper(root)
        return max(include, exclude)

# Test the solution
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

solution = Solution()
print(solution.getMaxSum(root)) 



 # Output: 16