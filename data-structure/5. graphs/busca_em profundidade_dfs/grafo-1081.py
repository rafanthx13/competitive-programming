# URI 1081 - Grafos - Outubro de 2019
# Assunto: DFS, BackTracking
# Accepted

print_list = []
visited = []
entrou = []
final_list = []

def print_pathR(b, start, node):
  return " "*b + str(start) + "-" + str(node) + " pathR(G," + str(node) + ")"

def print_final_node(b, start, node):
  return " "*b + str(start) + "-" + str(node)

def dfs(graph, qtd_vertex, start):
  b = 2
  entrou[start] = True
  for node in graph[start]:
    if(not visited[node]):
      print_list.append( print_pathR(b, start, node) )
      dfs_recursive(graph, node, b+2)
      visited[node] = True
    else:
      print_list.append( print_final_node(b, start, node) )
  visited[start] = True

def dfs_recursive(graph, node, b):
  for no in graph[node]:
    if(not entrou[no]):
      print_list.append( print_pathR(b, node, no) )
    else:
      print_list.append( print_final_node(b, node, no) )
      continue
    entrou[no] = True
    if(not visited[no]):
      dfs_recursive(graph, no, b+2)
    visited[no] = True

# A linha pathR nao nao pode ser repetir, entou, se ja
# entrou num no, nao pode chamar denovo

# Exec

n = int(input())

for case in range(n):
  vert, edge = list(map(int, input().split()))
  graph = { i:[] for i in range(vert)}
  print_list = []
  visited = [False]*vert
  entrou = [False]*vert

  # get edges
  for _ in range(edge):
    v1, v2 = list(map(int, input().split()))
    graph[v1].append(v2)

  # order nodes
  for el in graph.keys():
    graph[el] = sorted(graph[el])
  final_list = []

  for no in graph.keys():
    if(graph[no] != [] and not visited[no]):
      print_list = []
      dfs(graph, vert, no)
      final_list.append(print_list)

  print("Caso "+ str(case + 1) + ":")
  for ak in final_list:
    for l in ak:
      print(l)
    print()
