
class Solution:
    def minHeightShelves(self, books, shelfWidth) -> int:
        memo = {}
        min_height = self.helper(0,0,books,shelfWidth,0,memo)
        print(memo)
        print("min_t", min_height)
        return min_height
    
    def helper(self, w, h, books, shelfWidth, book_i, memo):
        key = (book_i, h, w)
        if len(books) == book_i:
            return h
        elif key in memo :
            return memo[key]
        
        current_book = books[book_i]
        w_b, h_b = current_book

        w_current = w + w_b 
        min_height = float("inf")
        if w_current <= shelfWidth:
            h_current = max(h, h_b)
            c_1 = self.helper(w_current, h_current, books, shelfWidth, book_i+1, memo)
            min_height = min(min_height, c_1)

        c_2 = self.helper(w_b, h_b, books, shelfWidth, book_i+1, memo) + h

        min_height = min(min_height, c_2)
        memo[key] = min_height 
        return min_height


s = Solution()
s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4)
# s.minHeightShelves(books = [[1,3],[2,4],[3,2]], shelfWidth = 6)