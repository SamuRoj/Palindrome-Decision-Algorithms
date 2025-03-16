from collections import deque

def two_pointers(s):
    l, r = 0, len(s) - 1            # O(1)
    isPalindrome = True             # O(1)
    while l < r and isPalindrome:   # O(n/2) Breaks just in the half of the string
        if s[l] != s[r]:            # O(1)
            isPalindrome = False    # O(1)
        l += 1                      # O(1)
        r -= 1                      # O(1)
    return isPalindrome             # O(1)

# Best Base: O(1) The string is not a palindrome
# Worst Case: O(n/2) The string is a palindrome

def reverse_string(s):
    reversed = s[::-1]              # O(n)
    for i in range(len(s)):         # O(n)
        if s[i] != reversed[i]:     # O(1)
            return False            # O(1)
    return True                     # O(1)

# Best Base: O(n) Even if the string is not a palindrome the string is reversed
# Worst Case: O(n) The string is a palindrome

def recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return recursive(s[1:-1])

# Best Base: O(n) If the first character is different. 
# Worst Case: O(n) The string is a palindrome

def stack(s):   
    stack = deque()             # O(1)
    n = len(s)                  # O(1)
    i = 0                       # O(1)
    while i < n // 2:           # O(n/2)
        stack.append(s[i])      # O(1)
        i += 1                  # O(1)
    if n % 2 != 0:              # O(1)
        i += 1                  # O(1)
    while i < n:                # O(n/2)
        char = stack.pop()      # O(1)
        if char != s[i]:        # O(1)
            return False        # O(1)
        i += 1                  # O(1)
    return True                 # O(1)

# Best Base: O(n/2) The stack is already made and the first char of comparison is different 
# Worst Case: O(n) The string is a palindrome
