class Solution(object):
    def thirdMax(self, nums):
  
        highest = second_highest = third_highest = -sys.maxint
        for num in nums:
            if num > highest:
                highest, second_highest, third_highest = num, highest, second_highest
            elif num > second_highest and num < highest:
                second_highest, third_highest = num, second_highest
            elif num > third_highest and num < second_highest:
                third_highest = num
        return third_highest if third_highest != -sys.maxint else highest
