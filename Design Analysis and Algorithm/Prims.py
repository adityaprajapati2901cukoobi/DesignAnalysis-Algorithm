ini=999999
v=6
g=[[0,4,4,0,0,0],
   [4,0,2,0,0,0],
   [4,2,0,3,4,2],
   [0,0,3,0,0,3],
   [0,0,2,0,0,3],
   [0,0,4,3,3,0]]

visited=[0,0,0,0,0,0]
edge=0
visited[0]=True

print("Edge: Weight\n")
while(edge<v-1):
    minn=ini
    a=b=0
    for i in range(v):
        if visited[i]:
            for j in range(v):
                if((not visited[j]) and g[i][j]):
                   if minn > g[i][j]:
                      minn=g[i][j]
                      a=i
                      b=j

    print(str(a)+" - "+str(b)+":"+str(g[a][b]))
    visited[b]=True
    edge +=1
