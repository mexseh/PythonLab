n = int(input("Enter number of contacts: "))

dict = {}

i = 0
while i < n:
    x = input("Enter contact name: ")
    y = input("Enter phone number: ")
    dict.update({x: y})
    i += 1

while True:
    c = int(input("\nPhone Book Menu:\n1. Show all contacts\n2. Show names\n3. Show phone numbers\n4. Remove contact\n5. Exit\n\n"))

    if c == 1:
        print(dict.items())

    elif c == 2:
        print(dict.keys())

    elif c == 3:
        print(dict.values())

    elif c == 4:
        d = input("Enter the name to delete: ")
        del dict[d]

    elif c == 5:
        exit(1)

    else:
        print("Invalid choice")