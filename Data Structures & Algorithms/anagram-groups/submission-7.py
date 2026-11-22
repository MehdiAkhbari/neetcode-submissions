# Idea: Create a hashmap whose keys is the frequency of letters from (a-z) a tuple of length 26 for each word, and its values include a list of words with those keys.
# we need to use tuple for keys as keys can't be lists!
# for each word:
# if letters are already in the hashmap keys => append the word to the corresponding values
# otherwise, add a new element to the hashamp with the new key and word 


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

        return(list(hashmap.values()))

                

            
            