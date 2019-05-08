## Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # print(node.neighbors[1].neighbors[1].val)
        """
        DFS 62%
        Algorith:
        1. set up a dictionary, to store the function
        2. for each node, copy value, copy neighbor
        """
        def DFS(node):
            if node.val in dic:
                return dic[node.val]
            else:
                val = node.val
                nei = []
                new = Node(val, nei)
                dic[val] = new
                for i in node.neighbors:
                    nei.append(DFS(i))
            return new

        dic = {}
        new_node = DFS(node)

        return new_node
