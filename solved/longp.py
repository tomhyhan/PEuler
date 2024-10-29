def palin_len(s, left, right):
    plen = 0
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        
        plen += 2
        left -= 1
        right += 1
    return plen

def solution(s):
    
    max_plen = 1
    for i in range(1, len(s)-1):
        odd_palin_len = palin_len(s, i-1, i+1) + 1
        even_palin_len = palin_len(s, i-1, i)

        max_plen = max(max_plen, odd_palin_len, even_palin_len)
    
    even_palin_len = palin_len(s, len(s)-2, len(s)-1)
    return max(max_plen, even_palin_len )

def manacher(s):
    # Transform S into T
    T = '#'.join(f'^{s}$')
    n = len(T)
    P = [0] * n
    C = R = 0

    for i in range(1, n - 1):
        P[i] = (R > i) and min(R - i, P[2 * C - i])  # Use previously computed values
        print("T[i]", T[i])
        print("deff", R-i , P[2 * C - i])
        print("P[i]", P[i])
        # Attempt to expand palindrome centered at i
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # If the expanded palindrome is beyond R, adjust center C and right edge R
        if i + P[i] > R:
            C, R = i, i + P[i]
        print(C,R)
    # Find the maximum element in P
    max_len, center_index = max((n, i) for i, n in enumerate(P))
    start = (center_index - max_len) // 2  # Index in the original string
    return s[start:start + max_len]

# Example usage:
print(manacher("bbbb"))  # Output: "abba"


solution("abcdcba")