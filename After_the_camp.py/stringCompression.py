class Solution(object):
    def compress(self, chars):
        writer = 0
        reader1 = 0
        while reader1 < len(chars):
            reader2 = reader1
            while reader2 < len(chars) and chars[reader2] == chars[reader1]:
                reader2 +=1
            
            chars[writer] = chars[reader1]
            writer +=1
            if reader2 - reader1 > 1:
                String = str(reader2 - reader1)
                for s in String:
                    chars[writer] = s
                    writer +=1
            
            reader1 = reader2
        
        return writer
                
# time and space complexity
# time O(n) time complexity
# space = O(1)
