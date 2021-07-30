class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j ,k = 0, 0, len(nums)
        
        while j < k:
            if nums[j] < 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] > 1:
                k -= 1
                nums[k], nums[j] = nums[j], nums[k]
            else:
                j += 1
            
#             ps. nums.sort() 한줄로 끝낼 수 있음
