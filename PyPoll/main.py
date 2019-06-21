#import modules
import os
import csv

#initialize varialbles
election_csv=os.path.join('election_data.csv')

#need to set up a loop that compares the names in row [2] and if the names don't match,
#add name to list and to count how many times the name appears in the column

#unable to find anything in google that will explain to me how to do this.......

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

    #loop to count names
    #for row in data:
        #current_name=str(row[])
        #next_name=str((row[2])+1)
        #new_name=next_name
        #next_name=str(row[2])

        #if current_name == next_name:
            #candidate_name=current_name
            #print(candidate_name)
        #else:
            #print(next_name)
           

#loop to count how many times each name is counted
##for i in names:
    #x=names.count(i)
    #names_counted.append((i,x))


    #for row in csvreader:
        #candidate = row[2]
        #votes[candidate] += 1

    #loop thru rows
    #look for candidate names
    #print candidate name and add to counter
    #else print new candidate & add to their counter
    #I have no idea how to do any of this so I guess I'm getting an F on this homework
    #if candidates row[2]
    #print(candidates)


#print first couple of rows of output
print('Election Results')
print('-----------------------')
#count number of rows to determine total_months
print(f'Total Votes: {total_votes}')
print('-----------------------')
#print(current_name)
#list of candidates
#print(words + words_counted)
#total votes for each candidate
#percentage of votes for each candidate
#winner, based on popular vote