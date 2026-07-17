class Solution:
    def isPalindrome(self, s: str) -> bool:

        def is_alpha_numeric(char: str) -> bool:
            return ( 
                "A" <= char <= "Z" or
                "a" <= char <= "z" or
                "0" <= char <= "9"
            )

        i, j = 0, len(s)-1

        while i < j:
            while i < j and not(is_alpha_numeric(s[i])):
                i += 1
            while i < j and not(is_alpha_numeric(s[j])):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        return True



                

        