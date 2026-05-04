class Solution {
    
    
    public List<List<String>> groupAnagrams(String[] strs) {
        // Read each string in the array and sorted:
        // then check if sorted String in the map: 
        //     if (sorted string in the map): Add real string into the result
        //     else: Add sorted String into the map.  
        Map<String, Integer> map = new HashMap<>();
        List<List<String>> res = new ArrayList<>();        
        for(String str : strs){
            String sortedStr = sortString(str);
            if(map.containsKey(sortedStr)){
                int index = map.get(sortedStr);
                res.get(index).add(str);                
            }else{
                List<String> l = new ArrayList<>();
                l.add(str);
                res.add(l);
                map.put(sortedStr, map.size());
                // currIndex++;
            }
        }
        return res;
    }

    public String sortString(String str){
        char[] chars = str.toCharArray();
        Arrays.sort(chars);               
        return new String(chars);
        
    }
}
