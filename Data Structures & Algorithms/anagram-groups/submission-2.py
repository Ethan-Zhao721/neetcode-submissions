class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        map = defaultdict(list)

        # Read each string in the array and sorted:
        # then check if sorted String in the map: 
        #   if (sorted string in the map): Add real string into the result
        #   else: Add sorted String into the map.  

        for s in strs:            
            map[tuple(sorted(s))].append(s)
        
        return list(map.values())


           
                
