#Dependencies
import csv
import os



# Files to Load
file_to_load = os.path.join('Resources','budget_data.csv')
file_to_output = os.path.join('budget_output.txt')


# Variables to use
total_months = 0
total_revenue = 0

prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []

# Reading of files
with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

   #making a loop
    for row in reader:

        # Calculating total_months
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])
        # print(row)

        # Calculations of average revenue changes
        revenue_change = int(row["Profit/Losses"]) - prev_revenue

        revenue_changes.append(int(row["Profit/Losses"])- prev_revenue)
      
        prev_revenue = int(row["Profit/Losses"])
        

        # Determining greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row["Date"]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row["Date"]





    
    revenue_changes.pop(0)
    revenue_avg = sum(revenue_changes) / (len(revenue_changes)-1)
    
   
    

    # Printing outputs
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    




# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total_revenue))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
