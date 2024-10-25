import random
a = ["The moon", "A lonely star", "Whispers of the wind", "The ocean", "A fleeting dream"]
b = ["dances", "sings", "whispers", "glows", "fades"]
c = ["in the night sky", "with a gentle touch", "through the trees", "beneath the waves", "in silence"]
d = ["serene", "mysterious", "eternal", "fading", "luminous"]
x=1 
while x==1:
  print("Welcome to the Poem Generator!\n")
  print("\nPoem generated creatd by Alok:\n")
        
  rand = random.randint(0,4)
  print(a[rand])
  rand = random.randint(0,4)
  print(b[rand])
  rand = random.randint(0,4)
  print(c[rand])
  rand = random.randint(0,4)
  print(d[rand])
  x=int(input('Press 1 to continue creating poem'))
    