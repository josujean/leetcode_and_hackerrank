class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x_sign = -1
            x_new = str(x)[1:]
        else:
            x_sign = 1
            x_new = str(x)

        x_new = x_sign * int(x_new[::-1])
        if abs(x_new) > 2**31:
            return 0
        else:
            return x_new
