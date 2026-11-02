string_to_process = "eggs,cheese,milk,bread,cereal"

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"
uppercase_text = string_to_process.upper()
replaced_text = uppercase_text.replace(",", " | ")
print(uppercase_text)
print(replaced_text)
