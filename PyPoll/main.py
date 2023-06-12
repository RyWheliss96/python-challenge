# First we'll import the os module
import os

# Module for reading CSV files
import csv

#path for csvfile
csvpath = os.path.join('Resources', 'election_data.csv')

#initialize variables
totalVotes = 0
candidate = []
votes = []

#Open csvfile
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        #increment total votes
        totalVotes = totalVotes + 1
        #Count votes or add new candidate
        if row[2] in candidate:
            votes[candidate.index(row[2])] = votes[candidate.index(row[2])] + 1
        else:
            candidate.append(row[2])
            votes.append(1)
            
    #Print to Command Line
    print("Election Results")
    print("----------------------------")
    #The total number of votes cast
    print("Total Votes: " + str(totalVotes))
    print("----------------------------")
    #initialize winner
    winner = candidate[0]
    winnerVotes = votes[0]
    #print every candidate
    for i in range(len(candidate)):
        print(candidate[i-1] + ": " + str(round(votes[i-1]/totalVotes * 100, 3)) + "% ("+str(votes[i-1])+")")
        #update winner if next candidate has more votes
        if votes[i-1]>winnerVotes:
            winner = candidate[i-1]
            winnerVotes = votes[i-1]
    print("----------------------------")
    #The winner of the election based on popular vote
    print("Winner: " + str(winner))
    print("----------------------------")


file = 'analysis/output.txt'

# Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:
    
    #write each line that is printed above
    text.write("Financial Analysis \n")
    text.write("---------------------------- \n")
    text.write("Total Votes: " + str(totalVotes) + "\n")
    text.write("---------------------------- \n")
    #write every candidate
    for i in range(len(candidate)):
        text.write(candidate[i-1] + ": " + str(round(votes[i-1]/totalVotes * 100, 3)) + "% ("+str(votes[i-1])+") \n")
    text.write("---------------------------- \n")
    text.write("Winner: " + str(winner)+ "\n")
    text.write("---------------------------- \n")
