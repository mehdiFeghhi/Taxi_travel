import networkx as nx


def question_one(list_of_possible_edge, Node_of_Start, Node_of_End, number_of_travel) -> int:
    G = nx.DiGraph()
    G.add_node('S0 1', demand=-number_of_travel)
    G.add_node('D0 1', demand=number_of_travel)
    for i in Node_of_Start:
        G.add_node(i, demand=1)

    for i in Node_of_End:
        G.add_node(i, demand=-1)

    G.add_edge(list_of_possible_edge[0][0], list_of_possible_edge[0][1], weight=-1)
    for i in list_of_possible_edge[1:]:
        G.add_edge(i[0], i[1], weight=0)

    flowCost, flowDict = nx.network_simplex(G)

    number_of_taxi = number_of_travel - flowDict['S0 1']['D0 1']
    print("**************")
    print(number_of_travel)
    print(flowDict['S0 1']['D0 1'])
    print("------------------------")
    return number_of_taxi


def find_weight(name_start, name_end, list_of_cost):
    return list_of_cost[int(name_start.split()[-1]) - 1][int(name_end.split()[-1]) - 1]


def question_two(list_of_possible_edge, Node_of_Start, Node_of_End, number_of_travel, list_of_cost) -> tuple:
    G = nx.DiGraph()
    G.add_node('S0 1', demand=-number_of_travel)
    G.add_node('D0 1', demand=number_of_travel)
    for i in Node_of_Start:
        G.add_node(i, demand=1)

    for i in Node_of_End:
        G.add_node(i, demand=-1)

    G.add_edge(list_of_possible_edge[0][0], list_of_possible_edge[0][1], weight=0)
    for i in list_of_possible_edge[1:]:
        cost = find_weight(i[0], i[1], list_of_cost)
        G.add_edge(i[0], i[1], weight=cost)

    flowCost, flowDict = nx.network_simplex(G)

    number_of_taxi = number_of_travel - flowDict['S0 1']['D0 1']
    print("**************")
    print(flowCost)
    print(number_of_travel)
    print(flowDict['S0 1']['D0 1'])
    print("------------------------")
    return number_of_taxi, flowCost
