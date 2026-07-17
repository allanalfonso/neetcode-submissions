class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        #s.replace(" ","") # remove whitespace
        alphanumerical_string = re.sub(r"[^a-zA-Z0-9]", "", s)
        clean_string = alphanumerical_string.lower()
        print(clean_string)

        i = 0                           #pointer 1
        j = len(clean_string)-1         #pointer 2

        while i <= j:
            if clean_string[i] != clean_string[j]:
                return False
            else:
                i += 1
                j -= 1

        return True