import math
import turtle
print("Hello world")
print("********")
z = 1
# ctrl + shift + P (format documnet)
# ctrl + s ( auto format )
# cd = finding path in cmd
# ctrl + Alt + n (run code)
x = 1
x = 1
word = "python"
print("py" in word)
print("n" in word)
x = 5
x += 3
print(x)
x = 2
x /= 3
print(float(x))
print(round(x))
x = 16
print(abs(x))
print(math.sqrt(x))
print(math.comb(5, 2))
print(ord("apple"[0]))
x = 14
if x > 11:
    print("x is greater than 10")
elif x < 11:
    print(" x is equal to 10")
else:
    print("x is greater than 11")
age = 17
message = "eligible" if age >= 18 else "not eligible"
print(message)
high_income = True
good_credit = True
student = True
if not student or (high_income and good_credit):
    print("eligible for loan")
else:
    print("not eligible for loan")
if 15 <= age < 50:
    print("eigible age")
for number in range(1, 9, 3):
    print("hello world")
    print(number)
successful = False
for number in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")
for x in range(6):
    for y in range(2):
        print(f"{x}, {y}")
number = [1, 2, 3, 4, 5]
for x in number:
    print(x)
number = 100
while number > 0:
    print(number)
    number //= 2
print("done")
command = " "
while True:
    command = input(">>>")
    print(command)
    if command == 'exit':
        break




def write():
    print("my mother is beautiful")


write()

from turtle import Turtle, Screen

# Create Turtle object
timmy = Turtle()  # You missed the '=' sign
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)

# Create Screen object
my_screen = Screen()
print(my_screen.canvheight)  # Fixed typo: should be canvheight
my_screen.exitonclick()
def greet(first_name, last_name):
    print(f"Hello {first_name}, {last_name}")
greet("aza", "Gul")
letters = ["a", "b", "c"]
while True:
    print(letters)
    break
for _ in range(8):   # to creat a red flower
    for _ in range(2): 
        my_turtle.forward(100)
        my_turtle.right(90)
    my_turtle.right(45)
    my_turtle.forward(130)
square_side = turtle.square()
for _ in range(4): # Turtle is moving to creat an triangle
    square_side.color("blue")
    square_side.forward(400)
    square_side.right(90)
