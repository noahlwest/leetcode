class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        #get a list of product strings
        products = []

        num_i_zeroes = 0
        for i in range(len(num1)-1, -1, -1):
            curr_product = 0
            num_j_zeroes = 0
            for j in range(len(num2)-1, -1, -1):
                curr_product += int(num1[i]) * int(num2[j]) * (10**(num_i_zeroes + num_j_zeroes))
                num_j_zeroes += 1
                
            products.append(curr_product)
            num_i_zeroes += 1

        #combine the product strings
        ret = 0
        for product in products:
            ret += product
            
        return str(ret)