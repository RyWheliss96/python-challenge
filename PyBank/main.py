# First we'll import the os module
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#Initialize list of changes
changeList = []

#Initialize greatest Increase and Decrease Variables
greatestIncrease = ["",0]
greatestDecrease = ["",0]
changeValue = 0

#Open CSV File
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    #Look at first row
    csvRow1 = next(csvreader)
    #increment to add 1st month
    totalMonths = 1
    #initialize variable for total P/L
    totalPL = int(csvRow1[1])
    #initialize variable to calculate change
    oldPLchange = int(csvRow1[1])
    
    # Read each row of data after the header
    for row in csvreader:
        #increment to count # months
        totalMonths = totalMonths + 1
        
        #add PL each month to total
        totalPL = totalPL + int(row[1])
        
        #grab change value to compare and see if greates or smallest
        changeValue = int(row[1])-oldPLchange
        
        #if statement for greatest increase
        if greatestIncrease[1]<changeValue:
            greatestIncrease[0] = row[0]
            greatestIncrease[1]= changeValue
        
        #if statement for greatest decrease
        if greatestDecrease[1]>changeValue:
            greatestDecrease[0] = row[0]
            greatestDecrease[1]= changeValue
        
        #add PL Change to list for use later
        changeList.append(changeValue)
        oldPLchange = int(row[1])

    
    #Print to command line
    print("Financial Analysis")
    print("----------------------------")
    #total months
    print("Total Months: " + str(totalMonths))
    #total Profit/Losses
    print("Total: $" + str(totalPL))
    #he average of the changes in "Profit/Losses" over the entire period with formatting
    print("Average Change: $" + str(round(sum(changeList)/len(changeList), 2)))
    #The greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase in Profits: "+ greatestIncrease[0] + " ($" + str(greatestIncrease[1])+ ")")
    #The greatest decrease in profits (date and amount) over the entire period
    print("Greatest Decrease in Profits: "+ greatestDecrease[0] + " ($" + str(greatestDecrease[1])+ ")")

#file path for txt file
file = 'analysis/output.txt'

# Open the file in "write" mode ('w') and store the contents in the variable "text"
with open(file, 'w') as text:
    
    #write each line that is printed above include \n for new row
    text.write("Financial Analysis \n")
    text.write("---------------------------- \n")
    text.write("Total Months: " + str(totalMonths) + "\n")
    text.write("Total: $" + str(totalPL) + "\n")
    text.write("Average Change: $" + str(round(sum(changeList)/len(changeList), 2))+"\n")
    text.write("Greatest Increase in Profits: "+ greatestIncrease[0] + " ($" + str(greatestIncrease[1])+ ") \n")
    text.write("Greatest Decrease in Profits: "+ greatestDecrease[0] + " ($" + str(greatestDecrease[1])+ ") \n")
    
