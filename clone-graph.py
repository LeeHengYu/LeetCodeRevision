"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution1: # DFS recursion in Python 3
    def cloneGraph(self, node: 'Node') -> 'Node':
        mp = {}
        if not node: return None

        def clone(node):
            if not node:
                return None
            if node in mp:
                return mp[node]
            
            copy = Node(node.val)
            mp[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(clone(nei)) # Recursion 
            return copy

        return clone(node)
    
# Credit: NeetCode

class Solution2 { # BFS in C++
public:
    Node* cloneGraph(Node* node) {
        if (!node) return NULL;

        queue<Node*> q; //processing q
        q.push(node);

        Node* clone = new Node(node->val);
        mp[node] = clone; //map old node to new node in the hash table

        while(!q.empty()){
            Node* curr = q.front();
            q.pop();

            //process all the neighbors of CURR
            for (int i=0; i<curr->neighbors.size(); ++i){
                Node* currnei = curr->neighbors[i];
                
                if (mp.find(currnei)==mp.end()){
                    mp[currnei] = new Node (currnei->val);
                    q.push(currnei);
                }

                mp[curr]->neighbors.push_back(mp[currnei]);
            }
        }

        return mp[node];
    }

private:
    unordered_map<Node*, Node*> mp;
};

