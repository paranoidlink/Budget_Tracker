A simple Python-based budget tracker that allows users to input their income and expense transactions, view the balance, and save all transactions to a CSV file. This project helps users manage their finances by logging transactions and keeping track of their balance in real time.

Features

Add income and expense transactions
Automatically save transactions to a CSV file (budget.csv)
View the current balance based on added transactions
Restart an entry if a mistake is made
Handle invalid input and guide the user to correct mistakes
Data stored in CSV format for easy backup and portability

Usage

  Start a transaction: Enter start to input a new transaction (income or expense).
  View balance: Enter balance to see your current balance.
  Exit: Enter exit to save the data and exit the program.

When entering a transaction:

  You will be asked to input the type (income/expense).
  Provide a description for the transaction.
  Enter the amount.
  Choose a category for the transaction.

If you make a mistake while entering an amount, you can type restart to re-enter the value.

CSV Format

The application saves your transactions in a CSV file (budget.csv) with the following columns:

  Type: "income" or "expense"
  Description: Description of the transaction
  Amount: Amount of money for the transaction
  Category: Category of the transaction

The program ensures the file exists, and if it doesn't, it creates one with the necessary headers.
