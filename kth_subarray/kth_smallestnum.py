class Solution(object):
    def kthSmallest(self, m, n, k):
        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            count = 0
            for i in range(1, m + 1):
                count += min(mid // i, n)
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    m = 3
    n = 3
    k = 5
    result = solution.kthSmallest(m, n, k)
    print(f"The {k}-th smallest number in the {m}x{n} multiplication table is: {result}")
