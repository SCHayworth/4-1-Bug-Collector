# Scope
A bug collector collects bugs every day for five days. Write a program that keeps a running total of the number of bugs collected during the five days. The loops should ask for the number of bugs collected for each day, and when the loop is finished, the program should display the total number of the bugs collected.

### SAMPLE RUN:

    Enter the number of bugs collected today:  1
    Enter the number of bugs collected today:  2
    Enter the number of bugs collected today:  3
    Enter the number of bugs collected today:  4
    Enter the number of bugs collected today:  5

    Total bugs collected:  15

# Pseudocode

    Set accumulator = 0
    for each of 5 days
      prompt user for the number of bugs found that day
      increase accumulator by that amount
    print the value of the accumulator
