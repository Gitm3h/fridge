# Not used at the moment, but there for the test example
def evaluate(contents, shopping_list, combine_foods): #homework 2 hint:  def evaluate(contents, first, second):  then replace the body of the function
    if contents == True:
        print("Guten Apetit!!!")
        return True
    else:
        print("There's nothing to eat!!!")
        return False

def loop(x):
    for x in x:
        print(x)

def combine_foods(a, b):
    return a + b

def fridge():
    print("Welcome to the fridge")
    print("You currently have:\n")

    # "emmental" could also be a cheese, in the future
    contents = ["Emmental", "Butter", "Peas", "Milk", "Bread"]
    loop(contents)
    print ("You still need:\n")
    shopping_list = ["Cheddar", "Mushrooms", "Honey", "Eggs", "Salami", "Lettuce"]
    loop(shopping_list)
    a = str(input("Enter an item: "))
    b = str(input("Enter another item: "))
    if a and b in contents:
        print(f"The sum of {a} and {b} is {combine_foods(a, b.lower())}")
    elif a not in contents:
      print(f"You don't have {a}, but you do have {b}" )
    if b not in contents:
        print(f"You do not have {b}, which would go well with {a}")  
    else:
        print(f"You do not have either {a} nor {b}. Go shopping?")  

#'homework 1': The printing of the lists repeats. Can you turn that into a function that both can use? Done
#'homework 2': See 'evaluate()' above? Can you replace that with what you are evaluating in fridge()? Maybe done?
#'homework 3': Can you update the fridge_test.py to test the new evaluate()?

if __name__ == "__main__":
    fridge()
