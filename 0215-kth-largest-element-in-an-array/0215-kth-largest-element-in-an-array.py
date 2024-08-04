from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q=PriorityQueue()
        for i in nums:
            q.put(i,i)
        a=0
        for i in range(len(nums)-k+1):
            a=q.get()
        return a