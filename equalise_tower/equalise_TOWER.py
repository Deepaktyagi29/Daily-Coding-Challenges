def minCost(heights, cost):
    def totalCost(h):
        return sum(abs(heights[i] - h) * cost[i] for i in range(len(heights)))
    
    low = min(heights)
    high = max(heights)
    while low < high:
        mid = (low + high) // 2
        cost1 = totalCost(mid)
        cost2 = totalCost(mid + 1)
        if cost1 < cost2:
            high = mid
        else:
            low = mid + 1
    return totalCost(low)

if __name__ == "__main__":
    heights = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    print(minCost(heights, cost))
