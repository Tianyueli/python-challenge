from pathlib import Path
import os
import csv

budget_file_path = os.path.join("Assignments","Module_3_Assignment","python-challenge","PyBank","Resources","budget_data.csv")
# Initiate variables

with open(budget_file_path) as budget_file:
    reader = csv.reader(budget_file,delimiter = ',')
    header = next(reader)
    max_increase = 0
    max_decrease =0
    total_profit = 0
    total_months = 0
    date = []
    profit_losses = []
    
    for row in reader: 
       total_months += 1
       total_profit += int(row[1])
    #    max_increase
       if int(row[1]) > max_increase:
              max_increase = int(row[1])
    #    max_decrease
       if int(row[1]) < max_decrease:
               max_decrease = int(row[1])

print("Total Months: ", total_months)
print("Total: $", total_profit)
print("Average Change: $", total_profit/total_months)
print("Greatest Increase in Profits: $", row[0], max_increase)
print("Greatest Decrease in Profits: $", row[0], max_decrease)



# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
            
