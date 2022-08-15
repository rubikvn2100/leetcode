class Solution
    def isValid(self, s str) - bool
        stack = []
        braket_dict = {'(' ')', '[' ']', '{' '}'}
        
        for braket in s
            if braket in braket_dict
                stack.append(braket)
            else
                if len(stack) == 0
                    return False
                
                if stack[-1] not in braket_dict
                    return False
                
                if braket != braket_dict[stack[-1]]
                    return False
                
                stack.pop()
                
        if len(stack) != 0
            return False
        
        return True 