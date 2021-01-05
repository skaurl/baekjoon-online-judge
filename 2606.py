n = int(input())
graph = {}
for i in range(n):
    graph[str(i+1)]=set()
m = int(input())
for i in range(m):
    a,b = map(str,input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(graph,start):
    visited = []
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue+=graph[n]-set(visited)
    return visited

print(len(bfs(graph,"1"))-1)