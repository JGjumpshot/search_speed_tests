import random
SEED_VALUE = 100
# random.seed(SEED_VALUE)
test = random.sample(range(1000000), k=SEED_VALUE)
#test.sort()
print(sorted(test))
