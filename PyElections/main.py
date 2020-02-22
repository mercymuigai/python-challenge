
import os
import csv
from statistics import mean
import collections
import operator

# Seting the  path for file
csvpath = os.path.join('houston_election_data.csv')
file_to_output = os.path.join('houston_election.csv')

# Opening the CSV
with open(csvpath, newline='', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

#making a dictionary keys and looping
    candidate = {}
    total_Vote  = 0
    for row in reader:
        total_Vote += 1
        if row[0] not in candidate.keys():
            candidate[row[0]] = 1
        else:
           candidate[row[0]] += 1
        candidate_sorted = sorted(candidate.items(), key=operator.itemgetter(1),reverse=True)

    print()
    print("--------------------------------------------------------")
    print("Houston Mayoral Election Results")
    print("--------------------------------------------------------")
    print("Total Cast Votes: " + str('{:,}'.format(total_Vote)))
    print("--------------------------------------------------------")
    for r in candidate_sorted:
        print(str(r[0]) + "  (" + str('{:,}'.format(r[1])) + ")" + " : " + str('{0:.2%}'.format((r[1])/total_Vote)) )
    print("--------------------------------------------------------")
    print ("1st Advancing Candidate: " + str(candidate_sorted[0]) + "\n" "2nd Advancing Candidate: "+ str(candidate_sorted[1]))
    print("--------------------------------------------------------")

# Output Files
with open(file_to_output, 'w') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Candidate Name", "Total Votes Received", "Percentage of Votes Received"])
    for r in candidate_sorted:
        #writer.writerow( str((r[0])) + str((r[1])) + str(((r[1])/total_Vote)))
        writer.writerow(r)
    writer.writerow(["1st Advancing Candidate :", str(candidate_sorted[0])])
    writer.writerow(["2nd Advancing Candidate :", str(candidate_sorted[1])])


 




