class Solution:
    def findMaximum(self, arr):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid] > arr[mid - 1]:
                low = mid + 1
            else:
                high = mid - 1

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    sol = Solution()
    print("Bitonic Point:", sol.findMaximum(arr))
