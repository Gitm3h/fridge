# Not used at the moment, but there for the test example
def evaluate(contents, food): #homework 2 hint:  def evaluate(contents, first, second):  then replace the body of the function
    if contents == food:
        print("Yes, it's all food!!!")
        return True
    else:
        print("That's not all of the food, or there is still something you shouldn't eat!!!")
        return False

def combine_foods(a, b):
    return a + b

def fridge():
    print("Welcome to the fridge")

    # "emmental" could also be a cheese, in the future
    contents = ["Cheese", "Butter", "Peas", "Milk"]
    shopping_list = ["Cheese", "Butter", "Milk", "Eggs", "Salami", "Lettuce"]
    print("You have in your fridge:\n")
    for x in contents:
        print(x)
    print("You still need:\n")
    for x in shopping_list:
        print(x)
    a = str(input("Enter an item: "))
    b = str(input("Enter another item: "))
    if a in contents and b in contents:
      print(f"The sum of {a} and {b} is {combine_foods(a, b.lower())}")
    elif a not in contents and b in contents:
      print(f"You don't have {a}, but you do have {b}" )
    if a in contents and b not in contents:
        print(f"You do not have {b}, which would go well with {a}")  
    else:
      print(f"You do not have either {a} nor {b}. Go shopping?")  

#'homework 1': The printing of the lists repeats. Can you turn that into a function that both can use?
#'homework 2': See 'evaluate()' above? Can you replace that with what you are evaluating in fridge()?
#'homework 3': Can you update the fridge_test.py to test the new evaluate()?

if __name__ == "__main__":
    fridge()
