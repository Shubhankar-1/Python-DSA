class Solution:
    def intersect( nums1, nums2):
        hashmap = {}
        for x in range(len(nums1)):
            hashmap[nums1[x]] = x

            
        return hashmap


if __name__ == '__main__':
    a = Solution
    print(a.intersect(nums1=[1, 2, 2, 1], nums2=[2, 2]))
