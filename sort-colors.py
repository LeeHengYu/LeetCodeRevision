class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # pointer method
        red, white, blue = 0, 0, len(nums)-1 # starting points
        while white<=blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1

            elif nums[white] == 1:
                white += 1

            else:
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1