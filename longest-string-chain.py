class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        shortest = len(words[0])
        dp = {}
        for word in words:
            dp[word]=1
            if len(word)==shortest:
                continue 
            # loop through all possible predecessors
            for i in range(len(word)):
                prev = word[:i]+word[i+1:]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev]+1)
                
        return max(dp.values())