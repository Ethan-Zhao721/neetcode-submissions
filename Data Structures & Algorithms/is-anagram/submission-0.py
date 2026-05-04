class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
        arr1 = [0] * 26 
        arr2 = [0] * 26

        for i in s:
            arr1[ord(i)- ord('a')]+=1
        for j in t:
            arr2[ord(j)-ord('a')]+=1
        
        for index, val in enumerate(arr1):
            if arr1[index] != arr2[index]:
                return False

        return True

