class Solution:
    def twoSum( nums, target):
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            print(hashmap)
            if complement in hashmap:
                return [hashmap[complement],i]
                
            hashmap[nums[i]] = i
            
            

if __name__ == "__main__":
    s = Solution
    x=s.twoSum(nums = [3,2,11,15,7], target = 9)
    print(x)