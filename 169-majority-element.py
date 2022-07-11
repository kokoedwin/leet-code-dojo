class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        set_nums = set(nums)
        big_num = 0
        how_big_num = 0
        for i in set_nums:
            temp = nums.count(i)
            if temp > how_big_num:
                big_num = i
                how_big_num = temp

        return(big_num)

        
