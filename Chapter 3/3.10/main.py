#Please make the compiler cover entire screen before using the code
total_price = float(input("Please enter the cost of the item: "))
print("")
remaining_price = (total_price * 0.9)
monthly_payment = remaining_price * 0.05
interest_owed = remaining_price * (.12/12.0)
principal = monthly_payment - interest_owed
month = 0
print("Month       Total Owed       Principal Owed      Interest Owed    Payment for Month    Balance Remaining")
while remaining_price > 0:
    month += 1
    remaining_price -= principal
    interest_owed = remaining_price * (.12/12.0)
    principal = monthly_payment - interest_owed
    print("%0d%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, total_price, interest_owed, principal, monthly_payment, remaining_price))
