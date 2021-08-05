class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            left, right = i+1, len(numbers)-1
            tmp = target-n
            
            while left <= right:
                mid = left + (right - left)//2
                if numbers[mid] < tmp:
                    left = mid + 1
                elif numbers[mid] > tmp:
                    right = mid -1
                else: return i + 1, mid + 1
