    def closeStrings(self, word1: str, word2: str) -> bool:
        m, n = len(word1), len(word2)
        c1, c2 = {},{}
        if ( m  == n ):
            # check whether they are the same set or not 
            for i in range(m):
                c1[word1[i]] = c1.get(word1[i],0) + 1
                c2[word2[i]] = c2.get(word2[i],0) + 1
            if ( set(c1) == set(c2) and sorted(c1.values()) == sorted(c2.values())):
                return True
        
        else:
            return False

# Pain in ass question, but I did it. 
# Time complexity, O(N)
# Space complexity O(N)
