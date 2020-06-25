"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:
    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        collen = len(matrix)
        rowlen = len(matrix[0])
        nsquare = [[0]*rowlen for _ in range(collen)]
        totalsquare = 0
        for i in range(collen):
            for j in range(rowlen):
                if matrix[i][j]:
                    nsquare[i][j] += 1 + min(nsquare[i][j - 1], nsquare[i - 1][j], nsquare[i - 1][j - 1])
                    totalsquare += nsquare[i][j]
        return totalsquare
   
