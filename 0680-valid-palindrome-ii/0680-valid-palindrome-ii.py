class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(s) - 1  # Initialize pointers at both ends of the string

        # Iterate while the two pointers don't cross each other
        while left < right:
            # If the characters at the current pointers don't match
            if s[left] != s[right]:
                # Check for palindrome by removing one character - either from the left or right
                # If either case returns true, the function returns true
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            # Move both pointers towards the center
            left, right = left + 1, right - 1

        # If the string is a palindrome or can be made into one by removing a single character
        return True