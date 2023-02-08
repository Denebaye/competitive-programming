class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parents = {}
        ratios = {}
        
        def find(variable):
            if parents[variable] != variable:
                ratios[variable] *= ratios[parents[variable]]
                parents[variable] = find(parents[variable])
            return parents[variable]
        
        def union(var1, var2, value):
            root1 = find(var1)
            root2 = find(var2)
            if root1 != root2:
                parents[root1] = root2
                ratios[root1] = value * (ratios[var2] / ratios[var1])
        
        for (var1, var2), value in zip(equations, values):
            if var1 not in parents and var2 not in parents:
                parents[var1] = var2
                parents[var2] = var2
                ratios[var1] = value
                ratios[var2] = 1.0
            elif var1 in parents and var2 in parents:
                union(var1, var2, value)
            elif var1 in parents and var2 not in parents:
                root1 = find(var1)
                parents[var2] = root1
                ratios[var2] = 1 / value * ratios[var1]
            elif var1 not in parents and var2 in parents:
                root2 = find(var2)
                parents[var1] = root2
                ratios[var1] = value * ratios[var2]
                
        results = []
        for var1, var2 in queries:
            if var1 not in parents or var2 not in parents:
                results.append(-1.0)
                continue
            root1 = find(var1)
            root2 = find(var2)
            if root1 != root2:
                results.append(-1.0)
            else:
                results.append(ratios[var1] / ratios[var2])
                
        return results
