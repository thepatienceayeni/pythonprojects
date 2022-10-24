# With a for & while loop, print even numbers from 1 - 30
for x in range (0, 31):
    if (x % 2 == 0):
      print (x) 
print ("Congratulation! You've come to the end of the first question")

# With a for & while loop, print odd numbers from 1 - 30  
x = 1
while x <=30: # Using while
     print(x)
     x += 2  


  # Ahmed, an EiT Fellow, has been given an amount of GHC 50,000 for his capstone project 

def validate_number(num):
        num = float(num)
        return num

percentage_limit = 100
percentage_marketing = 0
percentage_operational_expenses = 0
    
    
income = int(input ("Enter your amount given:"))
print(income)

percentage_marketing = int(input ("Enter percentage spent on marketing:"))
        
percentage_limit -= percentage_marketing

percentage_operational_expenses = int(input("Enter percentage spent on operational expenses: "))

cost_per_customer = int(input("(ghs) What does it cost to acquire a customer: "))

marketing = income * (percentage_marketing / 100)
operational_expenses = income * (percentage_operational_expenses / 100)
customer_acquisition = income - (marketing + operational_expenses)
    
customers_aquisition_count = customer_acquisition / cost_per_customer

print("____AHMED'S FINANCIAL STATEMENT____ \n\n")

print(f"Marketing budget: {marketing}")
print(f"Operational expenses: {operational_expenses}")
print(f"Customer acquisition: {customer_acquisition}")
print (f"Number of customers that would be acquired: {customers_aquisition_count}")
print (f"\n\nYou've completed your calculation!")

  
