"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
    The input strings only contain lower case letters.
    The length of both given strings is in range [1, 10,000].
"""

#Use hash it's very efficient

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashp = sum(hash(ch) for ch in s1)
        hashi = sum(hash(ch) for ch in s2[:len(s1)-1])
        for (ch_out, ch_in) in zip([""] + list(s2), s2[len(s1)-1:]):
            hashi += hash(ch_in) - hash(ch_out)
            if hashi == hashp:
                return True
                
        return False
        
