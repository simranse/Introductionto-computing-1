#2.Tax
grossIncome=float(input("Enter the gross income:"))
dependent=int(input("Enter the number of dependents:"))
TaxableIncome=grossIncome-10000-(3000*dependent)
Tax=TaxableIncome*0.20
print("The income tax is:",Tax)


