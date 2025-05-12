import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()
        available = list(range(n))
        heapq.heapify(available)
        busy = []
        count = [0] * n

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                time, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                count[room] += 1
            else:
                time, room = heapq.heappop(busy)
                heapq.heappush(busy, (time + (end - start), room))
                count[room] += 1

        max_count = max(count)
        for i in range(n):
            if count[i] == max_count:
                return i

# Example usage
sol = Solution()
n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]
print(sol.mostBooked(n, meetings))  # Output: 0
