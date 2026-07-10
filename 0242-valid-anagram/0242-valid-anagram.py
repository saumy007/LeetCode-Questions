class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        if len(s) == len(t):
            for st in s:
                if st in seen1:
                    seen1[st] += 1
                else:
                    seen1[st] = 1
            
              
            for st in t:
                if st in seen2:
                    seen2[st] += 1
                else:
                    seen2[st] = 1
            if seen1 == seen2:
                return True
        if len(s) != len(t):
            return False

        
        return False
