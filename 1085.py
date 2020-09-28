x, y, w, h = map(int,input().split())
N = []
N.extend([x,y,w-x,h-y])
print(min(N))