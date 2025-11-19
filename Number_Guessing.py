import random
lower_bound = 1 
Uper_bound = 100
Secret_number = random.randint(lower_bound,Uper_bound)
max_attempts = 10 
attempts = 0

while attempts < max_attempts :
    try:
         guess = int(input(f"Guess The Number Betwwen {lower_bound} and {Uper_bound}:"))
         attempts +=1
         if guess < Secret_number:
              print("Too Low!")
         elif guess > Secret_number:
              print("Too High")
         else:
              print(f"Congratulations ! you Guess the Number in {attempts} Attempts")     
              break
    except ValueError:
         print("invalid input.Plesase enter a Intezer")
else:
     print(f"sorry you use all {max_attempts} Attempts.The Number was {Secret_number} ")         
               