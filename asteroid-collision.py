class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for n in asteroids:
            if n<0:
                while stack and stack[-1]>0 and stack[-1]<abs(n): # when the asteroid in the stack is smaller
                    stack.pop()
                if stack and stack[-1]+n==0: # both destroyed
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(n)
            else:
                stack.append(n)
        return stack