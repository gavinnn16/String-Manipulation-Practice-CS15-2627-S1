string_to_process = "t H e , T a L e :: O f , T w O :: c I t I e S"

# Expected Output: The Tale Of Two Cities

Cleaned_text = string_to_process.replace(",", " ").replace("::", " ").title()
Words = Cleaned_text.replace("  ", " ")
Title_Words = Cleaned_text.split("   ")
No_Space = Title_Words[0].replace(" ","")
No_Space2 = Title_Words[1].replace(" ", "")
No_Space3 = Title_Words[2].replace(" ", "")
No_Space4 = Title_Words[3].replace(" ", "")
No_Space5 = Title_Words[4].replace(" ", "")
Joined_Text = " ".join([No_Space, No_Space2, No_Space3, No_Space4, No_Space5]).title()
print(Cleaned_text)
print(Words)
print(Title_Words)
print(No_Space)
print(No_Space2)
print(No_Space3)
print(No_Space4)
print(No_Space5)
print(Joined_Text)