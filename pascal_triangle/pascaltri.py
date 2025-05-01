class Solution:
    def nthRowOfPascalTriangle(self, n):
        row = [1]
        for i in range(1, n):
            new_row = [1]
            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])
            new_row.append(1)
            row = new_row
        return row

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    sol = Solution()
    result = sol.nthRowOfPascalTriangle(n)
    print("Nth row of Pascal's Triangle:", result)
