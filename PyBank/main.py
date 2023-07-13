import os
import csv

csvpath= os.path.join("Resources", "budget_data.csv")
export_file= os.path.join("analysis", "budget_analysis.txt")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    first_row = next(csvreader)

    print("Financial Analysis")
    print("---------------------------------------------------------")


    data = list(csvreader)
    months_count = len(data) + 1 
    print("Total Months:  " + str(months_count))
    
    
    total_value = 0
    total_value = total_value + int(first_row[1])
    previous = int(first_row[1])
    total_change = 0
    greatest_increase = 0
    greatest_increase_month = " "
    greatest_decrease = 0 
    greatest_decrease_month = " "

    for row in data: 
        total_value = total_value + int(row[1])
        current = int(row[1]) 
        change = current - previous
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]
        if change < greatest_decrease:
            greatest_decrease = change 
            greatest_decrease_month = row[0]
        total_change = total_change + change
        previous = current

    print("Total: " + "$"+str(total_value))
    print("Average Change: " + "$"+ str(round(total_change/(months_count -1),2)))
    print("Greatest Increase in Profits: " + greatest_increase_month + "  ($"+ str(greatest_increase) +")")
    print("Greatest Decrease in Profits: " + greatest_decrease_month + "  ($"+ str(greatest_decrease) +")")


    output = (
        f"Financial Analysis\n"
        f"---------------------------\n"
        f"Total Months:  {months_count}\n"
        f"Total:  ${total_value}\n"
        f"Average Change: ${str(round(total_change/(months_count -1),2))}\n"
        f"Greatest Increase in Profits:  {greatest_increase_month} (${greatest_increase})\n"
        f"Greatest Decrease in Profits:  {greatest_decrease_month} (${greatest_decrease})"
    )

with open(export_file, "w") as txt_file:
    txt_file.write(output)

 
            




 
