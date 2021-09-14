import random

SEED_VALUE = int(100 * random.random())
# random.seed(SEED_VALUE)
lyst = sorted(random.sample(range(1000000), k=SEED_VALUE))
# test.sort()
# print(sorted(lyst), '\n')
# print(len(sorted(lyst)), '\n')


def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return True

    return False


def binary_search(my_list, target):
    middle = (len(my_list) // 2)
    # print(f"List: {my_list}\nMiddle: {my_list[middle]} \nSlice: {my_list[middle + 1:]}")
    if len(my_list) == 0:
        return False
    elif target == my_list[middle]:
        return True
    elif target > my_list[middle]:
        return binary_search(my_list[middle + 1:], target)
    elif target < my_list[middle]:
        return binary_search(my_list[:middle], target)


# def jump_search(lyst, target):

def main():
    #print(lyst, '\n')
    linear_search(lyst, lyst[-1])
    linear_search(lyst, lyst[0])
    linear_search(lyst, len(lyst) // 2)
    linear_search(lyst, lyst * 4)
    binary_search(lyst, lyst[-1])
    binary_search(lyst, lyst[0])


if __name__ == "__main__":
    main()
