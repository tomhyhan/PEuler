class Solution:
    def minHeightShelves(self, books, shelfWidth) -> int:

        self.helper(0,0,books,shelfWidth)
        pass
    
    def helper(self, w, h, books, shelfWidth):
        if len(books) == 0:
            print(h)
            return
        
        current_book = books[0]
        w_c, w_h = current_book
        current_w = 


        self.helper(w+w_c, h+w_h, books[1:], shelfWidth)
        
        pass
    
s = Solution()
s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4)