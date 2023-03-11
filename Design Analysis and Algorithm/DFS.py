def DFS(graph,start,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)

    print(start)

    for next in graph[start]-visited:
        DFS(graph,next,visited)
    return visited

graph={
    '0':set(['1','2']),
    '1':set(['2']),
    '2':set(['0','3']),
    '3':set(['3'])   
}
DFS(graph,'2')