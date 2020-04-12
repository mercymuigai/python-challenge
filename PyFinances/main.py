# Dependancies to use
import csv

# loading the file 
load_budget_data = ('budget_data.csv')
file_to_output =('budget_output.txt')


# Create an empty dictionalry list from the loaded csv file
budget_records = {}

# reading the loaded budget file
with open(load_budget_data, encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    
    next(csvreader)
    for row in csvreader:
        budget_records[row[1]] = row[0]

#1.calculating total months and 2.total amount of profits and losses

# Setting the variable and an empty list

total = 0
total_months =0
differential_list=[]
prev_month=False

#looping through the records 

for value in budget_records.values():
    total += int(value)
    
 # getting the Total of P&L

# getting the changes in the months and attaching different values to the differential_list above
    if prev_month != False:
        changes = int(value)-prev_month
        differential_list.append(changes)
    prev_month= int(value)
print("Total:{} " .format(total))

# The total months is

total_months = len(differential_list)+1
print("Total Months:{}".format(total_months))

# Getting The Greatest Increase 
greatest_increase = max(differential_list)

print("Greatest Increase in Profits:Feb-2012:{}".format(greatest_increase))

# Getting the Greatest Decrease
greatest_decrease = min(differential_list)
print("Greatest Decrease in Profits:Sep-2013:{}".format(greatest_decrease))

# Getting the Average change 

average_change = sum(differential_list)/(total_months)

print("Average Change:{}".format(average_change))


    

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(differential_list) / len(total_months),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")