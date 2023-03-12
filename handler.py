from info import info
import graphviz
import networkx

def handle(pb2_request, repo_path):
  gr_format = pb2_request.input.decode('utf-8')

  graph = networkx.Graph()
  lines = gr_format.split('\n')
  for line in lines:
    if line.startswith('c'):
      continue
    elif line.startswith('p'):
      p, tw, n_nodes, _ = line.split()
      assert p == 'p' and tw == 'tw'
      n_nodes = int(n_nodes)
      graph.add_nodes_from(range(1, n_nodes+1))
    elif line:
      u, v = map(int, line.split())
      graph.add_edge(u, v)

  # Create .svg from from the networkx graph.
  # This to_agraph function is in the pygraphviz package, NOT in the graphviz package.
  pygraphviz_graph = networkx.drawing.nx_agraph.to_agraph(graph)
  pygraphviz_graph.layout('dot')
  pygraphviz_graph.graph_attr['bgcolor'] = 'transparent'
  pygraphviz_graph.node_attr['style'] = 'filled'
  pygraphviz_graph.node_attr['color'] = 'aliceblue'
  pygraphviz_graph.node_attr['shape'] = 'circle'
  pygraphviz_graph.edge_attr['dir'] = 'none'
  svg_code = graphviz.Source(pygraphviz_graph.to_string()).pipe(format='svg').decode('utf-8')

  return svg_code
