#import modules
import os
import csv

#initialize varialbles
election_csv=os.path.join('election_data.csv')

#need to set up a loop that compares the names in row [2] and if the names don't match,
#add name to list and to count how many times the name appears in the column


#lists to store data
#total_votes=0
#current_name=[]
#next_name=[]
#name_counts=[]

#open and read csv
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #read thru each row of data (skip header row)
    csv_header = next(csvfile)
    data=list(csvreader)
    #total number of votes
    total_votes=len(data)

    #read first name in list
    for row in data:
        #candidate_votes=something
        candidate_name=str(row[2])  
        next_name=str(row[2])+1        
        if candidate_name = next_name:
            print(candidate_name)
        else:
            print(next_name)


#print first couple of rows of output
print('Election Results')
print('-----------------------')
#count number of rows to determine total_months
print(f'Total Votes: {total_votes}')
print('-----------------------')
#print(current_name)
#list of candidates, percent of vote + total number of votes
#print({candidate_name}+float(percent_vote), int(candidate_votes))
print('-----------------------')
#winner, based on popular vote
#print({winner_name})
print('-----------------------')
    





    
