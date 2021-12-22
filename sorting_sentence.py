class Solution:
    def sortSentence(self, s: str) -> str:
        """
        example we are at a2sv lab" 
        to shuffle this sentence
        
        - we have 1-indexed word position "we",
          "we" assigned the number 1 and "are" assigned a number 2, "at" = 3, "a2sv" = 4,"lab" =            5.       
        
        1- "lab5 we1 at3 a2sv4 are2" this can be taken as a shuffled sentence
        2- "at3,a2sv4,we1,are2,lab5"       
       
      as a solution the numbers can help to reconstruct the original sentence
      to access the numbers and separate them from each word 
           
      1- first we separate each word using "split" built in method in python.
      2- secondly we access the numbers using their index which is the last one we don't have to 
         traverse each character other than the last index because as it's given the numbers              are found at the last position of the index,so to get them in integer form we subtr-            act their ASCII value with the ASCII value of zero.Finally we creat a dictionary                using the numbers as a key and removing(or poping out the number after having them).
         
         problems I faced during solving this problem 
       1- I tried to find built-in function to remove the last element from the array of string
          at last I found a replace().
        
      """
        shuf_Sent = s.split()
        Dict = {}
        orig_Sent = []
        for word in shuf_Sent:
            index = int(word[-1])
            word = word[:-1]
            Dict[index] = word
            
        for i in range(1,len(Dict) + 1):            
            orig_Sent.append(Dict[i])
                    
        return " ".join(orig_Sent)   
                
        
        