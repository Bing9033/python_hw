import os
import csv

def Pybank(filepath):
    date=[]
    revenuedata = []
    revenuechange = [0]
    row_count = 0
    total = 0
    totalchange = 0
    with open(filepath, 'r') as budget_data:
        csvreader = csv.reader(budget_data, delimiter=",")
        csv_header = next(csvreader)
        for row in csvreader:
            date.append(row[0])
            revenuedata.append(row[1]) 
            row_count += 1
            total += int(row[1])
        for i in range(1, row_count):
            revenuechange.append(int(revenuedata[i]) - int(revenuedata[i-1]))   
        max_increase = max(revenuechange)  
        max_increasedate = str(date[revenuechange.index(max_increase)])    
        max_decrease = min(revenuechange)    
        max_decreasedate = str(date[revenuechange.index(max_decrease)])             
        dollartotal = '${:.0f}'.format(total)
        average = sum(revenuechange) / (len(revenuechange)-1)
        dollaraverage = '${:.2f}'.format(average)
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(row_count)}")
    print(f"Total: {str(dollartotal)}")
    print(f"Average  Change: {str(dollaraverage)}")
    print("Greatest Increase in Profit:", max_increasedate,"($",max_increase,")")
    print("Greatest Decrease in Profit:", max_decreasedate,"($",max_decrease,")")


filepath = "Resources_pybank/budget_data.csv"
Pybank(filepath)
