#import modules
import os
import csv

#initialize varialble
budget_csv=os.path.join('budget_data.csv')
total_pl=0
total_months=0
avg_chg=0
high_profit=0
low_loss=0
high_date=0
low_date=0
next_profit=0
next_loss=0

#open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read thru each row of data (skip header row)
    csv_header = next(csvfile)
    data=list(csvreader)
    total_months=len(data)

    #get total_pl
    for row in data:
        total_pl += int(row[1])
        #store value in high profit if greater than high profit
        if high_profit>int(row[1]):
            high_profit=high_profit-int(row[1])
            high_date=str(row[0])

        if low_loss>int(row[1]):
            low_loss=int(row[1])
            low_date=str(row[0])
    #calc avg_chg
    
avg_chg=total_pl/total_months

   
#print first couple of rows of output
print('Financial Analysis')
print('-----------------------')
#count number of rows to determine total_months
print(f'Total Months: {total_months}')
print(f'Net Total: ${total_pl}')
print(f'Average Change: $' + str(avg_chg))
#print greatest increase in profits with date
print(f'Greatest Increase in proftis: $ {high_profit} {high_date}')
#pring greatest decrease in profits with date
print(f'Greatest Decrease in proftis: $ {low_loss} {low_date}')
