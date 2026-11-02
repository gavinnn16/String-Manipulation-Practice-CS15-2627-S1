string_to_process = "   sMitH, aLeX    "

# Expected output: "Alex Smith"


Clean_String = string_to_process.strip()
Name_parts = Clean_String.split(",")
Capitilized = Name_parts[0].title().strip(), Name_parts[1].title().strip()
Reordered_Name = Name_parts[1].title().strip(), Name_parts[0].title().strip()
Final_name = " ".join(Reordered_Name)
print(Clean_String)
print(Name_parts)
print(Capitilized)
print(Reordered_Name)
print(Final_name)
