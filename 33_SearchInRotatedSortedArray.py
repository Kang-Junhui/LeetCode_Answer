class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         밑 두줄로 풀이 가능
#         try: return nums.index(target)
#         except: return -1
        
        
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        
        left, right = 0 , len(nums) - 1
        while left <= right:
            mid = left + (right - left) //2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
        return -1
