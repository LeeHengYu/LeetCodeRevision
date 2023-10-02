class Solution1: # brute force O(n)
    def winnerOfGame(self, colors: str) -> bool:
        qA = qB = 0
        n = len(colors)
        for i in range(1,n-1):
            if colors[i-1]==colors[i]==colors[i+1]=='A':
                qA += 1
            if colors[i-1]==colors[i]==colors[i+1]=='B':
                qB += 1
        return qA>qB

class Solution2: # replace O(n)
    def winnerOfGame(self, colors: str) -> bool:
        qA = qB = 0
        lastLen = len(colors)
        all_colors = "AB"
        for col in all_colors:
            while col*3 in colors:
                colors = colors.replace(col*3, col*2)
                if col == 'A':
                    qA += (lastLen - len(colors))
                else:
                    qB += (lastLen - len(colors))
                lastLen = len(colors)
        return qA > qB