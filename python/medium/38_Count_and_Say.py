class Solution:
    def countAndSay(self, n: int) -> str:
           
        string = "1"
        
        for i in range(1, n):
            output = []
            curr_char = string[0]
            curr_count = 0
            for i in range(0, len(string)):
                if string[i] != curr_char:
                    output.append(str(curr_count))
                    output.append(curr_char)
                    curr_char = string[i]
                    curr_count = 1
                else:
                    curr_count += 1

                if i == len(string)-1:
                    output.append(str(curr_count))
                    output.append(curr_char)
                    string = "".join(output)
        
        return string
        