

def set_budget_limit():
    budget_amount = int(input("Set your total budget: €"))
    print("Your total budget is", budget_amount)
    return budget_amount


def enter_expenses():
    expenses_dictionary = {}
    while True:
        expense_name = input("Give a description of your expense: ")
        expense_amount = int(input("Enter the expense amount: €"))
        expenses_dictionary[f"{expense_name}"] = expense_amount
        enter_new_expense = input("Do you want to add another expense? (y/n) ").lower()
        if enter_new_expense == "n":
            break 
        else:
            continue
    return expenses_dictionary


def check_balance(budget, exp, exp_dict):
    balance = budget - exp 
    for x, y in exp_dict.items():
        print(f"{x}: €{y}")
    print("Your total expenditure is €", exp)
    print("Your total budget is €", budget)
    if balance < 0:
        print("You have exceeded your budget.")
    else:
        print(f"Your current balance is €{balance}")
    return balance






def create_budget():
    while True:
        total_budget = set_budget_limit()

        expenses = enter_expenses()
        expenditure = 0
        for i in expenses.values():
            expenditure = expenditure + i

        check_balance(total_budget, expenditure, expenses)
        replay_answer = input("Do you want to set a new budget (y/n)? ").lower()
        if replay_answer == "n":
            break
        else:
            continue

create_budget()