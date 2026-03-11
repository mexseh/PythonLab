## Experiment Title

Experiment 4

## Aim

To write a program to demonstrate list and related functions in Python.

## Algorithm

1. Initialize two lists: `a = [1, 2, 3, 4]` and `b = [11, 12, 13, 14]`.
2. Append the value `10` to list `a` using `a.append(10)` and print `a`.
3. Extend list `a` with list `b` using `a.extend(b)` and print `a`.
4. Copy list `b` into `a` using `a = b.copy()` and print `a`.
5. Sort list `a` in descending order using `a.sort(reverse=True)` and print `a`.
6. Insert the value `10` at index `2` in `a` using `a.insert(2, 10)` and print `a`.
7. Remove the value `10` from `a` using `a.remove(10)` and print `a`.
8. Replace the slice `a[1:2]` with `[6, 7]` and print `a`.
9. Clear all elements from list `b` using `b.clear()` and print `b`.

## Output

Sample run:

```text
[1, 2, 3, 4, 10]
[1, 2, 3, 4, 10, 11, 12, 13, 14]
[11, 12, 13, 14]
[14, 13, 12, 11]
[14, 13, 10, 12, 11]
[14, 13, 12, 11]
[14, 6, 7, 12, 11]
[]
```