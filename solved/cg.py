
def solution(cookie):

    psum = [0] * (len(cookie) + 1)
    
    for i in range(1, len(cookie) + 1):
        psum[i] = psum[i-1] + cookie[i-1]
    
    max_possible = sum(cookie) // 2
    largest = 0 

    for mid in range(1, len(cookie)):
        left = mid
        right = mid + 1
        
        while left >= 0 and right <= len(cookie):
            
            left_sum = psum[mid] - psum[left-1]
            right_sum = psum[right] - psum[mid]
            
            if left_sum == right_sum:
                largest = max(largest, left_sum)     
                if left_sum == max_possible:
                    return max_possible
            
            if left_sum > right_sum:
                right += 1
            else:
                left -= 1          

    return largest

solution([1,1,2,3])
solution([1,2,4,5])