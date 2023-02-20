class Solution:
    def expressiveWords(self, original_string: str, words: List[str]) -> int:
        def compress(s):  
            compressed_arr = []
            count = 0
            last_char = s[0]
            for c in s:
                if c == last_char:
                    count += 1
                else:
                    compressed_arr.append((last_char, count))
                    count = 1
                last_char = c

            compressed_arr.append((last_char, count))
            return compressed_arr

        def test(word, compressed_original):
            compressed_word = compress(word)
            if len(compressed_word) != len(compressed_original): 
                return False  
            for i in range(len(compressed_word)):
                if compressed_original[i][0] != compressed_word[i][0]: 
                    return False  
                if not (compressed_original[i][1] == compressed_word[i][1] or compressed_original[i][1] >= max(3, compressed_word[i][1])):
                    return False
            return True

        compressed_original = compress(original_string)
        output = 0
        for word in words:
            if test(word, compressed_original):
                output += 1
        return output
