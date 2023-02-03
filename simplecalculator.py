print("Simple Calculator")
print("Enter the first value: ")

number_1 = int(input())

print("First value is: " + str(number_1))

print("Enter the second value: ")

number_2 = int(input())

print("Second value is: " + str(number_2))

print("Select the operation you wish to perform: ")
print("1: Enter 1 for addition")
print("2: Enter 2 for subtraction")
print("3: Enter 3 for multiplication")
print("4: Enter 4 for division")

selection = int(input())
print("\nYour answer is: ")
if(selection==1):
    print(number_1 + number_2)
elif(selection==2):
    print(number_1 - number_2)
elif(selection==3):
    print(number_1 * number_2)
elif(selection==4):
    print(number_1 / number_2)
else:
    print("Invalid input- only integers accepted!")
