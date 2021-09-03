import random

SEED_VALUE = 100
# random.seed(SEED_VALUE)
lyst = random.sample(range(1000000), k=SEED_VALUE)
#test.sort()
print(sorted(lyst), '\n')

def linear_search(my_list, target):
    for i in range(len(my_list)):
        if my_list[i] == target:
            return True

        return False
# def binary_search(lyst, target):

# def jump_search(lyst, target):

def main():
    print(lyst, '\n')
    print(linear_search(lyst, 23455))

if __name__ == "__main__":
    main()
