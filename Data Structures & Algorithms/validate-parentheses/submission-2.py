class Solution:
    def isValid(self, s: str) -> bool:
        
        """ Translate
            Determine whether a string has a valid open and close bracket sequence
        """

        """ Requirements 
            The string is valid if it passes all three rules
            1. every open bracket is closed by the same type of close bracket
            2. open brackets are closed in the correct order
            3. every close bracket has a corresponding open bracket of the same type
        """

        """ Approach 
            Push all the open brackets to a Stack and verify the closing brackets by popping from the stack.
            This way, the last open bracket must match the first closing bracket.
            We determine it's invalid if the bracket doesn't match.
            Additionally, the string is invalid if it's an odd number, given that every open bracket must be closed.
            Lastly, the string is only valid when we've popped every valid element from the stack and there is nothing left in the string.
        """

        """ Code 
            if isOdd(len(s))
                return false
            
            m1 = deque()

            for bracket in s:
                
                if isOpen(bracket):
                    m1.append(bracket)
                else:
                    next = m1.pop()
                    if !isValid(bracket, next):
                        return false
                    
            if m1.empty:
                return true
            else:
                return false

            def isOpen(b):

                return b == '(' or b == '[' or b == '{'
            
            def isValid(b1, b2):

                if b1 == '(':
                    return b2 == ')'
                if b1 == '[':
                    return b2 == ']'
                if b1 == '{':
                    return b2 == '}'
                
                return false
        """ 

        """ Efficiency
        """

        # if len(s) % 2 != 0:
        #     return False
            
        m1 = deque()

        for bracket in s:
            
            if self.isOpenBracket(bracket):
                m1.append(bracket)
            else:
                if len(m1) == 0:
                    return False
                open_bracket = m1.pop()
                if not self.isValidBracket(open_bracket, bracket):
                    return False
                    
        if len(m1) == 0:
            return True
        else:
            return False

    def isOpenBracket(self, b):

        return b == '(' or b == '[' or b == '{'
    
    def isValidBracket(self, b1, b2):

        if b1 == '(':
            return b2 == ')'
        if b1 == '[':
            return b2 == ']'
        if b1 == '{':
            return b2 == '}'
        
        return False

