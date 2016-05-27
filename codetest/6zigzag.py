#coding=utf-8
'''
Created on 2016年5月26日

@author: PI
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        slist=list(s)
        ss=[]
        if numRows==1:
            return s
        else:
            period = 2*numRows-2
            for i in range(numRows):
                for j in range(i,len(s),period):
                    ss.append(slist[j])
                    secondjj=(j-i)+period-i
                    if(i != 0 and i != numRows-1 and secondjj<len(slist)):
                        ss.append(slist[secondjj])
            print ss
            zigzags=''.join(ss)
            return zigzags
                    
                
                
if __name__=='__main__':
    s='PAYPALISHIR'
    num=4
    aa=Solution()
    aa.convert(s,num)
    