class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        edge_scores = [0] * len(edges)
        
        for u, v in enumerate(edges):
            edge_scores[v] += u
            
        max_val = edge_scores[0]
        max_idx =             0
        for idx, score in enumerate(edge_scores):
            if max_val < score:
                max_val = score
                max_idx = idx
                
        return max_idx
        