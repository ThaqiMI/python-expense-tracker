expenses = []

def add_expense():
    print("Enter expense details:")
    amount = int(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        'number': len(expenses) + 1,
        'amount': amount,
        'category': category,
        'date': date
    }
    expenses.append(expense)
    print("Expense added!")


def view_expenses():
    if len(expenses) == 0:
        print("No Expenses Here!")
    else:
        for i in expenses:
            print(i["number"],"|", i["amount"],"|", i["category"],"|", i["date"])
        

def delete_expenses():
    if len(expenses)==0:
        print("No Expenses Here!")
        return
    
    view_expenses()
    del_no=int(input('What Expense You Want to Delete?:'))

    for expense in expenses:
        if expense['number'] == del_no:
            expenses.remove(expense)
            break

    n = 1
    for expense in expenses:
        expense['number'] = n
        n = n+1
    print("DONE!")
    view_expenses()




def total_expenses():
    total= 0
    for expense in expenses:
        total = float(expense['amount']) + total
    print("Total is:", total)


def show_menu():
    print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
    print('1. Add expense')
    print('2. View expense')
    print("3. Delete expense")
    print("4. Total")
    print("5. EXIT")


while True:
    show_menu()
    choice = input("choose (1-5): ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        delete_expenses()
    elif choice == "4":
        total_expenses()
    elif choice == "5":
        print("THANK YOU!")
        break
    else:
        print("INVALID CHOICE!")
