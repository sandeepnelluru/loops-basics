# while loop
i = 1
while i <= 5:
    print("*"*i)
    i = i+1
print(i)

# building a guessing game using while loop
# secret_number = 9
# guess_count = 0
# guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count +=1
    if guess == secret_number:
       print("You Won!")
       break
else:
       print("Sorry, You lost")

l = [1,4,6,234,6,764]
for i in l:
    print(i)

t = (6,231,75,122)
for i in t:
   print(i)

l = [1,7,8]
for item in l:
    print(item)
else:
    print("done")

for i in range(1,100):
    if i == 34:
        break #ends loop then and there itself
    print(i)

for i in range(1,35):
    if i == 21:
        continue #skips the value

    print(i)
for i in range(645):
    pass #null statement in python helps to skip

i = 0
while i < 15:
    print(i)
    i += 1

# Write a program to print multiplication table of a given number using for loop.
n = int(input("Enter the number: "))
for i in range(1,11):
 print(f"{n} X {i} = {n * i}")
    
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")
