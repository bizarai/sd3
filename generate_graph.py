import graphviz

# Create a new directed graph
dot = graphviz.Digraph(comment='AI Concepts Knowledge Graph')
dot.attr(rankdir='LR', size='8,5')

# Add nodes
nodes = [
    "Supercomputing", "Reinforcement_Learning", "Transformer", "High_Dimensionality",
    "Multimodal", "Diffusion_Models", "Meta_Learning", "Planning", "Context",
    "Fine_Tuning", "RAG", "GANs", "NeRFs", "3D_Convergence", "Compression", "Distillation"
]

for node in nodes:
    dot.node(node, node.replace('_', ' '))

# Add edges
edges = [
    ("Supercomputing", "Transformer", "enables"),
    ("Transformer", "Reinforcement_Learning", "enhances"),
    ("Reinforcement_Learning", "Planning", "optimizes"),
    ("Planning", "Meta_Learning", "aids"),
    ("Meta_Learning", "Fine_Tuning", "improves"),
    ("Transformer", "Diffusion_Models", "powers"),
    ("Transformer", "GANs", "used in"),
    ("Transformer", "RAG", "integrates with"),
    ("GANs", "NeRFs", "applies to"),
    ("NeRFs", "3D_Convergence", "advances"),
    ("Diffusion_Models", "High_Dimensionality", "requires"),
    ("Multimodal", "High_Dimensionality", "operates in"),
    ("Multimodal", "Context", "builds"),
    ("RAG", "Context", "augments"),
    ("Compression", "Transformer", "optimizes"),
    ("Compression", "High_Dimensionality", "reduces"),
    ("Distillation", "Transformer", "applies to"),
    ("Distillation", "Compression", "related to"),
    ("Distillation", "Fine_Tuning", "precedes")
]

for edge in edges:
    dot.edge(edge[0], edge[1], edge[2])

# Generate the graph
dot.render('ai_concepts_graph', format='svg', cleanup=True)
print("Graph generated as 'ai_concepts_graph.svg'")
