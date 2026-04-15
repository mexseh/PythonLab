## Experiment Title

Experiment 8

## Aim

To write a program to demonstrate regular expression operations in Python (`match`, `search`, `findall`, `sub`) and validate a date pattern.

## Algorithm

1. Import the `re` module.
2. Read `date` input in the format `DD/MM/YY`.
3. Initialize sample strings `text` and `code`, and pattern `Jain`.
4. Use `re.match()` to check whether `code` starts with `user`.
5. Use `re.search()` to check whether `text` contains `Jain`.
6. Use `re.findall()` to find all occurrences of `Jain` in `text`.
7. Use `re.sub()` to replace `Python` with `Java` in `text`.
8. Extract numbers from `code` using `re.findall("[0-9]+", code)`.
9. Validate `date` using the regex pattern `\d{2}/\d{2}/\d{2}$` with `re.match()`.
10. Print results for each step.

## Output

Sample run:

```text
Enter date (DD/MM/YY): 15/04/26
Code is valid
Text valid 
Text valid
I am studying in Jain University and I am learning Java
['1234']
Valid date