class Account():
    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_annual_interest_rate(self):
        return self.__annualInterestRate

    def set_annual_interest_rate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate / 100

    def get_monthly_interest_rate(self):
        monthly_interest_rate = self.__annualInterestRate / 12
        return monthly_interest_rate

    def get_monthly_interest(self, monthly_interest_rate):
        return self.__balance * monthly_interest_rate

    def withdraw(self, amount_to_withdraw):
        balance = self.__balance - amount_to_withdraw
        return balance

    def deposit(self, amount_to_deposit):
        new_balance = self.__balance + amount_to_deposit
        return new_balance



