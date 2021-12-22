class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        finding distance to the 
        question may be I may sort the points based on it 
        I have k given so that in how many iterations I can get the closest points to origin 
        may be I need also index for the array
        I am thinking I may need an empty array so that I can append the closest points 
        finally one of friend came up with the idea there's a way to sort based on keys like distance in 
        my case that's lambda function. 
        """
        points.sort(key = lambda elm: elm[0]**2 + elm[1]**2 )
        closest_Points = []
        for i in range(0,k):
            closest_Points.append(points[i])
        return closest_Points    