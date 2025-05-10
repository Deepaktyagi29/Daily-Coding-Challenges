class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if arr[i] > k else -1)

        stack = []
        for i in range(n + 1):
            if not stack or prefix[i] < prefix[stack[-1]]:
                stack.append(i)

        res = 0
        for i in range(n, -1, -1):
            while stack and prefix[i] > prefix[stack[-1]]:
                res = max(res, i - stack.pop())
        return res


# Driver code to test
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 1]
    k = 2
    print("Longest subarray length:", sol.longestSubarray(arr, k))
