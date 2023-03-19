# python3

import sys


def build_heap(data, n):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(n // 2, -1, -1):
        lowest = i
        while True:
            left_branch = 2 * i + 1
            right_branch = 2 * i + 2
            if left_branch < n and data[left_branch] < data[lowest]:
                lowest = left_branch
            if right_branch < n and data[right_branch] < data[lowest]:
                lowest = right_branch
            if lowest != i:
                data[i], data[lowest] = data[lowest], data[i]
                swaps.append((i, lowest))
                i = lowest
            else:
                break

    return swaps


def main():

    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    input_method = input()
    if input_method.startswith("I"):
        # input from keyboard
        n = int(input())
        data = list(map(int, input().split()))
    elif input_method.startswith("F"):
        print("File path: ")
        file_name = input()
        file_path = "./tests/"
        if "a" not in file_name:
            with open(file_path + file_name, mode = "r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
        else:
            exit()
    else:
        exit()

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n, "Entered length must be the same as the actual length of the array"

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data, n)

    # TODO: output how many swaps were made, 
    # this lowestber should be less than 4n (less than 4*len(data))

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()