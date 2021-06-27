class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        index1 = len(num1)-1
        index2 = len(num2)-1
        ret = ""
        carryout = 0
        while index1 >= 0 or index2 >= 0:
            if index1 >= 0 and index2 >= 0:
                num = ord(num1[index1])-48 + ord(num2[index2])-48 + carryout
            elif index1 >= 0:
                num = ord(num1[index1])-48 + carryout
            else:
                num = ord(num2[index2])-48 + carryout
            carryout = num // 10
            num = num % 10
            ret = str(num) + ret
            index1 -= 1
            index2 -= 1
        if carryout > 0:
            ret = str(carryout) + ret
        return ret

#runtime: O(n)
#memory: O(1)