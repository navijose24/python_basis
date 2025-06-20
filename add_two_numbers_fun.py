"""
Given two integers num1 and num2, return the sum of the two integers.

Example 1:

Input: num1 = 12, num2 = 5
Output: 17
Explanation: num1 is 12, num2 is 5, and their sum is 12 + 5 = 17, so 17 is returned.

Constraints:

    -100 <= num1, num2 <= 100

"""
def add(num1,num2):
    if -100 <= num1 and num2 <= 100:
        return num1 + num2
    else:
        return "Error: Input numbers are out of range"
print(add(12,5))  # Output: 17
