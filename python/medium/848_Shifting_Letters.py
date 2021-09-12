class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        s_list = list(s)
        
        curr_shifts = 0
        for i in range(len(s_list)-1, -1, -1):
            curr_shifts += shifts[i]
            s_list[i] = letters[((ord(s_list[i]) - ord('a')) + curr_shifts) % 26]
                
        return "".join(s_list)
                

    #runtime: O(n)
    #memory: O(1)