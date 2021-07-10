# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import readFile
def main():

    file_name = input("Please enter your name of file : ")

    list_of = readFile.make_matrix_travel(file_name)
    # print(list_of)
    print(readFile.find_feasible_edge(list_of,readFile.make_matrix_of_cost("MarixD_dataset1_General.txt")))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
