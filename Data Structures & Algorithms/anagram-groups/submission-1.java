class Solution {
    
    
    public List<List<String>> groupAnagrams(String[] strs) {
        // Read each string in the array and sorted:
        // then check if sorted String in the map: 
        //     if (sorted string in the map): Add real string into the result
        //     else: Add sorted String into the map.  
        Map<String, List<String>> map = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars); // canonical form

            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }

    public String sortString(String str){
        char[] chars = str.toCharArray();
        Arrays.sort(chars);               
        return new String(chars);
        
    }
}
