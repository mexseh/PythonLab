## Experiment Title
Experiment 6

## Aim
To write a program to demonstrate dictionary and related functions in Python.

## Algorithm

1. Read `n`, the number of contacts to be stored.
2. Create an empty dictionary `dict = {}` and set `i = 0`.
3. Repeat while `i < n`:
   - Read contact name `x`.
   - Read phone number `y`.
   - Add the pair to the dictionary using `dict.update({x:y})`.
   - Increase `i` by 1.
4. Start an infinite loop to perform phone book operations.
5. Display the menu and read the user’s choice `c`.
6. If `c == 1`, print all entries using `dict.items()`.
7. If `c == 2`, print all names using `dict.keys()`.
8. If `c == 3`, print all phone numbers using `dict.values()`.
9. If `c == 4`, read a name and delete it using `del dict[d]`.
10. If `c == 5`, exit the program.
11. Otherwise print "Invalid choice".
12. Repeat until the user selects Exit.

## Output

Sample run:

```text
Enter number of contacts:3
Enter contact name:Pavan
Enter phone number:9876543210
Enter contact name:Sufi
Enter phone number:9123456780
Enter contact name:Dawood
Enter phone number:9988776655

Phone Book Menu:
1. Show all contacts
2. Show names
3. Show phone numbers
4. Remove contact
5. Exit
1
dict_items([('Pavan', '9876543210'), ('Sufi', '9123456780'), ('Dawood', '9988776655')])

Phone Book Menu:
1. Show all contacts
2. Show names
3. Show phone numbers
4. Remove contact
5. Exit
2
dict_keys(['Pavan', 'Sufi', 'Dawood'])

Phone Book Menu:
1. Show all contacts
2. Show names
3. Show phone numbers
4. Remove contact
5. Exit
5
```