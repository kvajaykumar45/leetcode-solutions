class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet="abcdefghijklmnopqrstuvwxyz"
        for each in alphabet:
            if each not in sentence:
                return False
        return True
        
