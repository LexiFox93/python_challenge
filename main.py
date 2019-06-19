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
current_pl=0
monthly_pl=0
highest_pl=0

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
        current_pl=int(row[1])-monthly_pl
        high_profit=high_profit+current_pl
        montly_pl=int(row[1])
    
        if highest_pl<current_pl:
            highest_pl=current_pl
            print(highest_pl)
            high_date=str(row[0])

        if low_loss>current_pl:
            low_loss=current_pl
            low_date=str(row[0])
    #calc avg_chg
    
avg_chg=(low_loss-highest_pl)/total_months

   
#print first couple of rows of output
print('Financial Analysis')
print('-----------------------')
#count number of rows to determine total_months
print(f'Total Months: {total_months}')
print(f'Net Total: ${total_pl}')
print(f'Average Change: $' + str(avg_chg))
#print greatest increase in profits with date
print(f'Greatest Increase in profits: $ {highest_pl} {high_date}')
#pring greatest decrease in profits with date
print(f'Greatest Decrease in profits: $ {low_loss} {low_date}')
