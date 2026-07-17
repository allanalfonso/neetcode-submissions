class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmap1 = {}
        hashmap2 = {}

        for char1 in s:
            if char1 in hashmap1:
                hashmap1[char1] += 1
            else:
                hashmap1[char1] = 1

        for char2 in t:
            if char2 in hashmap2:
                hashmap2[char2] += 1
            else:
                hashmap2[char2] = 1
        
        print(list(hashmap1.values()))
        print(list(hashmap2.values()))

        if hashmap1 == hashmap2:
            return True
        else:
            return False