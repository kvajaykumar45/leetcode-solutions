class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i = i + 1
            elif not s[j].isalnum():
                j = j - 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i=i+1
                j=j-1
        return True



