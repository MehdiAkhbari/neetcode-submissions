class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for i, word in enumerate(strs):
            letters = [0] * 26
            for ch in word:
                letters[ord(ch) - ord('a')] += 1

            if tuple(letters) in hashmap:
                hashmap[tuple(letters)].append(word)
            else:
                hashmap[tuple(letters)] = [word]

        # print(hashmap.values())
        return(list(hashmap.values()))

                

            
            