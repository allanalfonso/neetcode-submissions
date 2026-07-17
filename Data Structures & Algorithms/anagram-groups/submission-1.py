class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = defaultdict(list) # mapping charCount to list of Anagrams

        for word in strs:
            letter_count_array = [0] * 26 # a ... z

            for char in word:
                letter_count_array[ord(char) - ord("a")] += 1

            result[tuple(letter_count_array)].append(word)

        return list(result.values())
