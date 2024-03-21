from queue import Queue
# 初始化邻接表
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(grah, root):
    visited = set()
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        x = queue.get()
        print(x)
        for i in grah[x]:
            if i not in visited:
                visited.add(i)
                queue.put(i)




if __name__ == "__main__":
    bfs(graph, "A")