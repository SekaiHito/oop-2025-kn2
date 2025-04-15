n = int(input())
hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
digit_sum = hundreds + tens + ones
print(digit_sum) 