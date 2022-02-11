import random

cashFlows = []
rates = []
values = []
periods = []


period = random.randint(1,100)

def formula(cashFlow,rate,periods):
    rate = rate / 100
    return cashFlow / (1+rate)**periods
    
for i in range(period):
    cashFlow = random.randint(1000,5000)
    rate = random.randint(1,100)
    value = float(formula(cashFlow,rate,i+1))
    periods.append(i+1)
    cashFlows.append(cashFlow)
    rates.append(rate)
    values.append(value)
    

sum_of_values = 0

for i in range(len(values)):
    print(f"{i+1} ==> Value: {values[i]} && Cash Flow: {cashFlows[i]} && Rate: %{rates[i]}")
    sum_of_values+=values[i]

print()
print(f"Total Values of DCF Diagram: {sum_of_values}")    

temp_values = values
values.sort()

print()

for i in range(len(temp_values)):
    if temp_values[i] == values[len(values)-1]:
        print(f"Period: {periods[i]}")
        print(f"Best Value: {values[len(values)-1]}")
        print(f"Best value of Cash Flow: {cashFlows[i]}")
        print(f"Best value of Rate: %{rates[i]}")
        break
print()

for i in range(len(temp_values)):
    if temp_values[i] == values[0]:
        print(f"Period: {periods[i]}")
        print(f"Lowest Value: {values[0]}")
        print(f"Lowest value of Cash Flow: {cashFlows[i]}")
        print(f"Lowest value of Rate: %{rates[i]}")
        break









