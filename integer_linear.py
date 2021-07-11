from pulp import *


def question_one(list_of_possible_edge, Node_of_Start, Node_of_End, number_of_travel):
    nodes = ['S0_1', 'D0_1'] + Node_of_Start + Node_of_End
    nodeData = {'S0_1': [number_of_travel, 0], 'D0_1': [0, number_of_travel]}
    for i in Node_of_Start:
        nodeData[i] = [0, 1]

    for i in Node_of_End:
        nodeData[i] = [1, 0]

    arcs = []
    for i in list_of_possible_edge:
        arcs.append((i[0], i[1]))

    arcData = {(list_of_possible_edge[0][0], list_of_possible_edge[0][1]): [-1, 0, number_of_travel]}

    # for k in range(len(Node_of_Start)):
    #     arcData[(Node_of_Start[k], Node_of_End[k])] = [0, 1, 1]

    for i in list_of_possible_edge[1:]:
        arcData[(i[0], i[1])] = [0, 0, 1]

    (supply, demand) = splitDict(nodeData)
    (costs, mins, maxs) = splitDict(arcData)
    vars = LpVariable.dicts("Route", arcs, None, None, LpInteger)
    # Creates the upper and lower bounds on the variables
    for a in arcs:
        vars[a].bounds(mins[a], maxs[a])

    # Creates the 'prob' variable to contain the problem data
    prob = LpProblem("Minimum Cost Flow Problem Sample", LpMinimize)

    # Creates the objective function
    prob += lpSum([vars[a] * costs[a] for a in arcs]), "Total Cost of Transport"

    # Creates all problem constraints - this ensures the amount going into each node is
    # at least equal to the amount leaving
    for n in nodes:
        prob += (supply[n] + lpSum([vars[(i, j)] for (i, j) in arcs if j == n]) >=
                 demand[n] + lpSum([vars[(i, j)] for (i, j) in arcs if i == n])), \
                "Flow Conservation in Node %s" % n

    # The problem data is written to an .lp file
    prob.writeLP("simple_MCFP.lp")

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The optimised objective function value is printed to the sc
    # print("Total Cost of Transportation = ", value(prob.objective))
    print("Taxi = ",number_of_travel + value(prob.objective))


def find_weight(name_start, name_end, list_of_cost):
    return list_of_cost[int(name_start.split('_')[-1]) - 1][int(name_end.split('_')[-1]) - 1]


def question_two(list_of_possible_edge, Node_of_Start, Node_of_End, number_of_travel,list_of_cost):

    nodes = ['S0_1', 'D0_1'] + Node_of_Start + Node_of_End
    nodeData = {'S0_1': [number_of_travel, 0], 'D0_1': [0, number_of_travel]}
    for i in Node_of_Start:
        nodeData[i] = [0, 1]

    for i in Node_of_End:
        nodeData[i] = [1, 0]

    arcs = []
    for i in list_of_possible_edge:
        arcs.append((i[0], i[1]))

    arcData = {(list_of_possible_edge[0][0], list_of_possible_edge[0][1]): [0, 0, number_of_travel]}

    # for k in range(len(Node_of_Start)):
    #     arcData[(Node_of_Start[k], Node_of_End[k])] = [0, 1, 1]

    for i in list_of_possible_edge[1:]:
        arcData[(i[0], i[1])] = [find_weight(i[0], i[1],list_of_cost), 0, 1]

    (supply, demand) = splitDict(nodeData)
    (costs, mins, maxs) = splitDict(arcData)
    vars = LpVariable.dicts("Route", arcs, None, None, LpInteger)
    # Creates the upper and lower bounds on the variables
    for a in arcs:
        vars[a].bounds(mins[a], maxs[a])

    # Creates the 'prob' variable to contain the problem data
    prob = LpProblem("Minimum Cost Flow Problem Sample", LpMinimize)

    # Creates the objective function
    prob += lpSum([vars[a] * costs[a] for a in arcs]), "Total Cost of Transport"

    # Creates all problem constraints - this ensures the amount going into each node is
    # at least equal to the amount leaving
    for n in nodes:
        prob += (supply[n] + lpSum([vars[(i, j)] for (i, j) in arcs if j == n]) >=
                 demand[n] + lpSum([vars[(i, j)] for (i, j) in arcs if i == n])), \
                "Flow Conservation in Node %s" % n

    # The problem data is written to an .lp file
    prob.writeLP("simple_MCFP_2.lp")

    # The problem is solved using PuLP's choice of Solver
    prob.solve()

    # The optimised objective function value is printed to the sc
    print("Total Cost of Transportation = ", value(prob.objective))
