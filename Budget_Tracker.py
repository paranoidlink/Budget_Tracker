import csv
import sys

def Budget_Input(budget_list, transaction_type, description, amount, category):
    while transaction_type.lower() not in ["expense", "income"]:
        print("Please enter a valid transaction type either expense or income")
        transaction_type = input()
    
    while category == None:
        print("Please enter a category for this transaction")
        category = input()

    while description == None:
        print("Please enter a valid description for this transaction")
        description = input()

    while True:
        if isinstance(amount, str) and amount.lower() == "restart":
            return budget_list
        try:
            amount = float(amount)
            if transaction_type == "income" and amount <= 0:
                    print("Lower than 0 error \n Please enter a valid number greater than 0 or enter restart if you've made a mistake")
                    amount = input()
            elif transaction_type == "expense" and amount >= 0:
                print("Greater than 0 error \n Please enter a valid negative number for this transaction or enter restart if you've made a mistake")
                amount = input()
            else:
                break
        except ValueError:
            print("amount entered is not a number please enter a valid number or enter restart if you've made a mistake")
            amount = input()

    budget_entry = [transaction_type, description, amount, category]
    budget_list.append(budget_entry)
    return budget_list

def Get_Input():
    print("Please enter what type of transaction you'd like to perform either \'expense\' or  \'income\' or enter \'exit\' to quit the")
    transaction_type = input()
    print("Please enter a description for this transaction")
    description = input()
    print("Please enter an amount for this transaction")
    while True:
        try:
            amount = float(input())
            break
        except ValueError:
            print("Please enter a valid number")
    print("Please enter a category for this transaction")
    category = input()
    return transaction_type,description,amount,category

def Save_File(budget_list):
    with open("budget.csv", "a", newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Type", "Description", "Amount", "Category"])

        writer.writerows(budget_list)

budget_list = []
print("Hello welcome to the budget tracker enter \'start\' to begin or \'exit\' to exit the program")
while True:
    responce = input()
    if responce.lower() == "exit":
        Save_File(budget_list)
        sys.exit("Data has been saved to budget.csv now closing the program")
    elif responce.lower() == "start":
        transaction_type,description,amount,category = Get_Input()
        Budget_Input(budget_list, transaction_type, description, amount, category)
    print("Your updated budget list is " + str(budget_list) + "\nif you would like to add more enter \'start\' again if you'd like to exit enter \'exit\'")

