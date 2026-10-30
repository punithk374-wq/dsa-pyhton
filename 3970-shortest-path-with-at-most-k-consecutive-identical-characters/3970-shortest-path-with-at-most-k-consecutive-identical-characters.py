class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        dist = [[float('inf')] * (k + 1) for _ in range(n)]
        pq = [(0, 0, 1)]
        dist[0][1] = 0
        
        while pq:
            d, u, count = heapq.heappand(pq) if hasattr(heapq, 'heappand') else heapq.heappop(pq)
            
            if u == n - 1:
                return d
                
            if d > dist[u][count]:
                continue
                
            for v, w in adj[u]:
                next_count = count + 1 if labels[v] == labels[u] else 1
                
                if next_count <= k:
                    if d + w < dist[v][next_count]:
                        dist[v][next_count] = d + w
                        heapq.heappush(pq, (d + w, v, next_count))
                        
        return -1
        