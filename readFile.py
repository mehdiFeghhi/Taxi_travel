from operator import itemgetter


def find_feasible_edge(list_of_travel, list_of_cost_edge):
    sort_of_list = sorted(list_of_travel, key=itemgetter(0))
    start_node = []
    end_node = []
    size_of_list = len(sort_of_list)
    list_of_possible_edge = [['S0 1', 'D0 1']]
    k = 0
    for i in sort_of_list:
        list_of_possible_edge.append(['S0 1', 'S' + str(k + 1) + " " + i[2]])
        list_of_possible_edge.append(['D' + str(k + 1) + " " + i[3], 'D0 1'])
        k += 1
    k = 0
    for i in sort_of_list:
        start_node.append('S' + str(k + 1) + " " + i[2])
        end_node.append('D' + str(k + 1) + " " + i[3])
        for c in range(0, size_of_list):
            if sort_of_list[c][1] >= list_of_cost_edge[int(i[3]) - 1][int(sort_of_list[c][2]) - 1] + \
                    list_of_cost_edge[int(sort_of_list[c][3]) - 1][int(sort_of_list[c][2]) - 1] \
                    + i[1] and c != k:
                list_of_possible_edge.append(
                    ['D' + str(k + 1) + " " + i[3], 'S' + str(c + 1) + " " + sort_of_list[c][2]])

        k += 1

    return list_of_possible_edge, start_node, end_node, size_of_list


def find_feasible_edge_2(list_of_travel, list_of_cost_edge):
    sort_of_list = sorted(list_of_travel, key=itemgetter(0))
    start_node = []
    end_node = []
    size_of_list = len(sort_of_list)

    list_of_possible_edge = [['S0_1', 'D0_1']]
    k = 0
    for i in sort_of_list:
        list_of_possible_edge.append(['S0_1', 'S' + str(k + 1) + "_" + i[2]])
        list_of_possible_edge.append(['D' + str(k + 1) + "_" + i[3], 'D0_1'])
        k += 1
    k = 0
    for i in sort_of_list:
        start_node.append('S' + str(k + 1) + "_" + i[2])
        end_node.append('D' + str(k + 1) + "_" + i[3])
        for c in range(0, size_of_list):
            if sort_of_list[c][1] >= list_of_cost_edge[int(i[3]) - 1][int(sort_of_list[c][2]) - 1] + \
                    list_of_cost_edge[int(sort_of_list[c][3]) - 1][int(sort_of_list[c][2]) - 1] \
                    + i[1] and c != k:
                list_of_possible_edge.append(
                    ['D' + str(k + 1) + "_" + i[3], 'S' + str(c + 1) + "_" + sort_of_list[c][2]])

        k += 1

    return list_of_possible_edge, start_node, end_node, size_of_list


def make_matrix_travel(name_file) -> list:
    f = open(name_file, "r")
    table_numbers = int(f.readline())
    all_list = []
    for i in range(table_numbers):
        str_list = f.readline().split(',')
        start_hour = make_str_hour_to_hour(str_list[0])
        end_hour = make_str_hour_to_hour(str_list[1])
        all_list.append([start_hour, end_hour, str_list[2], str_list[3].split('\n')[0]])

    return all_list


def make_matrix_of_cost(name_file) -> list:
    f = open(name_file, "r")
    place_numbers = int(f.readline().split()[-1])
    matrix_of_cost = []
    for i in range(place_numbers):
        matrix_of_cost.append([0 for i in range(place_numbers)])

    for i in range(place_numbers):
        a = list(map(int, f.readline().split()))[1:]
        size = len(a)
        for j in range(place_numbers - size, place_numbers):
            matrix_of_cost[i][j] = a[j - (place_numbers - size)]
            matrix_of_cost[j][i] = a[j - (place_numbers - size)]

    return matrix_of_cost


def make_str_hour_to_hour(string) -> int:
    minute = int(string[-2:])
    hour = int(string[:-2])
    return hour * 60 + minute
