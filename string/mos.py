class Solution:
    def multiplyStrings(self, s1, s2):
        neg = (s1[0] == '-') ^ (s2[0] == '-')
        s1 = s1.lstrip('0-')
        s2 = s2.lstrip('0-')
        if not s1 or not s2:
            return "0"
        n = len(s1)
        m = len(s2)
        res = [0] * (n + m)
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                sum = mul + res[i + j + 1]
                res[i + j + 1] = sum % 10
                res[i + j] += sum // 10
        while res and res[0] == 0:
            res.pop(0)
        if not res:
            return "0"
        ans = ''.join(map(str, res))
        if neg:
            ans = '-' + ans
        return ans

if __name__ == "__main__":
    s1 = input("Enter first number: ")
    s2 = input("Enter second number: ")
    sol = Solution()
    print(sol.multiplyStrings(s1, s2))
