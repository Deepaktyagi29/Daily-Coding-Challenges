class Solution:
    def countSubstr(self, s, k):
        def atMostK(s, k):
            count = {}
            res = left = 0
            for right in range(len(s)):
                count[s[right]] = count.get(s[right], 0) + 1
                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                res += right - left + 1
            return res
        return atMostK(s, k) - atMostK(s, k - 1)

if __name__ == "__main__":
    s = input("Enter the string: ")
    k = int(input("Enter the value of k: "))
    sol = Solution()
    print("Count of substrings with exactly", k, "distinct characters:", sol.countSubstr(s, k))
