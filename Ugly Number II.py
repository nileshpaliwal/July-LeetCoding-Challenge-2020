#rite a program to find the n-th ugly number.
#
#Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
#Example:
#
#Input: n = 10
#Output: 12
#Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#Note:  
#
#1 is typically treated as an ugly number.
#n does not exceed 1690.
#   Hide Hint #1  
#The naive approach is to call isUgly for every number until you reach the nth one. Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
#   Hide Hint #2  
#An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
#   Hide Hint #3  
#The key is how to maintain the order of the ugly numbers. Try a similar approach of merging from three sorted lists: L1, L2, and L3.
#   Hide Hint #4  
#Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).

class Solution(object):
    def nthUglyNumber(self, n): 
        ugly = [1]

        i_2, i_3, i_5 = 0, 0, 0     

        while len(ugly) < n:
            ugly.append(min(2 * ugly[i_2], 3 * ugly[i_3], 5 * ugly[i_5]))

            if ugly[-1] == 2*ugly[i_2]:
                i_2+=1
            if ugly[-1] == 3*ugly[i_3]:
                i_3+=1
            if ugly[-1] == 5*ugly[i_5]:
                i_5+=1
        return ugly[-1]
        