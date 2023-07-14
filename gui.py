from tkinter import *

def main():
    loan_amount = float(entry_loan_amount.get())
    interest_rate = float(entry_interest_rate.get()) / 100
    loan_term = int(entry_loan_term.get())

    down_payment = 0.2 * loan_amount
    principal = loan_amount - down_payment
    monthly_interest_rate = interest_rate / 12
    total_payments = loan_term * 12

    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
    result_label.config(text="Monthly Payment: $ {:.2f}".format(monthly_payment))

def calculate_monthly_payment():
    loan_amount = float(entry_loan_amount.get())
    interest_rate = float(entry_interest_rate.get()) / 100
    loan_term = int(entry_loan_term.get())

    down_payment = 0.2 * loan_amount
    principal = loan_amount - down_payment
    monthly_interest_rate = interest_rate / 12
    total_payments = loan_term * 12

    monthly_payment = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)
    result_label.config(text="Monthly Payment: $ {:.2f}".format(monthly_payment))

root = Tk()
root.title("Mortgage Calculator")

label_loan_amount = Label(root, text="Loan Amount:")
label_loan_amount.pack()
entry_loan_amount = Entry(root)
entry_loan_amount.pack()

label_interest_rate = Label(root, text="Interest Rate (%):")
label_interest_rate.pack()
entry_interest_rate = Entry(root)
entry_interest_rate.pack()

label_loan_term = Label(root, text="Loan Term (years):")
label_loan_term.pack()
entry_loan_term = Entry(root)
entry_loan_term.pack()

# Calculate Monthly Payment Button
calculate_monthly_payment_button = Button(root, text="Calculate Monthly Payment", command=calculate_monthly_payment)
calculate_monthly_payment_button.pack()

result_label = Label(root, text=" ")
result_label.pack()

root.mainloop()
