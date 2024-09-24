class Solution:
    # reverse half number
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        if x < 10:
            return True

        reversed_half = 0
        while x > reversed_half:
            remainder = x % 10
            reversed_half = reversed_half * 10 + remainder
            x //= 10

        return x == reversed_half or x == (reversed_half // 10)

    # reverse all number
    # def isPalindrome(self, x: int) -> bool:
    #     if x < 0:
    #         return False

    #     if x < 10:
    #         return True
        
    #     tmp_x = x
    #     reversed_number = 0

    #     while (tmp_x > 0):
    #         digit = tmp_x % 10
    #         tmp_x = tmp_x // 10
    #         reversed_number = reversed_number * 10 + digit

    #     if x < 0:
    #         reversed_number *= -1
        
    # return x == reversed_number

        