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
# def binary_search(lyst, target):

# def jump_search(lyst, target):

def main():
    #print(lyst, '\n')
    print((len(lyst) / 2))
    linear_search(lyst, lyst[-1])
    linear_search(lyst, lyst[0])
    print(len(lyst))
    linear_search(lyst, len(lyst) // 2)
    linear_search(lyst, lyst * 4)

if __name__ == "__main__":
    main()
