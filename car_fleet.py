class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        time = [0] * len(pos)
        pos_time = []
        for i in range(len(pos)):
            time[i] = (target - pos[i])/speed[i]
        
        #print(time)
        for p,t in zip(pos,time):
            pos_time.append([p,t])
        pos_time.sort()
        #print(pos_time)
        stack = []   
        for i in range(len(pos)):
            while stack and pos_time[i][1] >= stack[-1]:
                stack.pop()
            stack.append(pos_time[i][1])
            
        return len(stack)    
            