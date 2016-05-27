#coding=utf-8
'''
Created on 2016年5月26日

@author: PI
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        aa=[]
        nums.sort()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    sum3=nums[i]+nums[j]+nums[k]
                    if sum3==0:
                        subnums=[nums[i],nums[j],nums[k]]
                        if subnums not in aa:
                            aa.append(subnums)  
        print aa
        for i in range(len(aa)):             
            return aa[i]

if __name__=='__main__':
    numss = [-1,0,2,-4,-1,1]      
    x = Solution()
    x.threeSum(numss)     