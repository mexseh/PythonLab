## Experiment Title

Experiment 2

## Aim

To write a program to implement control flow statements and looping statements in Python.

# Algorithm

1. Read `n`, the number of players from the user.
2. Use a `for` loop to repeat the process for `n` players.
3. Display the player number.
4. Read `runs`, `balls`, `fours`, `sixes`, `wickets`, `runs_conceded`, `overs`, and `catches`.
5. Calculate strike rate `sr = (runs / balls) * 100`.
6. Calculate economy rate `er = runs_conceded / overs`.
7. Based on `runs` and `sr`, classify the batting performance as **Excellent Batter**, **Good Batter**, **Average Batter**, or **Poor Batter**.
8. Based on `wickets` and `er`, classify the bowling performance as **Excellent Bowler**, **Good Bowler**, **Average Bowler**, or **Poor Bowler**.
9. Based on `catches`, classify the fielding performance as **Outstanding Fielder**, **Active Fielder**, or **Needs Improvement**.
10. Using the batting and bowling results, determine the overall performance as **Star All-Rounder**, **Strong All-Rounder**, **Supporting All-Rounder**, or **Needs Improvement**.
11. Print the strike rate, economy, batting, bowling, fielding, and overall performance.
12. Repeat until all `n` players are processed.

## Output

```text
Enter the number of players: 1

Player 1
Enter the runs scored: 65
Enter the number of balls faced: 40
Enter the number of 4s scored: 6
Enter the number of 6s scored: 2
Enter the number of wickets taken: 3
Enter the number of runs conceded: 24
Enter the number of overs bowled: 4
Enter the number of catches taken: 1

Strike Rate: 162.5
Economy: 6.0
Batting: Excellent Batter
Bowling: Excellent Bowler
Fielding: Active Fielder
Overall: Star All-Rounder
```
