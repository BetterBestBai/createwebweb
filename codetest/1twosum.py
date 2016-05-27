#coding=utf-8
'''
Created on 2016年5月25日

@author: PI
'''
class Solution(object):
    '''
    def __init__(self):
        pass
        '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict={};
        for i in range(len(nums)):
            add1=nums[i]
            if target-add1 in dict:
                print (dict[target-add1],i)
                return (dict[target-add1],i)
                
            else:
                dict[add1]=i
                
                

if __name__=='__main__':
    nums=[2,5,3,1,6] 
    target=3
    ss=Solution()
    ss.twoSum(nums, target)
    