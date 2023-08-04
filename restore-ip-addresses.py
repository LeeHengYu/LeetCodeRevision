class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # backtracking
        res = []
        def dfs(i, partition):
            if i==len(s):
                if len(partition)==4:
                    res.append(".".join(partition))
                return
            if (i<len(s) and len(partition)==4):
                return
            
            if s[i]=='0':
                partition.append('0')
                dfs(i+1, partition)
                partition.pop()
            else:
                for j in range(1,4):
                    if i+j<=len(s) and 0<=int(s[i:i+j])<=255:
                        partition.append(s[i:i+j])
                        dfs(i+j, partition)
                        partition.pop()
        dfs(0,[])
        return res