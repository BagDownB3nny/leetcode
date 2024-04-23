class Node:
    
    def __init__(self):
        self.neighbours = set()
    
    def addNeighbour(self, n: int):
        self.neighbours.add(n)
        
    def removeNeighbour(self, n: int):
        self.neighbours.remove(n)
        

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        nodes = {}
        leaves = set()
        removed = set()
        for edge in edges:
            for i in range(2):
                node = edge[i]
                otherNode = edge[(i + 1) % 2]
                if node in nodes:
                    nodes[node].addNeighbour(otherNode)
                    if node in leaves:
                        leaves.remove(node)
                else:
                    newNode = Node()
                    newNode.addNeighbour(otherNode)
                    nodes[node] = newNode
                    leaves.add(node)
      
        newLeaves = []
        while len(nodes) > 2:
            numLeaves = len(leaves)
            for _ in range(numLeaves):
                leaf = leaves.pop()
                leafNode = nodes[leaf]
                for neighbour in leafNode.neighbours:
                    neighbourNode = nodes[neighbour]
                    neighbourNode.removeNeighbour(leaf)
                    if len(neighbourNode.neighbours) == 1:
                        newLeaves.append(neighbour)
                del nodes[leaf]
            for leaf in newLeaves:
                leaves.add(leaf)
            newLeaves = []
        
        answers = []
        for key in nodes:
            answers.append(key)
            
        return answers
            
                
            
