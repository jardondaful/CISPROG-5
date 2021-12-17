import math

initial_population = int(input("Please enter the initial population of organisms: "))
growth_rate = float(input("\nPlease enter the growth rate: "))
hours_to_achieve_growth_rate = float(input("\nPlease enter the amount of hours it takes to acheve the growth rate: "))
hours_that_pass_by = float(input("\nPlease enter the amount of hours that passes by: "))
print("\nThe amount of organisms in " + str(hours_that_pass_by) + " hours will be " + str(math.floor(initial_population*growth_rate**(hours_that_pass_by/hours_to_achieve_growth_rate))))
