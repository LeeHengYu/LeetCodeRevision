def solution(s):
    # DP not easy: need to consider both front and back
    res, n = 0, len(s)
    pTank = -1 # keep track of the front most tank setup
    for i in range(n):
        front, back = False, False
        if s[i]=="-": # only consider houses
            continue
        if i>0 and s[i-1]=="-": # there can be a tank at the front
            front = True
        if i<n-1 and s[i+1]=="-": # there can be a tank at the back
            back = True
        if not front and not back:
            return -1 # invalid
        
        # setting up tanks: GREEDY ALGO
        # traverse from front to back
        # prioritize back tank as it can be shared with possibly more houses
        
        if back and pTank!=i-1:
            # also need to check if there is already a tank at the front, set up a tank at the back
            res += 1
            pTank = i+1
        elif not back and front and pTank!=i-1:
            # check if already set up a tank at the front
            res += 1
            pTank = i-1
    return res


print(solution("-"))