#Import Modules

import os
import csv

#variables / initial states
candidate = []
results = []
votes = []
vote_count = {}
percentage = {}

total_votes = 0
count_votes = 0
count_candidates = 0

#create a file path
PyPoll_csv = os.path.join('C:/BootCamp in class/ku-edw-data-pt-07-2020-u-c/02-Homework/03-Python/Instructions/PyPoll/Resources',"election_data.csv")

#read csv_reader
with open (PyPoll_csv,newline='') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    csv_header = next(csv_reader)
    line_count = 0

#cycle through data and append candidate list with candidate increases vote counter by 1
    
    for row in csv_reader:
        total_votes += 1
        if row[2] in candidate and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

#else create new spot in list for candidate
        else:
            candidate.append(row[2])
            vote_count[row[2]] = 1


#Percentage calculation
for key,value in vote_count.items():
    percentage[key] = str(round((value/total_votes)*100,3)) + "% ("+str(value)+ ")"


#winner
winner = max(vote_count.keys(), key=(lambda k: vote_count[k]))


#output to textfile
with open('output_election.txt','w',newline='') as textfile:
    print('Election Results', file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Total Votes: {total_votes}', file = textfile)
    print('----------------------------------',file = textfile)
    for i in range(count_candidates):
        print(f'{results[i]}: {round(percentage[i], 2)}% ({votes[i]})', file=textfile)
    print(f'Percentage: {percentage}', file = textfile)
    print('----------------------------------',file = textfile)
    print(f'Winner: {winner}', file = textfile)
    print('----------------------------------', file = textfile)


with open('output_election.txt',newline='')as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    for row in csvreader:
        print(row) 
