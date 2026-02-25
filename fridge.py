contents = ["Emmental", "Butter", "Peas", "Milk", "Bread"]


# Not used at the moment, but there for the test example
def evaluate(contents, first, second):  # then replace the body of the function
  a = first
  b = second
  if a and b in contents:
    print(f"The sum of {a} and {b} is {a}{b.lower()}")
    return 2
  if a not in contents:
    print(f"You don't have {a}, but you do have {b}" )
    return 1
  if b not in contents:
    print(f"You do not have {b}, which would go well with {a}") 
    return 1 
  print(f"You do not have either {a} nor {b}. Go shopping?") 
  return 0

def print_list(x):
  for x in x:
      print(x)


def eating_sesh(score):
  a = str(input("\nEnter an item: "))
  b = str(input("Enter another item: "))
  score += evaluate(contents, a, b)
  return score

def fridge():
  print("Welcome to the fridge")
  score: int = 0

  print("You currently have:\n")
  # "emmental" could also be a cheese, in the future
  print_list(contents)
  print ("\nYou still need:\n")
  shopping_list = ["Cheddar", "Mushrooms", "Honey", "Eggs", "Salami", "Lettuce"]
  print_list(shopping_list)

  while score <5:
    score = eating_sesh(score)
    print(f"Score: {score}")

  print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!  YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")  
  exit(0)
    

#'homework 1': Can you update the fridge_test.py to test the evaluate()'s return values (no need to test the prints)?
#'homework 2': Let's allow the player to lose as well. How would you implement that?

if __name__ == "__main__":
    fridge()
