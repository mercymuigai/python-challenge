# Modules
import os
import csv
from statistics import mean

# Seting the  path for file
csvpath ="houston_election_data.csv"

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
           
    for entry in candidate:
        print(entry,"       : " ,(candidate[entry]/total_Vote)*100,"%", candidate[entry])
   
        
  
 # print('Houston Mayoral Election Results')
        
        print(f'total Cast Vote : {total_Vote}')
    



