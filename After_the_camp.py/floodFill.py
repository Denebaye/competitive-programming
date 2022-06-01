class Solution:
    def dfs(self,image,sr,sc,newColor,visited):
        visited.add((sr,sc))
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        
        directions = [(sr - 1,sc),(sr + 1,sc),(sr,sc - 1),(sr,sc + 1)]
        for dir in directions:
            
            if dir not in visited and (dir[0] < len(image)) and (dir[1] < len(image[0])) and (dir[1] >=0) and (dir[0] >= 0)and image[dir[0]][dir[1]] == oldColor:
    
                self.dfs(image,dir[0],dir[1],newColor,visited)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        mySet = set()
        self.dfs(image,sr,sc,newColor,mySet)
        return images