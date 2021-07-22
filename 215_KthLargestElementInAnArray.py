class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for i in nums:
            heapq.heappush(h, -i)
            
        for _ in range(k-1):
            heapq.heappop(h)
            
        return -h[0]
