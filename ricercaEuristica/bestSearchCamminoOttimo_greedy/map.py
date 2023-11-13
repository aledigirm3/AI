# Connessioni

connections = {}
connections['Arad'] = {'Sibiu', 'Timisoara', 'Zerind'}
connections['Bucarest'] = {'Fagaras', 'Giurgiu', 'Pitesti', 'Urziceni'}
connections['Craiova'] = {'Drobeta', 'Pitesti', 'Rimnicu Vilcea'}
connections['Drobeta'] = {'Craiova', 'Mehadia'}
connections['Eforie'] = {'Hirsova'}
connections['Fagaras'] = {'Bucarest', 'Sibiu'}
connections['Giurgiu'] = {'Bucarest'}
connections['Hirsova'] = {'Eforie', 'Urziceni'}
connections['Iasi'] = {'Neamt', 'Vaslui'}
connections['Lugoj'] = {'Mehadia', 'Timisoara'}
connections['Mehadia'] = {'Drobeta', 'Lugoj'}
connections['Neamt'] = {'Iasi'}
connections['Oradea'] = {'Sibiu', 'Zerind'}
connections['Pitesti'] = {'Bucarest', 'Craiova', 'Rimnicu Vilcea'}
connections['Rimnicu Vilcea'] = {'Craiova', 'Pitesti', 'Sibiu'}
connections['Sibiu'] = {'Arad', 'Fagaras', 'Oradea', 'Rimnicu Vilcea'}
connections['Timisoara'] = {'Arad', 'Lugoj'}
connections['Urziceni'] = {'Bucarest', 'Hirsova', 'Vaslui'}
connections['Vaslui'] = {'Iasi', 'Urziceni'}
connections['Zerind'] = {'Arad', 'Oradea'}


# Funzione EURISTCA

h = {}
h['Arad'] = 366
h['Bucarest'] = 0
h['Craiova'] = 160
h['Drobeta'] = 242
h['Eforie'] = 161
h['Fagaras'] = 176
h['Giurgiu'] = 77
h['Hirsova'] = 151
# h['Iasi'] = 226
h['Iasi'] = 198
h['Lugoj'] = 244
h['Mehadia'] = 241
# h['Neamt'] = 234
h['Neamt'] = 100
h['Oradea'] = 380
h['Pitesti'] = 100
h['Rimnicu Vilcea'] = 193
h['Sibiu'] = 253
h['Timisoara'] = 329
h['Urziceni'] = 80
h['Vaslui'] = 199
h['Zerind'] = 374
