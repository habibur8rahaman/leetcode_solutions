class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list)

        for item in strs:
            count = [0]*26

            for char in item:
                count[ord(char) - ord('a')] += 1

            hashmap[tuple(count)].append(item)
        return list(hashmap.values())
        
