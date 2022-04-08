class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "*":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(str(y * x))
            elif tokens[i] == "/":
                x = int(stack.pop())
                y = int(stack.pop())
                val = y/x
                if val < 0: 
                    val = floor(abs(val))
                    stack.append(str(-val))
                else:
                    stack.append(str(floor(val)))
            elif tokens[i] == "-":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(str(y - x))
            elif tokens[i] == "+":
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(str(y + x))
            else:
                stack.append(tokens[i])
        # print(stack)   
        return int(stack[0])
# time and space complexity
# time = O(n) 
# space = O(n)
                