#import modules
import os
import csv



#initialize varialbles
election_csv=os.path.join('election_data.csv')


#open and read csv
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    names=[]
    for row in csvreader:
        csv_names = row[2]
        for i in csv_names:
            names.append(i)

    names_counted = []
    for i in names:
        x = names.count(i)
        names_counted.append((i,x))

    print(names_counted)

#write this to csv file
#with open('output.txt', 'wb') as f:
    #writer = csv.writer(f)  
    #writer.writerows(edgl)



    
