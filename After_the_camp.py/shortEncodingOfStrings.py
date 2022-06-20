class TrieNode:
    
    def __init__(self):
        self.kids = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        
        for c in word:
            if c not in node.kids:
                node.kids[c] = TrieNode()
            node = node.kids[c]
        
    
    def find(self,word):
        node = self.root
        
        for c in word:
            if c not in node.kids:
                return False
            node = node.kids[c]
        
        return True
    
class Solution:
    def reverseWord(self,word):
        return word[::-1]
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = sorted(words,reverse = True,key = lambda x : len(x))
        T = Trie()
        outPut = 0
        for word in words:
            N = len(word)
            temp = self.reverseWord(word)
            if not T.find(temp):
                outPut += N + 1
                T.insert(temp)
        
        return outPut
                
                
        
        
        