def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result

graph = {}

n = int(input())
for i in range(n):
    graph[str(i+1)] = set()
a,b = map(str,input().split())
m = int(input())
for i in range(m):
    c, d = map(str, input().split())
    graph[c].add(d)
    graph[d].add(c)
ans = bfs_paths(graph, a, b)
if ans == []:
    print(-1)
else:
    ans = [len(i)-1 for i in ans]
    print(min(ans))