class Solution:
    def fib(self, n: int) -> int:
        my_dict = {}
        def fibe(n,my_dict):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n in my_dict.keys():
                return my_dict[n]
            my_dict[n] = fibe(n - 1,my_dict) + fibe(n - 2,my_dict)
            return my_dict[n]
        return fibe(n,my_dict)