# Brief
# Given an integer x, return true if x is a palindrome, and false otherwise.

# Solution
def isPalindrome(x):
        stringX = str(x)
        if stringX == stringX[::-1]:
            return True
        else:
            return False