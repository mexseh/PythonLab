text = "I'm pavan, studying BCA in Jain University"

print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Title Case:", text.title())
print("Swapcase:", text.swapcase())
print("Capitalize:", text.capitalize())
print("Length:", len(text))

words = text.split(" ")
print("Split:", words)

new_text = text.replace("BCA", "BCA-General")
print("Replace:", new_text)

position = text.index("Jain")
print("Index of 'Jain':", position)