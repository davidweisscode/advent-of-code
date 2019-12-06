import networkx as nx

def get_edge(orbit):
    rel_index = orbit.index(")")
    return (orbit[:rel_index], orbit[rel_index + 1:-1])

def get_total_orbit_sum(orbitgraph):
    sum = 0
    for stellar_object in orbitgraph.nodes():
        sum += nx.shortest_path_length(orbitgraph, stellar_object, "COM")
    return sum

edges = []

with open("orbitmap.txt", "r") as file:
    for orbit in file:
        edge = get_edge(orbit)
        edges.append(edge)

orbitgraph = nx.Graph()
orbitgraph.add_edges_from(edges)

total_orbit_sum = get_total_orbit_sum(orbitgraph)
print("The total number of direct and indirect orbits is", total_orbit_sum)

print("You are orbiting")
[print(n) for n in orbitgraph.neighbors("YOU")]
print("Santa is orbiting")
[print(n) for n in orbitgraph.neighbors("SAN")]

orbital_transfers = nx.shortest_path_length(orbitgraph, "YOU", "SAN") - 2

print("The minimum number of orbital transfers required to reach Santa is", orbital_transfers)
