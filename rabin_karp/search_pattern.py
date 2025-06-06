class Solution:
    def search(self, pat, txt):
        d = 256
        q = 101
        M = len(pat)
        N = len(txt)
        p = 0
        t = 0
        h = 1
        result = []

        for i in range(M - 1):
            h = (h * d) % q

        for i in range(M):
            p = (d * p + ord(pat[i])) % q
            t = (d * t + ord(txt[i])) % q

        for i in range(N - M + 1):
            if p == t:
                if txt[i:i + M] == pat:
                    result.append(i + 1)
            if i < N - M:
                t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
                if t < 0:
                    t += q

        return result


if __name__ == "__main__":
    txt = input("Enter text: ")
    pat = input("Enter pattern: ")
    sol = Solution()
    result = sol.search(pat, txt)
    print("Pattern found at positions:", result)
