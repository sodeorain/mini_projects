
#modularise it
# naming of variables ... inputs of function vs body of function 
# DRY... expenditure created twice 
# is dict best way to organise this ? 
# best way to handle y / n questions?
# nested while
# debugger is really nice
# foucsing more on data science use cases... Shiny, etc. 
def set_budget_limit():
    budget_amount = int(input("Set your total budget: €"))
    print("Your total budget is €", budget_amount)
    return budget_amount



def enter_expenses(budget):
    expenses_dictionary = {}
    while True:
        expense_name = input("Give a description of your expense: ")
        expense_amount = int(input("Enter the expense amount: €"))
        expenses_dictionary[f"{expense_name}"] = expense_amount
        total_expenditure = tally_expenditure(expenses_dictionary)
        if total_expenditure > budget:
            print("You have exceeded your budget. The expense cannot be added")
            expenses_dictionary.pop(expense_name)
            continue
        else:
            enter_new_expense = input("Do you want to add another expense? (y/n) ").lower()
            if enter_new_expense == "n":
                break 
            else:
                continue
    return expenses_dictionary

def tally_expenditure(dictionary):
    expenditure = 0
    for i in dictionary.values():
        expenditure = expenditure + i
    return expenditure
    


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



def prompt_user_new_budget():
    while True:
        replay_answer = input("Do you want to set a new budget (y/n)? ").lower()
        if replay_answer in ["y", "n"]:
            return replay_answer
        else:
            print("Invalid choice.")



def create_budget():
    while True:
        total_budget = set_budget_limit()

        expenses_dictionary = enter_expenses(total_budget)
        total_expenditure = tally_expenditure(expenses_dictionary)
        check_balance(total_budget, total_expenditure, expenses_dictionary)
        answer = prompt_user_new_budget()
        if answer == "n":
            break
        else:
            continue 

create_budget()

#lists, tuples 
# for loop:  break, continue 
# while True

# Python scope
# Python math
# Python try except
# Python user input 
# Python user formatting