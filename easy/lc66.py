## Plus one
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:


########### passed below, but slow ##################

#         if len(digits) == 1 and digits[0] == 9:
#             return [1,0]

#         c = (digits[-1] + 1) // 10
#         digits[-1] = (digits[-1] + 1) % 10
#         i =  len(digits)-2
#         while i > 0:
#             print(i,digits[i],c)
#             inplace = digits[i]+c
#             digits[i] = inplace % 10
#             c = inplace // 10
#             i -= 1

#         if digits[0] == 9 and c == 1:
#             digits[0] = 0
#             digits.insert(0, 1)
#         else:
#             digits[0] +=c

#         print(digits)
#         return digits


########### recursive ###########
        # if len(digits) == 0:
        #     digits = [1]
        # elif digits[-1] == 9:
        #     # print(digits[-1]+1)
        #     digits = self.plusOne(digits[:-1])
        #     digits.append(0)
        # else:
        #     digits[-1] +=1
        # return digits

########### iterative  97% ###########       
        count = 1
        for i in range(len(digits)-1, 0, -1):
            tmp = (digits[i]+count) % 10
            count = (digits[i]+count) // 10
            digits[i] = tmp
        # print(count)
        if (count + digits[0]) == 10:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[0] = digits[0] + count
        return digits
