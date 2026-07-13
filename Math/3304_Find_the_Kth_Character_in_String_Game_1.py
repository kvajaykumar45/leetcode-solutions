class Solution:
    def kthCharacter(self, k: int) -> str:
        word="a"
        while len(word)<k:
            string=""
            for each in word:
                string+=chr(((ord(each)+1)%97)+97)
            word+=string
        return word[k-1]

        
