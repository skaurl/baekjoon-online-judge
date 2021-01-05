a,b,c=map(int,input().split())
graph = {}
for i in range(1,a+1):
    graph[str(i)]=set()
for j in range(b):
    x,y = map(str,input().split())
    graph[x].add(y)
    graph[y].add(x)

def dfs(graph,start):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack+=[str(j) for j in sorted([int(i) for i in graph[n]-set(visited)],reverse=True)]
    return visited

def bfs(graph,start):
    visited = []
    queue = [start]
    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue+=[str(j) for j in sorted([int(i) for i in graph[n]-set(visited)])]
    return visited

print(*dfs(graph,str(c)))
print(*bfs(graph,str(c)))