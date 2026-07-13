class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        max_len = 0
        max_substring = ""
        char_index = {}

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1
            char_index[s[end]] = end
            if end - start + 1 > max_len:
                max_len = end - start + 1
                max_substring = s[start:end+1]

        return len(max_substring)

        
