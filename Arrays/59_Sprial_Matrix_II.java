

/*
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]

Constraints:
1 <= n <= 20

*/

//Solution

class Solution {
    public int[][] generateMatrix(int n) {
        
        int top = 0;
        int left = 0;
        int right = n-1;
        int bottom = n-1;
        int value = 1;
        int result[][] = new int[n][n];
        while(top<=bottom && left<=right)
        {
            for(int i=left; i<=right; i++)
            {
                result[top][i] = value;
                value++;
            }
            top++;

            for(int i=top; i<=bottom; i++)
            {
                result[i][right] = value;
                value++;
            }
            right--;

            for(int i=right; i>=left; i--)
            {
                result[bottom][i] = value;
                value++;
            }
            bottom--;

            for(int i=bottom; i>=top; i--)
            {
                result[i][left]= value;
                value++;
            }
            left++;
        }
        return result;
        
    }
}

