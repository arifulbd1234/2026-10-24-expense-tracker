"""
Day 18 - 2026-10-24
Tool: Simple Expense Tracker
What it does: Keeps a small list of daily expenses with categories,
adds them up in total and per category, and shows the biggest expense -
the basic maths behind tracking where your money goes each month.
Who it helps: Anyone budgeting household costs, students tracking
pocket money, or a small shop keeping an eye on daily spending.
"""


def add_expense(expenses, name, amount, category):
    """Add one expense (a dict) to the list and return the list."""
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    expenses.append({"name": name, "amount": round(amount, 2),
                     "category": category})
    return expenses


def total_spent(expenses):
    return round(sum(e["amount"] for e in expenses), 2)


def total_by_category(expenses):
    totals = {}
    for e in expenses:
        totals[e["category"]] = round(totals.get(e["category"], 0) + e["amount"], 2)
    return totals


def biggest_expense(expenses):
    if not expenses:
        return None
    return max(expenses, key=lambda e: e["amount"])


def remaining_budget(budget, expenses):
    return round(budget - total_spent(expenses), 2)


if __name__ == "__main__":
    my_expenses = []
    add_expense(my_expenses, "Rickshaw fare", 60, "Transport")
    add_expense(my_expenses, "Lunch", 180, "Food")
    add_expense(my_expenses, "Groceries", 850, "Food")
    add_expense(my_expenses, "Mobile recharge", 100, "Phone")

    print("Total spent today:", total_spent(my_expenses), "taka")
    print("By category:", total_by_category(my_expenses))
    big = biggest_expense(my_expenses)
    print("Biggest expense:", big["name"], "-", big["amount"], "taka")
    print("Left from a 1500 taka daily budget:",
          remaining_budget(1500, my_expenses), "taka")
