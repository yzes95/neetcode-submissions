class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s.lower())
        t = sorted(t.lower())
       # s = sorted(s, key = lambda x : x[0])
       # t = sorted(t, key = lambda x : x[0])
       # for s_ele,t_ele in zip(s,t):
            #if s_ele != t_ele:
                #return False
        #else:
             #return True
        return s == t 
    