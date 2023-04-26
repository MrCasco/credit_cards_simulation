from collections import OrderedDict
from User import User
from os import scandir


def run_transactions(input):
    users = {}
    format_quantity = lambda x: int(x.strip("$"))
    for transaction in input:
        action, info = transaction.split(" ", 1)
        if action == "Add":
            user, card, limit = info.split()
            users[user] = User(user, card, format_quantity(limit))
        else:
            user, amount = info.split()
            amount = format_quantity(amount)

            if action == "Charge":
                users[user].charge(amount)
            else:
                users[user].credit(amount)
    return users


def print_result_alphabetically(users):
    users = OrderedDict(sorted(users.items()))
    for user in users:
        print(
            f' - {user}: {"" if users[user].balance == "error" else "$"}{users[user].balance}'
        )


def run_tests():
    with scandir("./Tests") as files:
        for file in files:
            input = open(file, "r")
            results = run_transactions(input)
            print("Output from:", file.name)
            print_result_alphabetically(results)
            print('')


run_tests()
