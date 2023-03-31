CLEANING_RATE = 60
CAVITY_FILLING_RATE = 200
X_RAY_RATE = 100
TAX_RATE = 0.15
DISCOUNT_ABOVE_200 = 0.05
DISCOUNT_ABOVE_300 = 0.10

patient = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
filling = input("Was cavity-filling performed? (y/n): ")
xray = input("Was X-Ray performed? (y/n): ")

sub_total = 0

if cleaning == 'y':
    sub_total += CLEANING_RATE
if filling == 'y':
    sub_total += CAVITY_FILLING_RATE
if xray == 'y':
    sub_total += X_RAY_RATE

tax_due = sub_total * TAX_RATE

total = sub_total + tax_due

if sub_total > 300:
    total *= 1 - DISCOUNT_ABOVE_300
elif sub_total > 200:
    total *= 1 - DISCOUNT_ABOVE_200

print("")
print("            Melanie Dental Clinic             ")
print("        *---------------------------*         ")
print("  Receipt for patient:", patient)
print("----------------------------------------------")
print("  Subtotal:", sub_total)
print("  Tax:", tax_due)
print("----------------------------------------------")
print("              Total:", total)
