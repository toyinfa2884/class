from classes_and_objects_chp7.account import Account


def main():
    account1 = Account(1122, 20.000, 0.045)
    account1.withdraw(2500)
    print("Balance is", account1.get_balance())
    account1.deposit(3000)
    print("Balance is", account1.get_balance())


main()