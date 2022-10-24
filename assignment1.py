def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return val
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return val
        except ValueError:
            print("Haba Chale, Oya try again")
            receive_input()

def receive_input():
    input1 = input("Hi, pick a number: ")
    input2 = input("Pick another number: ")
    num1 = check_user_input(input1)
    num2 = check_user_input(input2)
    return num1, num2

num1, num2 = receive_input()
sum = num1 + num2

print("The sum is:", sum)
print("Nice job!")
    
    
