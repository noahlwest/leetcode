class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #basic idea: "move" up and down while appending to each row.
        #at the end, join all rows into a string.
        
        row_counter = -1
        reverse = False
        
        ret_lists = [[] for i in range(0, numRows)]
        
        for char in s:
            if reverse == True:
                row_counter -= 1
            else:
                row_counter += 1

            if row_counter < 0:
                row_counter += 1
            if row_counter > numRows-1:
                row_counter -= 1
                
            ret_lists[row_counter].append(char)
            
            if row_counter == numRows-1:
                reverse = True
            if row_counter == 0:
                reverse = False
            
        #combine the lists and create the string
        str_list = []
        for i in range(0, numRows):
            str_list = str_list + ret_lists[i]
            
        ret_str = "".join(str_list)
            
        return ret_str
        
#runtime: O(n)
#memory: O(n)
