class Solution:
    def minDeletions(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if length > 2 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return n - dp[0][n - 1]

if __name__ == "__main__":
    s = input("Enter the string: ")
    sol = Solution()
    result = sol.minDeletions(s)
    print("Minimum deletions to make it a palindrome:", result)
