import re

date = input("Enter date (DD/MM/YY): ")

text = "I am studying in Jain University and I am learning Python"
code = "user1234"

word = "Jain"

# match
res = re.match("user", code)
if res:
    print("Code is valid")
else:
    print("Invalid code")

# search
res = re.search(word, text)
if res:
    print("Text valid")
else:
    print("Text invalid")

# findall
res = re.findall(word, text)
if res:
    print("Text valid")
else:
    print("Invalid text")

# replace
new = re.sub("Python", "Java", text)
print(new)

# extract numbers
nums = re.findall("[0-9]+", code)
print(nums)

# date validation
pattern = r"\d{2}/\d{2}/\d{2}$"
check = re.match(pattern, date)

if check:
    print("Valid date")
else:
    print("Invalid date")