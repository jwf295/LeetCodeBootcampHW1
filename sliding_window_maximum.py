class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        for i in range(len(nums) - k + 1):
            max_val = max(nums[i:i+k])
            output.append(max_val)
        return output
