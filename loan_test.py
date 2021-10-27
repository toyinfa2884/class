from classes_and_objects_chp7.loan import Loan


def main():
    annual_interest_rate = eval(input("Enter yearly interest rate:"))
    number_of_years = eval(input("Enter number of years as an integer:"))
    loan_amount = eval(input("Enter loan amount:"))
    borrower = input("Enter borrower's name:")

    # create a loan object
    loan = Loan(annual_interest_rate, number_of_years, loan_amount, borrower)

    print("The loan is for", loan.get_borrower())
    print("The monthly payment is", format(loan.get_monthly_payment(), ".2f"))
    print("The total payment is", format(loan.get_total_payment(), ".2f"))


main()
