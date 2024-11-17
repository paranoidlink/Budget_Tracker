def Budget_Input(budget_list, type, description, amount, catagory):
    while type.lower() not in ["expense", "income"]:
        print("Please enter a valid transaction type either expense or income")
        type = input()
    
    while catagory == None:
        print("Please enter a category for this transaction")
        catagory = input()

    while description == None:
        print("Please enter a valid description for this transaction")
        description = input()

    while True:
        if isinstance(amount, str) and amount.lower() == "restart":
            return None
        try:
            amount = float(amount)
            if type == "income":
                if amount <= 0:
                    print("Amount lower than 0 error \n Please enter a valid number greater than 0 or enter restart if you've made a mistake")
                    amount = input()
                else:
                    break
            if type == "expense":
                if amount >= 0:
                    print("Greater than 0 error \n Please enter a valid negative number for this transaction or enter restart if you've made a mistake")
                    amount = input()
                else:
                    break
        except ValueError:
            print("amount entered is not a number please enter a valid number or enter restart if you've made a mistake")
            amount = input()

    budget_entry = [type, description, amount, catagory]
    budget_list.append(budget_entry)
    return budget_list

def Get_Input():
    print("Please enter what type of transaction you'd like to perform either \'expense\' or  \'income\'")
    type = input()
    print("Please enter a description for this transaction")
    description = input()
    print("Please enter an amount for this transaction")
    while True:
        try:
            amount = float(input())
            break
        except ValueError:
            print("Please enter a valid number")
    print("Please enter a catagory for this transaction")
    catagory = input()
    return type,description,amount,catagory