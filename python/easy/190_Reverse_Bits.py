class Solution:
    def reverseBits(self, n: int) -> int:
        #convert to binary string
        bin_str = bin(n)[2:].zfill(32)
        #reverse binary string
        bin_str = bin_str[::-1]
        #convert binary string to int
        return int(bin_str, 2)