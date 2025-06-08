class Solution:
    def isSumString(self, s):
        def check(s, start, len1, len2):
            s1 = s[start:start+len1]
            s2 = s[start+len1:start+len1+len2]
            if (s1.startswith('0') and len1 > 1) or (s2.startswith('0') and len2 > 1):
                return False
            sum_str = str(int(s1) + int(s2))
            sum_len = len(sum_str)
            next_index = start + len1 + len2
            if next_index + sum_len > len(s):
                return False
            if s[next_index:next_index+sum_len] != sum_str:
                return False
            if next_index + sum_len == len(s):
                return True
            return check(s, start + len1, len2, sum_len)

        n = len(s)
        for len1 in range(1, n):
            for len2 in range(1, n - len1):
                if check(s, 0, len1, len2):
                    return True
        return False

# Input from user
if __name__ == "__main__":
    s = input("Enter the string of digits: ")
    sol = Solution()
    result = sol.isSumString(s)
    print("Yes" if result else "No")
