# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import readFile,NetWork_x,integer_linear
def main():

    # file_name = input("Please enter your name of file : ")
    #
    # list_of = readFile.make_matrix_travel(file_name)
    # # print(list_of)
    # find_feasible_edge,Node_of_Start,Node_of_End,number_of_travel = readFile.find_feasible_edge(list_of,readFile.make_matrix_of_cost("MarixD_dataset1_General.txt"))
    # number_of_taxi = NetWork_x.question_one(find_feasible_edge,Node_of_Start,Node_of_End,number_of_travel)
    # print(number_of_taxi)
    # print("//////////////////////////////////////")
    # number_of_taxi = NetWork_x.question_two(find_feasible_edge,Node_of_Start,Node_of_End,number_of_travel,readFile.make_matrix_of_cost("MarixD_dataset1_General.txt"))
    # print(number_of_taxi)

    number = input("witch problem do you like to solve one(1)/tow(2): ")
    file_name = input("please enter file name: ")
    list_of = readFile.make_matrix_travel(file_name)
    which_way = input("networkModel(1)/linear programming model(2): ")
    if number == '1':
        if which_way == '1':
            find_feasible_edge, Node_of_Start, Node_of_End, number_of_travel = readFile.find_feasible_edge(list_of,
                                                                                                           readFile.make_matrix_of_cost(
                                                                                                               "MarixD_dataset1_General.txt"))
            number_of_taxi = NetWork_x.question_one(find_feasible_edge, Node_of_Start, Node_of_End, number_of_travel)
            print("number_of_taxi :"+str(number_of_taxi))
        elif which_way == '2':
            find_feasible_edge, Node_of_Start, Node_of_End, number_of_travel = readFile.find_feasible_edge_2(list_of,
                                                                                                           readFile.make_matrix_of_cost(
                                                                                                               "MarixD_dataset1_General.txt"))
            integer_linear.question_one(find_feasible_edge,Node_of_Start,Node_of_End,number_of_travel)
    elif number == '2':
        if which_way == '1':
            find_feasible_edge, Node_of_Start, Node_of_End, number_of_travel = readFile.find_feasible_edge(list_of,
                                                                                                           readFile.make_matrix_of_cost(
                                                                                                               "MarixD_dataset1_General.txt"))
            number_of_taxi,Cost = NetWork_x.question_two(find_feasible_edge, Node_of_Start, Node_of_End, number_of_travel,
                                                    readFile.make_matrix_of_cost("MarixD_dataset1_General.txt"))

            print("number_of_taxi :"+str(number_of_taxi))
            print("amount_of cost :"+str(Cost))

        elif which_way == '2':
            find_feasible_edge, Node_of_Start, Node_of_End, number_of_travel = readFile.find_feasible_edge_2(list_of,
                                                                                                             readFile.make_matrix_of_cost(
                                                                                                                 "MarixD_dataset1_General.txt"))
            integer_linear.question_two(find_feasible_edge,Node_of_Start,Node_of_End,number_of_travel,readFile.make_matrix_of_cost(
                                                                                                                 "MarixD_dataset1_General.txt"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
