class Solution():
    def isValid(self, s):

    
        stack = []
        counter_round = 0   # счетчик для ()
        counter_square = 0  # счетчик для []
        counter_curly = 0   # счетчик для {}

        for i in s:
            if i == "(":
                stack.append(i)
                counter_round += 1
            elif i == ")":
                counter_round -= 1
                if counter_round < 0 or not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif i == "[":
                stack.append(i)
                counter_square += 1
            elif i == "]":
                counter_square -= 1
                if counter_square < 0 or not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif i == "{":
                stack.append(i)
                counter_curly += 1
            elif i == "}":
                counter_curly -= 1
                if counter_curly < 0 or not stack or stack[-1] != "{":
                    return False
                stack.pop()
        
        if counter_round != 0 or counter_square != 0 or counter_curly != 0:
            return False
        
        return True if not stack else False

if __name__ == "__main__":
    sol = Solution()
       


            