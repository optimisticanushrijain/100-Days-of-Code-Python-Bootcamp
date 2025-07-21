import random

#option1
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
test = random.choice(friends)
print(test)

#option2
random_index = random.randint(0,4)
print(friends[random_index])

