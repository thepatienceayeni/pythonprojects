def financial_statement():
    percentage_tracker = 100
    percentage_marketing = 0
    percentage_operational_expenses = 0
    
    
    income = input ("Enter your amount given:")
    print(income)

    percentage_marketing = input("(%) marketing:")
        
    percentage_tracker -= percentage_marketing

    percentage_operational_expenses = input("(%) operational expenses: ")

    cost_per_customer = input("(ghs) What does it cost to acquire a customer: ")

    marketing = income * (percentage_marketing / 100)
    operational_expenses = income * (percentage_operational_expenses / 100)
    customer_acquisition = income - (marketing + operational_expenses)
    
    customers_aquisition_count = customer_acquisition / cost_per_customer

    print("____AHMED'S FINANCIAL STATEMENT____ \n\n")

    print(f"Marketing budget: {marketing} \n\n Operational expenses: {operational_expenses} \n\n Customer acquisition: {customer_acquisition} \n\n Number of customers to acquire: {customers_aquisition_count}")
