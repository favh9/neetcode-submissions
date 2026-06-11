class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ Translate
        A palindrome is a string that reads the same forward and backward.
        Ignores non-aplhanumeric characters and is case-insensitive.
        """

        """ Requirements / Output, Input, and Constraints
        Output: True or False
        Input: str
        The given string is made up of all printable ASCII characters.
        Its length is between 1 and 1000 (inclusive)
        """

        """ Approach / Methods and Observations
        1st: 
        Use two pointers that iterate the string, one that starts at the beginning and another at the end.
        No need for extra space so no additional data structures are used

        When do we know when the string is a Palindrome?
            when the string is 1 character
            when the left pointer crosses the right pointer, or viceversa
        When do we know it's not a palindrome?
            when the left pointer's character is valid but does not match the right pointer, or viceversa
        """

        """ Code / Pseudocode
        1st Approach:
        
        left = 0 
        right = len(s)-1

        WHILE left_index <= right_index
            
            WHILE left_index < right_index AND left_char is invalid
                left_index++
            
            WHILE right_index = left_index AND right_char is invalid 
                right_index--

            IF left_char != right_char
                return False
            
            right_index--
            left_index++
            
        return True
        """
        s = s.lower()

        left_index = 0
        right_index = len(s)-1

        while left_index < right_index:

            while left_index < right_index and not self.isAlphaNum(s[left_index]):
                left_index += 1
            while right_index > left_index and not self.isAlphaNum(s[right_index]):
                right_index -= 1
            
            if s[left_index] != s[right_index]:
                return False

            right_index -= 1
            left_index += 1

        return True

    def isAlphaNum(self, c: str) -> bool:

        # ascii code range for numbers: 48 - 57 inclusive (0-9)
        # ascii code range for letters: 
            # 65 - 90 inclusive (A-Z)
            # 97 - 122 inclsuive (a-z)
        
        num_min = ord('0')
        num_max = ord('9')
        upper_letter_min = ord('A')
        upper_letter_max = ord('Z')
        lower_letter_min = ord('a')
        lower_letter_max = ord('z')
        
        ascii_s = ord(c)

        # numbers
        if ascii_s >= num_min and ascii_s <= num_max:
            return True
        # uppercase letters
        if ascii_s >= upper_letter_min and ascii_s <= upper_letter_max:
            return True
        # lowercase letters
        if ascii_s >= lower_letter_min and ascii_s <= lower_letter_max:
            return True
        
        return False




        