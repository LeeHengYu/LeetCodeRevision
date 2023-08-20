from collections import defaultdict
class Solution:
    def sortItems(self, n: int, m: int, group, beforeItems):
        def topoSort(adj,indeg): # adj is defaultdict(set), Kahn's algo, used on inter/intra group
            res = []
            q = [node for node in range(len(adj)) if indeg[node]==0]
            while q:
                curr = q.pop(0) 
                res.append(curr)
                for nxt in adj[curr]:
                    indeg[nxt]-=1
                    if not indeg[nxt]:
                        q.append(nxt)
            return res if len(res)==len(adj) else []

        unique = m
        for i in range(n):
            if group[i]==-1:
                group[i]=unique
                unique += 1
        
        item_adj = [[] for i in range(n)]
        group_adj = [[] for i in range(unique)]

        item_indeg = [0]*n
        group_indeg = [0]*unique

        for i in range(n):
            for prereq in beforeItems[i]:
                item_adj[prereq].append(i)
                item_indeg[i]+=1
                if group[i]!=group[prereq]:
                    group_adj[group[prereq]].append(group[i])
                    group_indeg[group[i]]+=1 

        orderedItems = topoSort(item_adj, item_indeg)
        orderedGroups = topoSort(group_adj, group_indeg)
        if not orderedItems or not orderedGroups: return []

        itemInGroups = defaultdict(list)
        for item in orderedItems: 
            itemInGroups[group[item]].append(item)
        ans = []
        for grp in orderedGroups:
            ans+=itemInGroups[grp]

        return ans 