import math
import random
import time

SEED_VALUE = int(100 * random.random())
lyst = sorted(random.sample(range(1000000), k=SEED_VALUE))


def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return True

    return False


def binary_search(my_list, target):
    middle = (len(my_list) // 2)
    if len(my_list) == 0:
        return False
    elif target == my_list[middle]:
        return True
    elif target > my_list[middle]:
        # try:
        return binary_search(my_list[middle + 1:], target)
    elif target < my_list[middle]:
        return binary_search(my_list[:middle], target)

def jump_search(my_list, target):
    try:
        step = math.floor(math.sqrt(len(my_list)))
        i = 0
        while my_list[step - 1] < target:
            i = step
            step += math.floor(math.sqrt(len(my_list)))
            if i >= len(my_list):
                return False

        while my_list[i] < target:
            i += 1
            if i == step:
                return False

        if my_list[i] == target:
            return True
        else:
            return False
    except(IndexError) as error:
        return f"Error is {error}"


def stopwatch(function, my_list, target, my_type):
    start = time.perf_counter()
    function(my_list, target)
    stop = time.perf_counter()
    print(f"Function {function.__name__} took {stop - start} seconds to run {my_type}")


def main():
    stopwatch(linear_search, lyst, lyst[-1], "finding end of list element")
    stopwatch(linear_search, lyst, lyst[0], "finding the first element")
    stopwatch(linear_search, lyst, len(lyst) // 2, "finding the middle element")
    stopwatch(linear_search, lyst, len(lyst) * 4, "finding an index out of range")
    stopwatch(binary_search, lyst, lyst[-1], "finding end of list element")
    stopwatch(binary_search, lyst, lyst[0], "finding the first element")
    stopwatch(binary_search, lyst, len(lyst) // 2, "finding the middle element")
    stopwatch(binary_search, lyst, len(lyst) * 4, "finding an index out of range")
    stopwatch(jump_search, lyst, lyst[-1], "finding end of list element")
    stopwatch(jump_search, lyst, lyst[0], "finding the first element")
    stopwatch(jump_search, lyst, len(lyst) // 2, "finding the middle element")
    stopwatch(jump_search, lyst, len(lyst) * 4, "finding an index out of range")


if __name__ == "__main__":
    main()
