#User function Template for python3

class Solution:
    
    def getrightchild(self,i):
        return (i*2) + 2
    def getleftchild(self,i):
        return (i*2) + 1
    def getparent(self,i):
        return (i - 1)//2
    #Heapify function to maintain heap property.
    
    def heapify(self,arr, n, i):
        self.upheap(arr,n,i)
        self.downheap(arr,n,i)
        
    def upheap(self,arr,n,i):
        
        if i == 0:return
    
        p = self.getparent(i)
        if arr[i] < arr[p]:
            arr[i],arr[p] = arr[p],arr[i]
            
            self.upheap(arr,n,p)
            
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n):
            self.upheap(arr,n,i)
        
    #Function to sort an array using Heap Sort.   
    def remove(self,arr,n,i):
        arr[i],arr[n - 1] = arr[n - 1],arr[i]
        self.heapify(arr,n - 1,i)
            
    def downheap(self,arr,n,i):
        if i >= n:return
    
        l = self.getleftchild(i)
        r = self.getrightchild(i)
        if l >= n: return
        if l < n and r >= n:
            if arr[i] > arr[l]:
                arr[i],arr[l] = arr[l],arr[i]
            return 
        
        if arr[i] <= arr[l] and arr[i] <= arr[r]:return
    
        if arr[r] > arr[l]:
            arr[l],arr[i] = arr[i],arr[l]
            i = l
        else:
            arr[i],arr[r] = arr[r],arr[i]
            i = r
        self.downheap(arr,n,i)
        
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n):
            self.remove(arr,n - i,0)
        arr.reverse() 