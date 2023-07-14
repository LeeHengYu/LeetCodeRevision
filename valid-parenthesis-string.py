class Solution:
    def checkValidString(self, s: str) -> bool:
        # sol: https://www.youtube.com/watch?v=QhPdNS143Qg
        MIN, MAX = 0, 0
        for c in s:
            if c=="(":
                MIN+=1
                MAX+=1
            elif c=="*":
                MIN-=1
                MAX+=1
            elif c==")":
                MIN-=1
                MAX-=1
            if MAX<0:
                return False
            if MIN<0:
                MIN=0
        return not MIN