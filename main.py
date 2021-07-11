import readFile,NetWork_x,integer_linear
def main():

    number = input("which problem do you like to solve one(1)/two(2): ")
    file_name = input("please enter file name: ")
    list_of = readFile.make_matrix_travel(file_name)
    which_way = input("networkModel(1)/linear programming model(2): ")
    if number == '1':
        if which_way == '1':
            find_feasible_edge, Start_Node, End_Node, travels_number = readFile.find_feasible_edge(list_of,
                                                                                                           readFile.make_matrix_of_cost(
                                                                                                               "MarixD_dataset1_General.txt"))
            taxis_number = NetWork_x.question_one(find_feasible_edge, Start_Node, End_Node, travels_number)
            print("number_of_taxi :"+str(taxis_number))
        elif which_way == '2':
            find_feasible_edge, Start_Node, End_Node, travels_number = readFile.find_feasible_edge_2(list_of,
                                                                                                           readFile.make_matrix_of_cost(
                                                                                                               "MarixD_dataset1_General.txt"))
            integer_linear.question_one(find_feasible_edge,Start_Node,End_Node,travels_number)
    elif number == '2':
        if which_way == '1':
            find_feasible_edge, Start_Node, End_Node, travels_number = readFile.find_feasible_edge(list_of,
                                                                                                           readFile.make_matrix_of_cost(
                                                                                                               "MarixD_dataset1_General.txt"))
            taxis_number,Cost = NetWork_x.question_two(find_feasible_edge, Start_Node, End_Node, travels_number,
                                                    readFile.make_matrix_of_cost("MarixD_dataset1_General.txt"))

            print("number_of_taxi :"+str(taxis_number))
            print("amount_of cost :"+str(Cost))

        elif which_way == '2':
            find_feasible_edge, Start_Node, End_Node, travels_number = readFile.find_feasible_edge_2(list_of,
                                                                                                             readFile.make_matrix_of_cost(
                                                                                                                 "MarixD_dataset1_General.txt"))
            integer_linear.question_two(find_feasible_edge,Start_Node,End_Node,travels_number,readFile.make_matrix_of_cost(
                                                                                                                 "MarixD_dataset1_General.txt"))


if __name__ == '__main__':
    main()


