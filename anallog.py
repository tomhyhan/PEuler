def solution(h1, m1, s1, h2, m2, s2):
    t1 = h1 * 60 * 60 + m1 * 60 + s1
    t2 = h2 * 60 * 60 + m2 * 60 + s2
    
    s = s1
    cnt = 0
    h = t1
    m = m1 * 60 + s1
    while t1 < t2:

        h_view_t = h / 12 / 60
        m_view_t = m / 60
        
        h = (h + 1) 
        m = (m + 1) 
        
        nh_view_t = h / 12 / 60
        nm_view_t = m / 60
        ns = s + 1
        
        if s <= h_view_t < ns and s <= nh_view_t < ns:
            cnt += 1
        if s <= m_view_t < ns and s <= nm_view_t < ns:
            cnt += 1
        
        if h_view_t == m_view_t:
            cnt -= 1
        
        t1 += 1
        s = ns % 60
        h = h % (60 * 60 * 12)
        m = m % (60 * 60)

    if nh_view_t % 60 == s or nm_view_t % 60 == s:
        cnt += 1
    
    print(cnt)
# 0.0166
# solution(0, 5, 30, 0, 7, 0) # 2
# solution(12, 0, 0, 12, 0, 30) # 1
# solution(0, 6, 1, 0, 6, 6) # 0
# solution(11, 59, 30, 12, 0, 0) # 1
# solution(11, 58, 59, 11, 59, 0) # 1
# solution(1, 5, 5, 1, 5, 6) # 2
# solution(0, 0, 0, 23, 59, 59) # 2852
solution( 0, 0, 0, 23, 0, 0) # 2735

