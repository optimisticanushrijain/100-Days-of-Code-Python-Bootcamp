enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

testing = 8.0

def test_scope():
    testing = 10
    print(f"Inside the function: {testing}")

print(f"Outside the function: {testing}")
test_scope()
