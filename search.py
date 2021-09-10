import random

SEED_VALUE = int( 100 * random.random())
# random.seed(SEED_VALUE)
lyst = sorted(random.sample(range(1000000), k=SEED_VALUE))
#test.sort()
#print(sorted(lyst), '\n')

def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return True

    return False
def binary_search(my_list, target):
    middle = (len(my_list) // 2) - 1
    print(my_list[middle])
    # if (my_list):
    #     return True
    # elif (target != my_list[i]):


# def jump_search(lyst, target):

def main():
    #print(lyst, '\n')
    linear_search(lyst, lyst[-1])
    linear_search(lyst, lyst[0])
    linear_search(lyst, len(lyst) // 2)
    linear_search(lyst, lyst * 4)
    binary_search(lyst, lyst[-1])
if __name__ == "__main__":
    main()
