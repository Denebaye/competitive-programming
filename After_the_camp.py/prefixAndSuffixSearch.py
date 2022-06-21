class TrieNode:
    def __init__(self):
        self.kids = {}
        self.index = -1
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word,index):
        node = self.root
        node.index = index
        
        for c in word:
            if c not in node.kids:
                node.kids[c] = TrieNode()
            node = node.kids[c]
            node.index = index
       
    def find(self,prefix,suffix):
        temp = suffix + "#" + prefix
        node = self.root
        for c in temp:
            if c not in node.kids:
                return -1
            node = node.kids[c]
        
        return node.index
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.T = Trie()
        for index,word in enumerate(self.words):
            N = len(word)
            temp = word + "#" + word
            for i in range(N):
                self.T.insert(temp[i:],index)              

    def f(self, prefix: str, suffix: str) -> int:
        return self.T.find(prefix,suffix)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)