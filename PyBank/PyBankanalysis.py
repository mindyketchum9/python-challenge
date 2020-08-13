#Import Modules
import os
import csv

#variables / initial states
date = []
money = []

sum_total = 0

avg_money = 0

#create a file path
PyBank_csv = os.path.join('C:/BootCamp in class/ku-edw-data-pt-07-2020-u-c/02-Homework/03-Python/Instructions/PyBank/Resources',"budget_data.csv")

#read csv_reader

with open (PyBank_csv,newline='') as csvFile:
    csv_reader = csv.reader(csvFile, delimiter=',')
    csv_header = next(csv_reader)
    line_count = 0

#print(csv_header)  

#reading csv
with open('C:\\BootCamp in class\\ku-edw-data-pt-07-2020-u-c\\02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

#for loop through data, appends lists, and increases counters
    for row in csvreader:
        date.append(row[0])
        money.append(int(row[1]))
        sum_total += float(row[1])
#print(row)

#total months
months = len(date)

#loops through money indices and compares to find greates increase and decrease 
increase=money[0]
decrease=money[0]

for i in range(len(money)):
    if money[i] >= increase:
        increase = money[i]
        increase_month = date[i]
    elif money[i] <= decrease:
        decrease = money[i]
        decrease_month = date[i]
    else:
        print('Increase/Decrease Error')
        print("-----------------------------------")
        print(f'Total Months: {months}')
        print(f'Total Revenue: ${sum_total}')
        print(f'Average Profit/Loss Change: ${avg_money}')
        print(f'Greatest Increase Profit/Loss: {increase_month}(${increase})')
        print(f'Greatest Decrease Profit/Loss: {decrease_month}(${decrease})')
        print("-----------------------------------")

with open('output_financial.txt', "w") as csvfile:
    csvfile.write('Increase/Decrease Error')
    csvfile.write("-----------------------------------")
    csvfile.write(f'Total Months: {months}')
    csvfile.write(f'Total Revenue: ${sum_total}')
    csvfile.write(f'Average Profit/Loss Change: ${avg_money}')
    csvfile.write(f'Greatest Increase Profit/Loss: {increase_month}(${increase})')
    csvfile.write(f'Greatest Decrease Profit/Loss: {decrease_month}(${decrease})')
    csvfile.write("-----------------------------------")

