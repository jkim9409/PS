#Example 1: input = strs = ["eat","tea","tan","ate","nat","bat"]
#           output = [["bat"],["nat","tan"],["ate","eat","tea"]]

#Example 2: input = str = [""]
#           output = [[""]]

#Eample 3: input = ["a"]
#           output = [["a"]]

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
import collections

def groupAnagrams( strs: [str]) -> [[str]]:
    import collections
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)

    return list(anagrams.values())

#comment: ㅇ0ㅇ?? for now, focus on the fact that list(anagrams.values()) will return the list of values of the dictionary

class Solution:
    def groupAnagrams_mysolution(self,strs:[str]) -> [[str]]:
        result = {}
        for word in strs:
            group = tuple(sorted(word))
            if group in result:
                result[group].append(word)
            else:
                result[group] = []
                result[group].append(word)
        return list(dict.values(result))

# comment: using tuple for the dictionary key



input1 = ["eat","tea","tan","ate","nat","bat"]
input2 = [""]
input3 = ["a"]
print(groupAnagrams(input1))
print(groupAnagrams(input2))
print(groupAnagrams(input3))
print(Solution().groupAnagrams_mysolution(input1))
print(Solution().groupAnagrams_mysolution(input2))
print(Solution().groupAnagrams_mysolution(input3))

