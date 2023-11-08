import random

def game(comp, b):
    if comp == b:
        return None
    elif comp == 'S':
      if b == 'W':
          return True 
      elif b == 'G':
          return True
    elif comp == 'W':
      if b == 'G':
          return False
      elif b == 'S':
          return True
    elif comp == 'G':
      if b == 'S':
          return False
      elif b == 'W':
          return True


print("Comps turn: Snake(S) Water(W) or Gun(G)")
randno = random.randint(1,  3)
print(randno)
if randno ==1:
    comp='S'
elif randno ==2:
    comp= 'W'
elif randno ==3:
    comp= 'G'
b = input("Player's turn: Snake(S) Water(W) or Gun(G)")
a =game(comp, b)

print(f"computer chose\t{comp}")
print(f"you chose\t{b}")

if a == None:
    print("the game is a tie!")
elif a:
    print("you win")
else:
    print("you lose")