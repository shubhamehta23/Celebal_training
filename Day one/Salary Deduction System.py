
salary = float(input("Enter salary: "))
late_days = int(input("Enter late days: "))
absent_days = int(input("Enter absent days: "))

deduction_percentage = 0

if late_days > 10:
    deduction_percentage = deduction_percentage + 10
elif late_days > 5:
    deduction_percentage = deduction_percentage + 5

if absent_days > 2:
    deduction_percentage = deduction_percentage + 5

deduction_amount = salary * deduction_percentage / 100
final_salary = salary - deduction_amount

print("Deduction:", deduction_amount)
print("Final salary:", final_salary)
