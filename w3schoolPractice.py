#python match statement---> select one of many code blocks to run
equation = 1
match equation:
    case 1:
        print(3 + 6)
    case 2:
        print(1 +6)
    case 3:
        print(5 + 6)
    case 4:
        print(7+6)
command = input("Enter a coomand (start/stop/pause/exit):")
match command:
    case "start":
        print("Game started")   
    case "stop":
        print("game stopped")
    case "pause":
        print("game paused")
    case "exit":
        print("Goodbye!")
    case _:
        print("Invalid coommand, try gain")
month = 5
day = 3
match day :
    case 1|2|3|4|5 if month == 4:
        print("it's weekday in April")
    case 1|2|3|4|5 if month == 5:
        print("it's a week way in July")
    case 6|7 if month == 5:
        print("I love weekends in April")
    
    case _:
        print("Its summer day")
#password with while loops
password = "aza@357"
attempt = ""
while attempt != password:
    attempt = input("Enter your password:")
print("access granted")
#while loop with countdown
count = 10
while count > 0:
    print(count)
    count -= 1
    if count == 3:
        print("Get ready to celebrate!")
        continue
    print("Happy New Year!") 
else:
    print("countdown complete")  
names = ["Alic", "Bob", "Charlie"]
for name in names:
    print(f"Hello{name}, come to my goodbye party")
with open("Input/Names/invited_names.txt", 'r') as file:
    names = file.readlines()  # list of names
    for name in names:
        print(f"Hello {name}, come to my party")
    txt = f"Dear {name}, Are you coming to my party?"
txt = f"The price is 40$"
print(txt)