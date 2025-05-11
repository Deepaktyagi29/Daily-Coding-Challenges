from typing import List
import heapq

class Solution:
    def kthLargest(self, arr: List[int], k: int) -> int:
        n = len(arr)
        min_heap = []
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                if len(min_heap) < k:
                    heapq.heappush(min_heap, current_sum)
                else:
                    if current_sum > min_heap[0]:
                        heapq.heappop(min_heap)
                        heapq.heappush(min_heap, current_sum)
        
        return min_heap[0]