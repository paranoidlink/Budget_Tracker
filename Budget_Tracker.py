import csv
import sys
def Save_File(budget_list):
    with open("budget.csv", "a", newline='') as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Type", "Description", "Amount", "Category"])

        writer.writerows(budget_list)

def Validation_Helper(criteria):
    while criteria == "":
        print("Please enter a valid " + criteria + " for this transaction")
        criteria = input()
        return criteria
    
def Type_Helper(transaction_type):
    while transaction_type.lower() not in ["expense", "income"]:
        print("Please enter a valid transaction type either expense or income")
        transaction_type = input()
        return transaction_type

def Amount_Helper(amount, transaction_type):
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
                return amount
        except ValueError:
            print("amount entered is not a number please enter a valid number or enter restart if you've made a mistake")
            amount = input()


def Budget_Input(budget_list, transaction_type, description, amount, category):

    transaction_type = Type_Helper(transaction_type)
    category = Validation_Helper(category)
    description = Validation_Helper(description)
    amount = Amount_Helper(amount, transaction_type)

    budget_entry = [transaction_type, description, amount, category]
    budget_list.append(budget_entry)
    Save_File([budget_entry])
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

def balance_checker(budget_list):
    result = 0
    if budget_list == []:
        print("Please add some items to todays list before checking the balance")
        return 0
    for item in budget_list:
        result += item[2]
    return result

budget_list = []
print("Hello welcome to the budget tracker enter \'start\' to begin or \'exit\' to exit the program")
while True:
    response = input()
    if response.lower() == "exit":
        sys.exit("Thank you for using the budget tracker your data has been saved in the same folder as this program")
    elif response.lower() == "balance":
        balance = balance_checker(budget_list)
        print(f"Todays balance is £{balance:.2f}")
    elif response.lower() == "start":
        transaction_type,description,amount,category = Get_Input()
        Budget_Input(budget_list, transaction_type, description, amount, category)
    else:
        print("Please enter a valid option of either \'start\', \'budget\' or \'exit\'")
    print("Your updated budget list is " + str(budget_list) + "\nif you would like to add more enter \'start\' again \nIf you'd like to check your balance for todays inputs enter \'balance\'\nIf you'd like to exit enter \'exit\'")

