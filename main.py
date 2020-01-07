# @TODO: Import libraries
import csv
from pathlib import Path

#Print Current Working Directory 
print(f"Current Working Directory: {Path.cwd()}")

#Set file path 
csvpath = Path('Python/gitlab/CU-NYC-FIN-PT-12-2019-U-C/Homework/02-Python/Instructions/PyBank/Resources/budget_data.csv')

#Intialize Dates, Profit/Losses, and Monthly Change
dates = []
profit_losses = []
monthly_chg = []

#Intialize Line Number Variable 
line_num = 0 

#Open the input path as file object
with open (csvpath,'r')as csvfile:
    #Pass csv file to csvreader
    csvreader = csv.reader(csvfile, delimiter=',')
    # Go to next row from start and iterate as line number 1
    header = next(csvreader)
    line_num += 1
    #Print Header
    print(f"{header} <---- HEADER")
    for row in csvreader: 
        #Print Row
        print(row)
        #Set Months 
        month = (row[0])
        #Append Months 
        dates.append(month)
        #Set Profit/Loss Variable equal to the value in 2nd row
        profit_loss = int(row[1])
        #Append the row Profit/Loss Value 
        profit_losses.append(profit_loss)

#Intitaliaze metric variables
net_amount = 0
count_profit_loss = 0
chg = 0
avg_chg = 0
max_chg = 0 
min_chg = 0 
total_months = 0 
count_total_months = 0 

#Sum the total and count variables 
for profit_loss in profit_losses:
    net_amount += profit_loss
    count_profit_loss += 1
print(net_amount)
print(count_profit_loss)

#Calculate the monthly change in profit loss row
z = 1
prev = profit_losses[0]
while z < len(profit_losses):
    chg = (profit_losses[z] - prev)
    print (chg)
    monthly_chg.append(chg)
    prev = profit_losses[z]
    z += 1

#Sum the total months 
total_monthly_chg = 0
chg = monthly_chg[0]
for chg in monthly_chg:
    total_monthly_chg = total_monthly_chg + chg
print(total_monthly_chg)

#Set the average change 
avg_chg = round(total_monthly_chg/(count_profit_loss -1),2)
print(avg_chg)

#Finding The Max And Min Changes
max_chg = max(monthly_chg)
print(max_chg)
min_chg = min(monthly_chg)
print(min_chg)

#Set Output Header
header = "Financial Analysis"
dash = "-------------------" 

#Printing the results 
print(header)
print(dash)
print(f"Total Months: {count_profit_loss}")
print(f"Total: ${net_amount}")
print(f"Average Change: ${avg_chg}")
print(f"Greatest Increase in Profits: {dates[25]} {max_chg}")
print(f"Greatest Decrease in Profits: {dates[44]} {min_chg}")

with open ('PyBank_Final',"w") as txt_file:
    txt_file.writer(f'Financial Analysis\n')
    txt_file.writer(f'--------------------\n')
    txt_file.writer(f'Total Months: {count_profit_loss}\n')
    txt_file.writer(f'Total: ${net_amount}\n')
    txt_file.writer(f'Average Change: ${avg_chg}\n')
    txt_file.writer(f'Greatest Increase in Profits: {dates[25]}{max_chg}\n')
