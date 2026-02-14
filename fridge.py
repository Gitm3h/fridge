# Not used at the moment, but there for the test example
def evaluate(contents, food):
    if contents == food:
        print("Yes, it's all food!!!")
        return True
    else:
        print("That's not all of the food, or there is still something you shouldn't eat!!!")
        return False

def fridge():
    print("Welcome to the fridge")

    # "emmental" could also be a cheese, in the future
    contents = ["Cheese", "Butter", "Peas", "Milk"]
    shopping_list = ["Cheese", "Butter", "Milk", "Eggs", "Salami", "Lettuce"]
    print("You have in your fridge:\n")
    for x in contents:
        print(x)


if __name__ == "__main__":
    fridge()


