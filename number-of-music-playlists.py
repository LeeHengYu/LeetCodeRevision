class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        dp = {}
        def sol(size, unique):
            if size==goal:
                return 1
            if (size, unique) in dp:
                return dp[(size, unique)]
            res = repeat = 0
            if size>=k+1 and goal-size>n-unique:
                # 2 conditions: after first k songs are played
                # the remaining songs that need to be played must not be the ones yet appeared
                repeat = unique-k # last k songs cannot be played
            notRepeat = n-unique
            if repeat:
                res += sol(size+1,unique)*repeat # choose from repeat
            res += sol(size+1,unique+1)*notRepeat
            dp[(size, unique)]=res
            return res
        return sol(0,0)%(10**9+7)

        # sol: https://leetcode.com/problems/number-of-music-playlists/solutions/1879256/python-solution-recursion-memo-well-explained-how-to-reach-explained/