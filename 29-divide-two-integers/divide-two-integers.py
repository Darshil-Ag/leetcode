class Solution(object):
    def divide(self, dividend, divisor):
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        while abs_dividend >= abs_divisor:
            temp = abs_divisor
            multiple = 1
            while abs_dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
                
            abs_dividend -= temp
            quotient += multiple
            
        quotient *= sign
        
        if quotient < MIN_INT:
            return MIN_INT
        if quotient > MAX_INT:
            return MAX_INT
            
        return quotient