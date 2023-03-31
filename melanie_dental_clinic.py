CLEANING_RATE = 60
CAVITY_FILLING_RATE = 200
X_RAY_RATE = 100
TAX_RATE = 0.15
DISCOUNT_ABOVE_200 = 0.05
DISCOUNT_ABOVE_300 = 0.10

def get_patient_details():
    patient = input("Enter patient's name: ")
    cleaning = input("Was cleaning performed? (y/n): ")
    filling = input("Was cavity-filling performed? (y/n): ")
    xray = input("Was X-Ray performed? (y/n): ")
    return patient, cleaning, filling, xray

def calculate_sub_total(cleaning, filling, xray):
    sub_total = 0
    if cleaning == 'y':
        sub_total += CLEANING_RATE
    if filling == 'y':
        sub_total += CAVITY_FILLING_RATE
    if xray == 'y':
        sub_total += X_RAY_RATE
    return sub_total

def calculate_tax_due(sub_total):
    return sub_total * TAX_RATE

def calculate_gross_total(sub_total, tax_due):
    return sub_total + tax_due

def deduct_applicable_discount(gross_total):
    total_due = gross_total
    if gross_total > 300:
        total_due = gross_total * (1 - DISCOUNT_ABOVE_300)
    elif sub_total > 200:
        total_due = gross_total * (1 - DISCOUNT_ABOVE_200)
    return total_due

def print_receipt(patient, sub_total, tax_due, total_due):
    print("")
    print("            Melanie Dental Clinic             ")
    print("        *---------------------------*         ")
    print("  Receipt for patient:", patient)
    print("----------------------------------------------")
    print("  Subtotal:", sub_total)
    print("  Tax:", tax_due)
    print("----------------------------------------------")
    print("              Total:", total_due)

#MAIN PROGRAM FLOW
(patient, cleaning, filling, xray) = get_patient_details()
sub_total = calculate_sub_total(cleaning, filling, xray)
tax_due = calculate_tax_due(sub_total)
gross_total = calculate_gross_total(sub_total, tax_due)
total_due = deduct_applicable_discount(gross_total)
print_receipt(patient, sub_total, tax_due, total_due)


