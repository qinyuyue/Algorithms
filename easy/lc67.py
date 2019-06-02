# Binary Add
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Algorithm
        1. cast two string to same length by adding 0 ahead
        2. initialize an indicator = 0,
            for i from len(a) to -1
                sum up same position
        """
#         ## cast length
#         n = len(a)
#         m = len(b)
#         if n >= m:
#             b = '0' * (n-m) + b
#         else:
#             a = '0' * (m-n) + a

#         ## sum operation
#         output = []
#         count = 0
#         for i in range(len(a)-1, -1, -1):
#             sums = int(a[i]) + int(b[i]) + count
#             count = sums // 2
#             sums = sums % 2
#             output.insert(0, str(sums))
#         if count == 1:
#             output.insert(0, str(1))
#         return (''.join(output))

        return bin(int(a, 2) + int(b, 2)).replace('0b', '')
