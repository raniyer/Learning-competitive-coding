"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input:
s: "cbaebabacd" p: "abc"
Output:
[0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input:
s: "abab" p: "ab"
Output:
[0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

#learn hash for minimum rumtime
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        l1 = list(p)
        l1.sort()
        for i in range(len(s) - len(p)+ 1):
            l2 = list(s[i:i+len(p)])
            l2.sort()
            if l2 == l1:
                res.append(i)
        return res
                    

#not optimized but easy to understand
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        l1 = list(p)
        l1.sort()
        for i in range(len(s) - len(p)+ 1):
            l2 = list(s[i:i+len(p)])
            l2.sort()
            if l2 == l1:
                res.append(i)
        return res
