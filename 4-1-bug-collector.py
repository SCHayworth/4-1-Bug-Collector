# Program 4-1 Bug Collector
# Shaun Hayworth
# CIS 2
# 10-20-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/4-1-Bug-Collector

# This program prompts the user for an amount of bugs collected over a 5 day period
# and keeps a running total based on that amount.

# Initialize the accumulator total_bugs and set it to 0
total_bugs = 0

# Prompt user for the number of bugs collected each day and adds that total to
# total_bugs.
for day in range(1, 6):
    bugs_caught = int(input(f'Enter the number of bugss collected on day {day}: '))
    total_bugs += bugs_caught

# Display the final tally of bugs collected.
print(f'\nTotal bugs collected: {total_bugs}')
