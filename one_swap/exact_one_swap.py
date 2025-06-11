class Solution:
    def longestCommonSum(self, a1, a2):
        n = len(a1)
        diff = {}
        max_len = 0
        prefix1 = 0
        prefix2 = 0
        for i in range(n):
            prefix1 += a1[i]
            prefix2 += a2[i]
            curr_diff = prefix1 - prefix2
            if curr_diff == 0:
                max_len = i + 1
            elif curr_diff in diff:
                max_len = max(max_len, i - diff[curr_diff])
            else:
                diff[curr_diff] = i
        return max_len

if __name__ == "__main__":
    a1 = [0, 1, 0, 1, 1, 1, 1]
    a2 = [1, 1, 1, 0, 0, 1, 0]
    sol = Solution()
    print(sol.longestCommonSum(a1, a2))
