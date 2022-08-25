class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_dict = {}
        for char in s:
            freq_dict[char] = freq_dict.get(char, 0) + 1
        
        maxPalindromeLength = 0
        isOddFreq = False
        for char, freq in freq_dict.items():
            maxPalindromeLength += freq
            if freq & 1:
                maxPalindromeLength -= 1
                isOddFreq = True
                
        maxPalindromeLength += 1 if isOddFreq else 0
        return maxPalindromeLength
            
        