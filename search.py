import random

SEED_VALUE = int( 100 * random.random())
# random.seed(SEED_VALUE)
lyst = sorted(random.sample(range(1000000), k=SEED_VALUE))
#test.sort()
print(sorted(lyst), '\n')
print(len(sorted(lyst)), '\n')
def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return True

    return False
#TODO: Need to test if target < my_list[middle]
def binary_search(my_list, target):
    new_list = []
    middle = (len(my_list) // 2) - 1

    print(f"{my_list}\n{my_list[middle]} \n{my_list[middle:]}")
    if (target > my_list[middle]):
        new_list.append(my_list[middle:])
        return True
    else:
        return False
print(binary_search([1,2,3,4,5,6,7,8], 5))


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
