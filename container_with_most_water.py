class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * width)
            if height[left_pointer] <= height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area
