/*
1143 Longest Common Subsequence


Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

 Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

 

Constraints:
1. 1 <= text1.length, text2.length <= 1000
2. text1 and text2 consist of only lowercase English characters.
*/

// Top DownDP Solution (Recursion + Memoization)

    static int findLongestCommonSubsequence(String firstText, String secondText) {
                int n = firstText.length();
                int m = secondText.length();
                int memo[][] = new int[n][m];
                for(int i=0; i<n; i++)
                    Arrays.fill(memo[i], -1);
                int count = LCS(firstText, secondText, 0, 0, memo);
                return count;
    }
    
    static int LCS(String first, String second, int i, int j, int[][] memo)
    {
        if(i == first.length() || j == second.length())
        {
            return 0;
        }
        if(memo[i][j] != -1)
            return memo[i][j]; 
        
        if(first.charAt(i) == second.charAt(j))
        {
            memo[i][j] =  1 + LCS(first, second, i+1, j+1, memo);
        }
        else 
        {
            memo[i][j] = Math.max(LCS(first, second, i+1, j, memo), LCS(first, second, i, j+1, memo));
        }
        return memo[i][j];
    }
    
/*
​Time Complexity: O(n × m)
Because:
    • i can have n possible positions.
    • j can have m possible positions.
    • Therefore, there are at most n × m different (i, j) subproblems.
    • Each subproblem is calculated only once because of memo.
So: Time = O(n × m)
​
Space Complexity: O(n × m)
Your memo table is: int[][] memo = new int[n][m];  which requires n × m space.
There is also recursion-stack space of up to O(n + m), but the memo table dominates it.
So: Space = O(n × m)
​*/

//Bottom Up DP Solution

class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();

        int dp[][] = new int[n+1][m+1];
        for(int i=1; i<=n; i++)
        {
            for(int j=1; j<=m; j++)
            {
                if(text1.charAt(i-1) == text2.charAt(j-1))
                {
                    dp[i][j] = 1 + dp[i-1][j-1];                }
                else
                {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[n][m];
    }
}

/*

Time  → O(n × m)
Space → O(n × m)
*/

