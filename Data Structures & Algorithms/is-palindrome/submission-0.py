class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for c in s:
            if c.isalnum():
                string = string + c.lower()


        i = 0
        j = len(string)-1

        while(i<=j):
            if string[i] == string[j]:
                i += 1
                j -= 1
            else:
                return False


        return True