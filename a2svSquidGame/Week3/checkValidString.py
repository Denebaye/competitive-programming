class Solution:
    def checkValidString(self, string):
        if not string:
            return True
        
        left_parenthesis = '(*'
        right_parenthesis = ')*'

        length = len(string)
        dp = [[False] * length for _ in string]
        for i in range(length):
            if string[i] == '*':
                dp[i][i] = True
            if i < length-1 and string[i] in left_parenthesis and string[i+1] in right_parenthesis:
                dp[i][i+1] = True

        for size in range(2, length):
            for i in range(length - size):
                if string[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif string[i] in left_parenthesis:
                    for k in range(i+1, i+size+1):
                        if (string[k] in right_parenthesis and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]
