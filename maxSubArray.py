# Given an integer array nums, find the subarray which has the largest sum and return its sum.

class Solution:
    def maxSubArray(nums):
        current_sum = max_sum = nums[0] #assigned 1st element to current sum and max sum 
        for num in nums[1:]:
            print("\n\nCS - ", current_sum)

            current_sum = max(num, current_sum+num) 
            print("maxCur - ", current_sum)
            
            max_sum = max(current_sum, max_sum)
            print("MS - ", max_sum)

        return max_sum


if __name__ == '__main__':
    a = Solution
    print(a.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
