starting_salary = int(input("Please enter the teacher's beginning salary: "))
percent_increase = (float(input("Please enter the yearly percentage increase: ")) / 100)
number_of_years_worked = list(range(1,(int(input("Please enter number of years the teacher has in schedule: ")) + 1)))
print("\n")
for year in number_of_years_worked:
    updated_salary = starting_salary*percent_increase
    newSalary = starting_salary+updated_salary
    startSalary = newSalary
    print("The teacher's year {} salary is  {:0.2f}".format(year, newSalary))
