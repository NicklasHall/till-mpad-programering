def calculate_monthly_payment(Principal, annual_rate, years):
    monthy_rate =annual_rate/100/12
    Months=years*12
    payment = (Principal * monthy_rate*(1+monthy_rate)**Months) / ((1 + monthy_rate)**Months - 1)
    return payment


principal = float(input("Lånebelopp: "))
annual_rate = float(input("Årsränta (%): "))
years = int(input("Löptid (år): "))
payment = calculate_monthly_payment(principal, annual_rate, years)
print(f"Din månatliga betalning är: {payment:.2f} kr")






