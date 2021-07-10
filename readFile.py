from operator import itemgetter

def find_feasible_edge(list_of_travel,list_of_cost_edge) -> list:

    sort_of_list =  sorted(list_of_travel,key=itemgetter(0))
    size_of_list = len(sort_of_list)
    # print(sort_of_list)

    list_of_possible_edge = []
    k = 0
    for i in sort_of_list:
        list_of_possible_edge.append(['GS','S'+str(k)+" "+i[3]])
        list_of_possible_edge.append(['D'+str(k)+" "+i[3],'GN'])
        k += 1
    k = 0
    for i in sort_of_list:

        list_of_possible_edge.append(['S'+str(k)+" "+i[2],'D'+str(k)+" "+i[3]])
        for c in range(k+1,size_of_list):
            print(int(sort_of_list[c][2]))
            if sort_of_list[c][0] >= list_of_cost_edge[int(i[3])-1][int(sort_of_list[c][2])-1] + i[1]:
                list_of_possible_edge.append(['D'+str(k)+" "+i[3],'S'+str(c)+" "+sort_of_list[c][2]])


        k += 1

    return list_of_possible_edge


def make_matrix_travel(name_file) -> list:
    f = open(name_file, "r")
    number_of_table = int(f.readline())
    all_list = []
    for i in range(number_of_table):
        str_list = f.readline().split(',')
        start_hour = make_str_hour_to_hour(str_list[0])
        end_hour = make_str_hour_to_hour(str_list[1])
        all_list.append([start_hour,end_hour,str_list[2],str_list[3][:-1]])
    return all_list


def make_matrix_of_cost(name_file) -> list:

    f = open(name_file, "r")
    number_of_place = int(f.readline().split()[-1])
    matrix_of_cost = []
    for i in range(number_of_place):
        matrix_of_cost.append([0 for i in range(number_of_place)])

    for i in range(number_of_place):
        a = list(map(int, f.readline().split()))[1:]
        size = len(a)
        for j in range(number_of_place-size , number_of_place):
            # print(number_of_place-size)
            # print(j)
            # print("-------------------")
            matrix_of_cost[i][j] = a[j-(number_of_place-size)]
            matrix_of_cost[j][i] = a[j-(number_of_place-size)]

    return matrix_of_cost


def make_str_hour_to_hour(string) -> int:
    minute = int(string[-2:])
    hour = int(string[:-2])
    return hour * 60 + minute





