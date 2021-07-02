class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {"q":"_","w":"_","e":"_","r":"_","t":"_","y":"_","u":"_","i":"_","o":"_","p":"_","Q":"_","W":"_","E":"_","R":"_","T":"_","Y":"_","U":"_","I":"_","O":"_","P":"_"}
        row2 = {"a":"_","s":"_","d":"_","f":"_","g":"_","h":"_","j":"_","k":"_","l":"_","A":"_","S":"_","D":"_","F":"_","G":"_","H":"_","J":"_","K":"_","L":"_"}
        row3 = {"z":"_","x":"_","c":"_","v":"_","b":"_","n":"_","m":"_","Z":"_","X":"_","C":"_","V":"_","B":"_","N":"_","M":"_"}
        
        ret = []
        
        for word in words:
            fail = False
            if word[0] in row1:
                for char in word:
                    if char not in row1:
                        fail = True
            elif word[0] in row2:
                for char in word:
                    if char not in row2:
                        fail = True
            else: #word[0] in row3:
                for char in word:
                    if char not in row3:
                        fail = True
            if fail == False:
                ret.append(word)
                
        return ret
        
#runtime: O(n)
#memory: O(1)