string_to_process = "  18,27,35,20  "

# Expected Output:
# "Total: 100"
# "Average: 25.0"

isolated_numbers = string_to_process.strip().split(",")
first_number = int(isolated_numbers[0])
second_number = int(isolated_numbers[1])
third_number = int(isolated_numbers[2])
fourth_number = int(isolated_numbers[3])


total = first_number + second_number + third_number + fourth_number
average = (first_number + second_number + third_number + fourth_number)/4


print(isolated_numbers)
print(first_number)
print(second_number)
print(third_number)
print(fourth_number)
print(f"Total: {total}!")
print(f"Average: {average}!")