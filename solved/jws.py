import pprint

class Tree:
    def __init__(self) -> None:
        self.root = {}
        self.endsymbol = '*'
        
    def save(self, words):
        for word in words:
            tree = self.root
            for char in word:
                if char not in tree:
                    tree[char] = {}
                if self.endsymbol not in tree:
                    tree[self.endsymbol] = 0 
                tree[self.endsymbol] += 1
                tree = tree[char]
            if self.endsymbol not in tree:
                tree[self.endsymbol] = 0
            tree[self.endsymbol] += 1
            
    def find(self, word):
        time = 0
        tree = self.root
        for char in word:
            if tree[self.endsymbol] == 1:
                return time
            tree = tree[char]
            time += 1
            
        return time
    
def solution(words):
    tree = Tree()
    tree.save(words)
    pprint.pprint(tree.root)
    # total_time = 0
    # for word in words:
    #     total_time += tree.find(word)
    
    # print(total_time)
    # return total_time


# from collections import defaultdict

# class Trie:
#     def __init__(self):
#         self.root = defaultdict(int)
#         self.num = "#"

#     def insert(self, word):
#         current = self.root
#         for ch in word:
#             if ch not in current:
#                 current[ch] = defaultdict(int)
#             current[self.num] += 1
#             current = current[ch]
#         current[self.num] += 1

#     def search(self, word):
#         current = self.root
#         cnt = 0
#         for ch in word:
#             if current[self.num] == 1:
#                 return cnt
#             current = current[ch]
#             cnt += 1
#         return cnt

# def insert_words(trie, words):
#     for word in words:
#         trie.insert(word)

# def cnt_types(trie, words):
#     cnt = 0
#     for word in words:
#        cnt += trie.search(word) 
#     return cnt 
    
# def solution(words):
#     trie = Trie()
#     insert_words(trie, words)
#     print(trie.root['g'])
#     return cnt_types(trie,words)

solution(["go","gone","guild"])
# solution(["abc","def","ghi","jklm"])
# solution(["word","war","warrior","world"])


class Tree:
    def __init__(self) -> None:
        self.root = {}
        self.endsymbol = '*'
        
    def save(self, words):
        for word in words:
            tree = self.root
            for char in word:
                if char not in tree:
                    tree[char] = {}
                    tree[f"{char}cnt"] = 0     
                tree[f"{char}cnt"] += 1
                tree = tree[char]
            tree[self.endsymbol] = word
            
    def find(self, word):
        time = 0
        tree = self.root
        for char in word:
            time += 1
            if tree[f"{char}cnt"] == 1:
                return time
            tree = tree[char]
            
        return time
    
def solution(words):
    tree = Tree()
    tree.save(words)
    pprint.pprint(tree.root)
    # total_time = 0
    # for word in words:
    #     total_time += tree.find(word)
    
    # print(total_time)
    # return total_time

solution(["go","gone","guild"])
